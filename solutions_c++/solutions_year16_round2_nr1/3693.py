
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cfloat>
#include <climits>
#include <cmath>
#include <cstring>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
 
using namespace std;
 
int a[26],c[10];
int main()
{
	string s;int T;
	cin>>T;
	for(int t=1;t<=T;++t)
	{
		for(int i=0; i<10;++i)c[i]=0;
		for(int i=0; i<26;++i)a[i]=0;
		cin >>s;
		for(int i=0; i<s.size();++i)
		{
			a[s[i]-'A']++;
			if(s[i]=='W')c[2]++;
			if(s[i]=='Z')c[0]++;
			if(s[i]=='G')c[8]++;
			if(s[i]=='U')c[4]++;
			if(s[i]=='X')c[6]++;
		}
		c[3]=a['T'-'A']-c[2]-c[8];
		c[7]=a['S'-'A']-c[6];
		c[5]=a['V'-'A']-c[7];
		c[9]=a['I'-'A']-c[8]-c[6]-c[5];
		c[1]=a['O'-'A']-c[2]-c[0]-c[4];
		cout<<"Case #" <<t<<": ";
		for(int i=0;i<10;++i)
		{
			while(c[i]--)
			
			{
				cout<<i;
			}
		}
		cout<<endl;
	}
	return 0;
}