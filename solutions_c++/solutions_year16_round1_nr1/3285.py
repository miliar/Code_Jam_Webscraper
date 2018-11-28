#include<algorithm>
#include<array>
#include<bitset>
#include<cstring>
#include<deque>
#include<functional>
#include<fstream>
#include<iomanip>
#include<iostream>
#include<iterator>
#include<limits>
#include<memory>
#include<queue>
#include<stack>
#include<string>
#include<typeinfo>
#include<type_traits>
#include<unordered_map>
#include<unordered_set>
#include<utility>
#include<vector>
using namespace std;

int main()
{
	int T;
	ifstream ifs{"in"};
	ifs>>T;
	ofstream ofs{"out"};
	for(int case_i{0};case_i!=T;++case_i)
	{
		string in;
		ifs>>in;
		string out{in[0]};
		for(size_t i{1};i!=in.size();++i)
			if(in[i]>=out[0])
				out.insert(0,1,in[i]);
			else
				out.push_back(in[i]);
		ofs<<"Case #"<<case_i+1<<": "<<out<<endl;
	}
}