#include<algorithm>
#include<array>
#include<fstream>
#include<iostream>
#include<string>
#include<utility>
#include<vector>
using namespace std;

int main()
{
	int T;
	ifstream ifs{"B.in"};
	ifs>>T;
	ofstream ofs{"output.txt"};
	for(int case_i{0};case_i!=T;++case_i)
	{
		string str;
		ifs>>str;
		int count{0};
		for(int i{1};i<str.size();++i)
			if(str[i-1]!=str[i])
				++count;
		if(str.back()=='-')
			++count;
		ofs<<"Case #"<<case_i+1<<": "<<count<<endl;
	}
}

//bool split_and_count(unsigned long long N,array<bool,10> &accu)
//{
//	while(N)
//	{
//		accu[N%10]=true;
//		N/=10;
//		if(all_of(begin(accu),end(accu),[](const auto b){return b;}))
//			return false;
//	}
//	return true;
//}
//
//int main()
//{
//	unsigned long long T;
//	unsigned long long N;
//	ifstream ifs{"A.in"};
//	ifs>>T;
//	ofstream ofs{"output.txt"};
//	for(int case_i{0};case_i!=T;++case_i)
//	{
//		ifs>>N;
//		if(!N)
//		{
//			ofs<<"Case #"<<case_i+1<<": INSOMNIA"<<endl;
//			continue;
//		}
//		array<bool,10> accu{false,false,false,false,false,false,false,false,false,false};
//		int i{0};
//		while(split_and_count(++i*N,accu))
//			;
//		ofs<<"Case #"<<case_i+1<<": "<<i*N<<endl;
//	}
//}