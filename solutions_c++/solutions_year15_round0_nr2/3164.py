#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<algorithm>
#include<cmath>
   
using namespace std;

const int MAXN = 1005;
int num[MAXN];

int main(){
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++){
    	int N;
    	scanf("%d",&N);
        int mx = 0;
    	for(int j=0;j<N;j++){
    		scanf("%d",&num[j]);
        	mx = max(mx,num[j]);
    	}

        int mn = 0x3f3f3f3f;
        for(int base=1;base<=mx;base++){
            int cnt = 0;
            for(int j= 0;j<N;j++){
                cnt += (num[j] + base - 1)/base - 1;
            }

            mn = min(mn,cnt+base);
        }

    	printf("Case #%d: %d\n",i,mn);
	}
}
