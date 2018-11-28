#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <algorithm>
#include <iostream>
#include <string>
using namespace std;

int h[5],g[5],P,Q,N,ans,ed,a[5],b[5];
map <pair<int,long long>,int> MAP;

int dfs(int lv,int mk){
	if(mk==ed){
		return 0;
	}
	//printf("fir lv = %d, sc = %d, mk = %d\n",lv,sc,mk);
	long long mask = 0;
	/*for(int i=0;i<N;i++){
		mask = mask*11+a[i];
		mask = mask*11+b[i];
	}*/
	for(int i=0;i<N;i++){
		if(h[i]>0)	mask = mask*1000 + h[i];
		else	mask *= 1000;
	}
	if(MAP.find(make_pair(lv,mask))!=MAP.end())
		return MAP[make_pair(lv,mask)];
	/*for(int i=0;i<N;i++)
		printf("%d ",h[i]);
	printf("\nsec lv = %d, sc = %d, mk = %d, mask = %013lld\n",lv,sc,mk,mask);*/
	int maxi = 0;
	if(lv&1){  // second
		for(int i=0;i<N;i++){
			if((mk & (1<<i))==0){
				h[i] -= Q;
				b[i]++;
				if(h[i]<1)	maxi = max(maxi,dfs(lv+1,mk|(1<<i)));
				else	maxi = max(maxi,dfs(lv+1,mk));
				h[i] += Q;
				b[i]--;
				break;
			}
		}
	}else{  // first
		for(int i=0;i<N;i++){
			if((mk & (1<<i))==0){
				h[i] -= P;
				a[i]++;
				if(h[i]<1)	maxi = max(maxi,dfs(lv+1,mk|(1<<i))+g[i]);
				else	maxi = max(maxi,dfs(lv+1,mk));
				h[i] += P;
				a[i]--;
			}
		}
		maxi = max(maxi,dfs(lv+1,mk));
	}
	return MAP[make_pair(lv,mask)] = maxi;
}

int main()
{
    freopen("B-small-attempt1.in","r",stdin);
	//freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    
    int T;
	cin >> T;
	for(int t=0;t<T;t++){
		cin >> P >> Q >> N;
		MAP.clear();
		memset(a,0,sizeof(a));
		memset(b,0,sizeof(b));
		for(int i=0;i<N;i++)
			cin >> h[i] >> g[i];
		ans = 0;
		ed = (1<<N)-1;
		printf("Case #%d: %d\n",t+1,dfs(0,0));
		fprintf(stderr,"%d\n",t+1);
	}
    
    return 0;
}