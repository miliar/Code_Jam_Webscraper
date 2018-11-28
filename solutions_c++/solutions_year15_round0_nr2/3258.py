#include<iostream>
#include<algorithm>
#include<cstring>
#include<cstdio>
#include<cmath>
using namespace std;
typedef long long LL;
const int MAXN=1000+10;

int a[MAXN];

int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T,n,id=0,x;
    cin>>T;
    while(T--){
        memset(a,0,sizeof(a));
        cin>>n;
        while(n--){
            cin>>x;
            for(int i=1;i<x;i++)a[i]+=ceil(1.0*x/i)-1;
        }
        int mins=999999999;
        for(int i=1;i<MAXN;i++)mins=min(mins,a[i]+i);
        printf("Case #%d: %d\n",++id,mins);
    }
	return 0;
}
