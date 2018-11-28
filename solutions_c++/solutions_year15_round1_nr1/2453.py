//============================================================================
// Name        : shit.cpp
// Author      : SaMer
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <bits/stdc++.h>
#define mp make_pair
typedef long long ll;
using namespace std;
int arr[1111],n;
int main() {
#ifndef ONLINE_JUDGE
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
#endif
    int t;
    scanf("%d",&t);
    while(t--){
    	scanf("%d",&n);
    	int r=0;
    	for(int i=0;i<n;++i){
    		scanf("%d",arr+i);
    		if(i) r=max(r,arr[i-1]-arr[i]);
    	}
    	int y=0,z=0;
    	for(int i=0;i<n-1;++i){
    		if(arr[i]>arr[i+1]) y+=arr[i]-arr[i+1];
    		z+=min(r,arr[i]);
    	}
    	static int cas=1;
    	printf("Case #%d: %d %d\n",cas++,y,z);
    }
    return 0;
}

