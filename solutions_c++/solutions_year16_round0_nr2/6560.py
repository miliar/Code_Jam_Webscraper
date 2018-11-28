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
	freopen("B-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t,X=1;
	cin>>t;
	while(t--)
	{
		string s;
		cin>>s;
		int step=0;
		queue<char>curr;
		stack<char>curr1;

		while(true)
		{
			bool ok=1;

			for(int i=0;i<s.size();i++)
			{
				curr.push(s[i]);
				ok&=(s[i]=='+');
			}

			if(ok)
				break;
			char last=curr.front(),last1;

			for(int i=0;i<s.size();i++)
			{
				last1=curr.front();

				if(last!=last1)
					break;
				curr.pop();
				if(last1=='+')
					last1='-';
				else
					last1='+';
				curr1.push(last1);
			}

			s="";

			while(!curr1.empty())
				s+=curr1.top(),curr1.pop();

			while(!curr.empty())
				s+=curr.front(),curr.pop();

			step++;
		}
		cout<<"Case #"<<X++<<": "<<step<<endl;
	}
}
