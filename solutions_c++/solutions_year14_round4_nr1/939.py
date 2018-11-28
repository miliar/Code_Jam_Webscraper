#include <vector>
#include <string>
#include <map>
#include <unordered_map>
#include <fstream>
#include <algorithm>
#include <cassert>
#include <iostream>

using namespace std;

struct Case{
	int disc;
	vector<int> files;

	int Solve() {
		int result = 0;

		sort(files.begin(), files.end());
		int i1 = 0, i2 = files.size() - 1;
		while (i1 < i2)	{
			++result;
			if (files[i1] + files[i2] <= disc)
				++i1;				
			--i2;
		}
		if (i1 == i2)
			++result;

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
			int file_num;
			ifs >> file_num >> cas.disc;
			cas.files.resize(file_num);
			for (int i = 0; i < file_num; ++i)
				ifs >> cas.files[i];
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

