#include <vector>
#include <string>
#include <map>
#include <unordered_map>
#include <fstream>
#include <algorithm>
#include <cassert>
#include <iostream>

#undef min
using namespace std;

struct Case{
	vector<int> v;

	int Solve() {
		int result = 0;		

		while (v.size() > 2) {
			size_t mn_ind = 0;
			for (size_t i = 1; i < v.size(); ++i) {
				if (v[i] < v[mn_ind])
					mn_ind = i;				
			}
			result += min(mn_ind, v.size() - 1 - mn_ind);
			v.erase(v.begin() + mn_ind);
		}

		return result;		
	}
};


struct Input{
	vector<Case> cases;

	Input(){
		ifstream ifs("i");
		assert(!ifs.bad());

		int case_num;
		ifs >> case_num;
		cases.resize(case_num);
		for (int case_ind = 0; case_ind < case_num; ++case_ind)
		{
			Case&
				cas = cases[case_ind];
			int num;
			ifs >> num;
			cas.v.resize(num);
			for (int i = 0; i < num; ++i)
				ifs >> cas.v[i];
		}
	}
};


int main()
{
	Input inp;
	
	ofstream ofs("o.txt");	
	for (size_t i = 0; i < inp.cases.size(); ++i)
	{
		int answer = inp.cases[i].Solve();
		ofs << "Case #" << (i+1) << ": " << answer << endl;
	}

	return 0;
}

