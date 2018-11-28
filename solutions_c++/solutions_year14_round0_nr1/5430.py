#pragma comment(linker, "/STACK:64000000")
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
	int a[4][4],b[4][4],p1,p2,n;
	forn(t,T)
	{
		cout<<"Case #"<<(t+1)<<": ";

		cin>>p1;
		p1--;
		forn(i,4)
			forn(j,4)
				cin>>a[i][j];

		cin>>p2;
		p2--;
		forn(i,4)
			forn(j,4)
				cin>>b[i][j];

		n=-1;
		for (int j1=0;j1<4 && (n!=-2);j1++)
			for (int j2=0;j2<4 && (n!=-2);j2++)
				if(a[p1][j1] == b[p2][j2]){
					if (n==-1)
						n=a[p1][j1];
					else
						n=-2;
				}

		if (n==-2)
			cout<<"Bad magician!\n";
		else
		if (n==-1)
			cout<<"Volunteer cheated!\n";
		else
			cout<<n<<"\n";
	}
}