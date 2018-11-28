/**
Coded by:-   Himanshu (RogueH)
**/
#include <iostream>
#include <vector>
#include <string>
#include <utility>
#include <cmath>
#include <algorithm>
#include <cstdio>
#include <queue>
#include <sstream>
#include <map>
#include <set>
#include <bitset>
#include <iomanip>

#define LL long long int
#define SF second.first
#define SS second.second
#define mP make_pair
#define pB push_back
#define F first
#define S second
#define castInt static_cast<int>
#define castLong static_cast<long long int>

using namespace std;

int main()
{
	int T,cases;
	double c,f,t,cpt,x;
	cin>>T;
	for(cases=1; cases<=T; cases++)
	{
		cin>>c>>f>>x;
		t=0;
		cpt=2;
		while(x/cpt > c/cpt + x/(cpt+f))
		{
			t+=c/cpt;
			cpt+=f;
		}
		t+=x/cpt;
		cout<<fixed<<setprecision(7)<<"Case #"<<cases<<": "<<t<<endl;
	}
	return 0;
}

