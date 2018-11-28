#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <cmath>
#include <deque>
#include <bitset>
#include <cstdio>
#include <vector>
#include <string>
#include <complex>
#include <sstream>
#include <utility>
#include <climits>
#include <cstring>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <algorithm>

#define OO (int) 1e9

using namespace std;

int gcd(int u, int v) {return (v != 0)?gcd(v, u%v):u;}

int main()
{
	freopen("D-small-attempt4.in","r",stdin);
	freopen("out.txt","w",stdout);

	int tc;
	cin>>tc;
	for(int j=1;j<=tc;j++)
	{ 
		int x,r,c;
		cin>>x>>r>>c;

		if(r > c) swap(r,c);

		bool gab=0;

		cout<<"Case #"<<j<<": ";
		if(x==1)
			gab=1;
		else if (x==2)
		{
			if(r%2==0 || c%2==0) 
				gab=1;
			else 
				gab=0;
		}
		else if (x==3)
		{
			if((r==2 && c==3 )||(r==3 && c==4)||(r==3 && c==3)) 
				gab=1;
			else 
				gab=0;
		}
		else if(x==4)
		{
			if((r==3 || r==4) && c==4)
				gab=1;
			else 
				gab=0;
		}
		if(gab)
			cout<<"GABRIEL"<<endl;
		else cout<<"RICHARD"<<endl;

	}

}

