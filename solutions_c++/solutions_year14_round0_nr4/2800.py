#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;

#define forn(i,n) for(int i=0; i<(int)(n); i++)

int cards[32];
double v1[1024];
double v2[1024];
int used[1024];

int main(){
	int t; cin>>t;
	forn(tc,t){
		int n; cin>>n;
		forn(i,n)cin>>v1[i];
		forn(i,n)cin>>v2[i];
		forn(i,n)used[i]=0;
		sort(v1,v1+n);
		sort(v2,v2+n);
		int best1 = 0;
		int pos = 0;
		forn(i,n){
			if(v1[i]>v2[pos]){
				best1++;
				pos++;
			}
			//if(v1[i]<v2[n-1-i])best--;
			//else break;
		}
		int best2 = 0;
		forn(i,n){
			forn(j,n){
				if(used[j]==0 && v1[i]<v2[j]){
					used[j]=1;
					break;
				}
			}
		}
		forn(i,n)if(used[i]==0)best2++;
		printf("Case #%d: %d %d\n",tc+1,best1,best2);
	}
}
