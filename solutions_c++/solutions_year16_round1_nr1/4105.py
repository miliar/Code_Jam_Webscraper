#include <iostream>
#include <string>
#include <algorithm>
#include <iomanip>
#include <sstream>
#include <math.h>
#include <stdlib.h>
#include <cstdlib>
#include <stdio.h>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <fstream>
#include <stack>
#include <queue>
#include <deque>
#include <list>
#include <vector>
#include <map>
#include <set>
using namespace std;
const unsigned long long O = 2e9;
const double E = 1e-13;
const double pi = 3.1415926536;
int DX[] = { 1, -1, 0, 0 };
int DY[] = { 0, 0, 1, -1 };

/*bool valid(int x, int y)
{
    return ((x >= 0 && x<n) && (y >= 0 && y<n));
}*/
int main(){
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t,X=1;
	cin>>t;
	while(t--)
	{
		string s,res;
		cin>>s;
		char mini=s[0];
		int ind=0;
		bool vis[1002]={};
		for(int i=0;i<s.size();i++)
		{
			bool ok=0;
			for(int j=i+1;j<s.size();j++)
				if(mini<=s[j] )
					{ok=1;mini=s[j],ind=j;break;}
			if(ok)
				res=s[ind]+res,vis[ind]=1,s.erase(s.begin()+ind),i--;
			else
				res+=s[i];
		}
		cout<<"Case #"<<X++<<": "<<res<<endl;
	}
}
