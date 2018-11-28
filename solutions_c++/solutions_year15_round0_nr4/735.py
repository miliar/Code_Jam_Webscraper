#include <iostream>
#include <fstream>
#include <iomanip>
#include <math.h>
#include <limits.h>
#include <algorithm>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <bitset>
#include <string>
#include <string.h>
#include <sstream>
#include <ctime>
 
using namespace std;
 
typedef long long ll;
typedef unsigned long long ull;

bool g;
int x,r,c,cases,s1,s2,l,w;
int main()
{
	std::ios::sync_with_stdio(false);
	//freopen("in.txt","r",stdin);
	//freopen("out.txt","w",stdout);
	cin>>cases;
	for(int kase=1;kase<=cases;kase++)
	{
		cin>>x>>r>>c;
		cout<<"Case #"<<kase<<": ";
		if(x==1)
		{
			cout<<"GABRIEL\n";
			continue;
		}
		if(x==2 && (r*c)%x==0)
		{
			cout<<"GABRIEL\n";
			continue;
		}
		if(x==3 && (r*c)%x==0)
		{
			if(r==1 || c==1)
			{
				cout<<"RICHARD\n";
			    continue;
			}
			else
			{
				cout<<"GABRIEL\n";
			    continue;
			}
		}
		if(x==4 && (r*c)%x==0)
		{
			if(r==1 || c==1 || r==2 || c==2)
			{
				cout<<"RICHARD\n";
			    continue;
			}
			else
			{
				cout<<"GABRIEL\n";
			    continue;
			}
		}
		if(x==5 && (r*c)%x==0)
		{
			if(r==1 || c==1 ||r==2 ||c==2)
			{
				cout<<"RICHARD\n";
			    continue;
			}
			else
			{
				cout<<"GABRIEL\n";
			    continue;
			}
		}
		if(x==6 && (r*c)%x==0)
		{
			if(r==1 || c==1 || r==2 || c==2 || (r<6&&c<6))
			{
				cout<<"RICHARD\n";
			    continue;
			}
			else
			{
				cout<<"GABRIEL\n";
			    continue;
			}
		}
		if(x>=7 || (r*c)%x!=0)
		{
			cout<<"RICHARD\n";
			continue;
		}
		
	}
	return 0;
}