#include <cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <cstdlib>
#include <deque>
#include <set>
#include <map>
#include <list>
#include <limits>
#include <queue>
#include <stdexcept>
#include <iomanip> 
#include <sstream>
using namespace std;
#define RR 50
#define CC 50
char str[RR][CC];
#define TRY
#define SMALL
//#define LARGE
long Solve(vector<string> w)
{
	int len=w.size();
	string x,y,z;
	x=w[0];//gai
	y=w[1];
	int len1=x.length();
	int len2=y.length();
	int numm=0;
	int ab=0;
	int ii,jj;
	
		if(x[0]!=y[0])
			return -1;
		int i=1;int j=1;
		while (i<len1 && j<len2)
		{
			ii=i;jj=j;
			if(x[i]!=y[j])
			{
				if(x[i]==x[i-1])
				{
					while(i<len1 && x[i]!=y[j])
					{
						i++;
					}
					if(i==len1)
						return -1;
					numm+=((i-ii)-(j-jj));
				}
				else if(y[j]==y[j-1])
				{
					while(j<len2 && y[j]!=x[i])
					{
						j++;
					}
					if(j==len2)
						return -1;
					numm+=((j-jj)-(i-ii));
				}
				else
					return -1;
			}
			
			i++;j++;
			
			
		}
		if(j==len2)
		{
			for(;i<len1;i++){
				if(x[i]!=x[i-1])
					return -1;
				numm++;
			}
		}
		else if(i==len1)
		{
			for(;j<len2;j++){
				if(y[j]!=y[j-1])
					return -1;
				numm++;
			}
		}
		return numm;
	
}
int main() 
{
#ifdef TRY
	freopen("1.txt", "rt", stdin);
	freopen("2.out","wt",stdout);
#endif
#ifdef SMALL
	freopen("A-small-attempt0.in","rt",stdin);
	freopen("A-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
#endif
	int Numcase;
	cin>>Numcase;
	int n;
	string a,b;
	vector<string> p;
	for(int test=1;test<=Numcase;test++)
	{
		p.clear();
		cout<<"Case #"<<test<<": ";
		cin>>n;
		for(int i=0;i<n;i++){
			cin>>a;
			p.push_back(a);
		}
		long q=Solve(p);
		if(q==-1)
			cout<<"Fegla Won"<<endl;
		else
			cout<<q<<endl;
	}
}