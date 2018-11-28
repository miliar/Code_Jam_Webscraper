#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <vector>
#include <cassert>
#include <sstream>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <utility>
#include <string>

#define pb push_back
#define mp make_pair
#define clr(x) x.clear()
#define sz(x) ((int)(x).size())
#define pii pair<int, int>
#define pn(n) printf("%d\n",n)
#define sn(n) scanf("%d",&n)
#define tr(container , it) for(typeof(container.begin()) it=container.begin() ; it!=container.end() ; it++)

#define FORN(i, n) for(i = 0; i < n; i++)
#define FORAB(i,a,b) for(i = a; i <= b; i++)
	
typedef long long int li;
using namespace std;

int main(){
	int test;
	sn(test);
	int no=1;
	while(test--){

		int n;
		sn(n);
		string a[n];
		for (int i = 0; i < n; ++i)
		{
			cin >> a[i];
		}
		string uni[n];
		vector<int> count[n];
		for (int i = 0; i < n; ++i)
		{
			for (int j = 0; j < (int)a[i].length(); ++j)
			{
				if(j==0){
					uni[i]+=a[i][j];
					count[i].pb(1);
				}
				else{
					//printf("%c %c\n",uni[i][(int)uni[i].length()-1],a[i][j] );
					if(uni[i][(int)uni[i].length()-1]==a[i][j]){
						count[i][sz(count[i])-1]++;
					}
					else{
						//printf("adding\n");
						uni[i]+=a[i][j];
						count[i].pb(1);
					}
				}
			}
		}
		//printf("out\n");
		int flagyes=1;
		for (int i = 0; i < n-1; ++i)
		{
			if(uni[i]==uni[i+1]);
			else{
				flagyes=0;
			}
		}
		printf("Case #%d: ",no );
		no++;
		if(flagyes==1){
			int finalans=0;
			for (int j = 0; j < sz(count[0]); ++j)
			{
				int temparr[n];
				for (int i = 0; i < n; ++i)
				{
					temparr[i]=count[i][j];
				}
				int maxequal[1000];
				for (int i = 0; i < 1000; ++i)
				{
					maxequal[i]=0;
				}
				for (int i = 0; i < n; ++i)
				{
					maxequal[temparr[i]]++;
				}
				int index=0;
				for (int i = 0; i < 1000; ++i)
				{
					if(maxequal[i]>maxequal[index]){
						index=i;
					}
				}
				//printf("maxequal is %d\n",maxequal[index] );
				for (int i = 0; i < n; ++i)
				{
					finalans+=abs(temparr[i]-index);
				}
				//printf("**%d\n",finalans );
			}
			printf("%d\n",finalans );
		}
		else{
			printf("Fegla Won\n");
		}
	}
	return 0;
}

