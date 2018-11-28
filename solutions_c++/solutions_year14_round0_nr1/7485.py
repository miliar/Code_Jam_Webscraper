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
	int T,cases,sol,i,j,num,arr[17],cnt;
	cin>>T;
	for(cases=1; cases<=T; cases++)
	{
		cin>>sol;
		for(i=1;i<=16; i++)
			arr[i]=0;
		cnt=0;
		for(i=0; i<4; i++)
		{
			for(j=0; j<4; j++)
			{
				cin>>num;
				if(i+1==sol)
					arr[num]++;
			}
		}
		cin>>sol;
		for(i=0; i<4; i++)
		{
			for(j=0; j<4; j++)
			{
				cin>>num;
				if(i+1==sol)
					arr[num]++;
			}
		}
		for(i=1; i<=16; i++)
		{
			if(arr[i]==2)
			{
				num=i;
				cnt++;
			}
		}
		if(cnt==1)
			cout<<"Case #"<<cases<<": "<<num;
		else if(cnt==0)
			cout<<"Case #"<<cases<<": "<<"Volunteer cheated!";
		else
			cout<<"Case #"<<cases<<": "<<"Bad magician!";
		cout<<endl;
	}
	return 0;
}

