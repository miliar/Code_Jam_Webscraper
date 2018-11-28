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
string s,re;
int main(void){
	ifstream cin("C-large.in");
	ofstream cout("output.txt");
	std::ios::sync_with_stdio(false);cin.tie(0);
	int t,T;
	int i,n,m;
	int j,temp,x;
	cin>>T;
	for(t=1;t<=T;t++)
	{
		cin>>n>>m;
		cout<<"Case #"<<t<<":\n";
		s+='1';
		for(i=1;i<n-1;i++)
			s+='0';
		s+='1';
		for(i=0;i<m;i++)
		{
			re=s;
			temp=i;
			j=1;
			while(temp)
			{
				x=temp%2;
				if(x==1)
					re[j]=re[j+1]='1';
				j+=2;
				temp/=2;
			}
			cout<<re;
			for(j=2;j<=10;j++)
				cout<<' '<<j+1;
			cout<<'\n';
		}
	}
	system("pause");
	return 0;
}