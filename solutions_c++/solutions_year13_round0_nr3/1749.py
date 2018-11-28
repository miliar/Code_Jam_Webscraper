//============================================================================
// Name        : CodeJam.cpp
// Author      : diametralis
// Version     :
// Copyright   : Your copyright notice
// Description : Code Jam contest
//============================================================================

#include <iostream>
#include <fstream>
#include <string>
#include <cstring>
#include <vector>
using namespace std;

#define MAX 34
typedef long long ll;

class LM
{
public:
	void solve()
	{
		initData();

		ifstream infile("input");
		ofstream outfile("output");
		if(!infile.is_open())
			cout<<"error while opening";

		int T;
		infile>>T;
		for(int i=0; i<T; ++i)
		{
			ll start, end;
			infile>>start;
			infile>>end;
			int res=calc(start, end);
			outfile<<"Case #"<<(i+1)<<": "<<res<<endl;
		}

		infile.close();
		outfile.close();
	}
private:
	vector<ll> P;
	void initData()
	{
		P.push_back(1); P.push_back(4); P.push_back(9);
		P.push_back(121); P.push_back(484); P.push_back(10201);
		P.push_back(12321); P.push_back(14641); P.push_back(40804);
		P.push_back(44944); P.push_back(1002001); P.push_back(1234321);
		P.push_back(4008004); P.push_back(100020001); P.push_back(102030201);
		P.push_back(104060401); P.push_back(121242121); P.push_back(123454321);
		P.push_back(125686521); P.push_back(400080004); P.push_back(404090404);
		P.push_back(10000200001); P.push_back(10221412201); P.push_back(12102420121);
		P.push_back(12345654321); P.push_back(40000800004); P.push_back(1000002000001);
		P.push_back(1002003002001); P.push_back(1004006004001); P.push_back(1020304030201);
		P.push_back(1022325232201); P.push_back(1024348434201); P.push_back(1210024200121);
		P.push_back(1212225222121); P.push_back(1214428244121); P.push_back(1232346432321);
		P.push_back(1234567654321); P.push_back(4000008000004); P.push_back(4004009004004);
		P.push_back(100000020000001);
	}
	int calc(ll start, ll end)
	{
		int res=0;
		int cur=0;

		while(cur<P.size() && P[cur]<=end)
		{
			if(P[cur]>=start && P[cur]<=end)
				res++;
			cur++;
		}
		return res;
	}
};

int main() {
	LM lm;
	lm.solve();
	cout << "done" << endl;
	return 0;
}
