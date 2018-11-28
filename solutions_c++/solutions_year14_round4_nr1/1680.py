#pragma comment(linker, "/STACK:64000000")
#include <ctime>
#include <stdlib.h>
#include <fstream>
#include <iostream>
#include <vector>
#include <stdlib.h>
#include <stdio.h>
#include <cstring>
#include <map>
#include <set>
#include <string>
#include <deque>
#include <algorithm>
#define _USE_MATH_DEFINES
#include <math.h>
using namespace std;
#define forn(i,n) for (LL i=0;i<n;i++)
#define rforn(i,n) for (LL i=n-1;i>=0;i--)
#define mp make_pair
#define __int64 long long
#define LL long long

int main()
{
	ios_base::sync_with_stdio(false);
	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	#endif


	int T;
	cin>>T;
	LL n,x,e;
	vector <LL> a;
	forn(t,T)
	{
		int res=0;
		cin>>n>>x;

		a.resize(n);
		forn(i,n){
			cin>>a[i];
		}

		sort(a.begin(),a.end());
		LL l=0,y;
		LL r=n;
		LL step=1,pos;
		for (LL l=0;l<n;l++)
		{
			if (a[l]==-1)
				continue;
			res++;
			if (l>=r)
				continue;
			y=a[l];

			step=1;
			pos=l;
			while (step>0)
			{
				if (pos+step>=r){
					step/=2;
					continue;
				}
				e=a[pos+step];

				if (y+e<=x)
				{
					pos+=step;
					step*=2;					
				}
				else
				{
					step/=2;
				}
			}

			if (pos>l){
				a[pos]=-1;
				r=pos;
			}
			a[l]=-1;
		}


		cout<<"Case #"<<(t+1)<<": "<<res<<"\n";
	}

}