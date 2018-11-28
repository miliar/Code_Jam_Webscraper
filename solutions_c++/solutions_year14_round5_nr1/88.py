#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<vector>
using namespace std;

long long ctr[1010000];

void solve(){
        long long N,p,q,r,s;
        long long all = 0;
        scanf("%lld %lld %lld %lld %lld",&N,&p,&q,&r,&s);
        for(int i = 0 ; i < N ; ++ i ){
          ctr[i]=1LL*(1LL*(i)*p+q)%r+s;
          all+=ctr[i];
          //if(i)ctr[i]+=ctr[i-1];
        }
        long long mx = 0 ;

        long long st = 0;
        long long e = all;
        while(st<=e){
            long long mid = (st+e)/2;
            vector<long long> tmp;
            long long cache =0;
            bool ok =false;
            long long localMx=0;
            for(int i = 0 ; i < N ; ++ i ){
                if(cache+ctr[i]>mid){
                    localMx=max(localMx,cache);
                    tmp.push_back(cache);
                    cache=0;
                }

                cache+=ctr[i];
            }
            localMx=max(localMx,cache);
            tmp.push_back(cache);

            if(tmp.size()==3||tmp.size()==2)ok=true;
            if(ok){
                mx=max(mx,all-localMx);
                e=mid-1;
            }
            else{
                st=mid+1;
            }
            //printf("mid ok %lld %d\n",mid,ok);
        }
        printf("%.10lf\n",1.0*mx/all);
}

int main(){
    freopen("A-large"".in","r",stdin);
    freopen("ans2"".out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int i = 1 ; i<= t ; ++ i ){
		printf("Case #%d: ",i);
		solve();
	}



}
