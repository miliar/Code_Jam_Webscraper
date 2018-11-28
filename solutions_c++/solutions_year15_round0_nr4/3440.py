#include <vector>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <bitset>
#include <map>
#include <queue>
#include <climits>
#include <bitset>
#define LL long long
#define INFI 100000000000
#define D double
using namespace std;
#include <iomanip>


int main()
{
	
	LL t;
	cin>>t;
	LL tt=0;
	while(tt<t)
	{
		LL x,r,c;
		cin>>x>>r>>c;
		if(x == 1)
		{
			cout<<"Case #"<<tt+1<<": GABRIEL"<<endl;
		}
		else if(x == 2)
		{
			if(r%2 == 0 || c%2 == 0 || (r*c)%2 == 0)
			{
				cout<<"Case #"<<tt+1<<": GABRIEL"<<endl;
			}
			else
			{
				cout<<"Case #"<<tt+1<<": RICHARD"<<endl;
			}
		}
		else if(x == 3)
		{
			if(r>1 && c>1 && (r*c)%3 == 0)
			{
				cout<<"Case #"<<tt+1<<": GABRIEL"<<endl;
			}
			else
			{
				cout<<"Case #"<<tt+1<<": RICHARD"<<endl;
			}
		}
		else if(x == 4)
		{
			if(r > 2 && c > 2 && (r*c)%4 == 0)
			{
				cout<<"Case #"<<tt+1<<": GABRIEL"<<endl;
			}
			else
			{
				cout<<"Case #"<<tt+1<<": RICHARD"<<endl;
			}
		}
		tt++;
	}
	return 0;
	
}


//6 4
//1 3 2 3 4 1