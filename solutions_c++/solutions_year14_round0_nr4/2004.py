#include <iostream>
#include <iomanip>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sstream>
#include <math.h>
#include <limits.h>
#include <time.h>
#include <vector>
#include <utility>
#include <list>
#include <stack>
#include <queue>
#include <map>
#include <set>
using namespace std;

#define LIM_UI UINT_MAX
#define LIM_UL ULLONG_MAX
//iterations
#define repi(i,a,b) for(int i=a;i<=b;++i)
#define repd(i,a,b) for(int i=a;i>=b;--i)

#define MAX 1000
double naomi[MAX],ken[MAX];

int main(){
	ios::sync_with_stdio(false);
	int t,c=1,n;
	cin>>t;
	while(c<=t){
		cin>>n;
		repi(i,0,n-1)
			cin>>naomi[i];
		repi(i,0,n-1)
			cin>>ken[i];
		sort(naomi,naomi+n);
		sort(ken,ken+n);
		/*
		repi(i,0,n-1)
			cout<<naomi[i]<<" ";
		cout<<endl;
		repi(i,0,n-1)
			cout<<ken[i]<<" ";
		cout<<endl;*/

		int sn=0,sk=0,en=n-1,ek=n-1,i=0;
		int war=0;
		while(i<n){
			if(naomi[sn]<ken[sk]){
				++sn;
				++sk;
			}else{
				++war;
				++sk;
				--en;
			}
			++i;
		}

		sn=0,sk=0,en=n-1,ek=n-1,i=0;
		int dwar=0;
		while(i<n){
			if(naomi[sn]<ken[sk]){
				++sn;
				--ek;
			}else{
				++dwar;
				++sk;
				++sn;
			}
			++i;
		}
		cout<<"Case #"<<c<<": "<<dwar<<" "<<war<<"\n";
		++c;
	}
	return 0;
}