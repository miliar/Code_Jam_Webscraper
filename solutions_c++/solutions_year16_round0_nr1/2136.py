#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include<iomanip>
#include <algorithm>
#include <functional>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstdio>
#include <bitset>
using namespace std;
#define MOD 1000000007
int a[22];
int main(void){
	ifstream cin("A-large.in");
	ofstream cout("output.txt");
	std::ios::sync_with_stdio(false);cin.tie(0);
	int t,T;
	int i,n,tt,sum;
	int count,x;
	int re;
	cin>>T;
	for(t=1;t<=T;t++)
	{
		cin>>n;
		cout<<"Case #"<<t<<": ";
		if(n==0)
			cout<<"INSOMNIA"<<'\n';
		else
		{
			for(i=0;i<10;i++)
				a[i]=0;
			count=0;
			re=0;
			sum=0;
			while(count<10)
			{
				sum+=n;
				tt=sum;
				while(tt)
				{
					x=tt%10;
					if(a[x]==0)
					{
						count++;
						a[x]=1;
					}
					tt/=10;
				}
				re++;
			}
			cout<<sum<<'\n';
		}
	}
	system("pause");
	return 0;
}