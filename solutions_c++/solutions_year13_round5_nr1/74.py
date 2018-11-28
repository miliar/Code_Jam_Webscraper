#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<set>
#include<algorithm>
#include<iostream>
using namespace std;
typedef long long ll;
double calE(vector<pair<ll,ll> > &v,int cntMin,ll minV){
    double z=0.0;
    //printf("%d %lld\n",cntMin,minV);
    //int cntMin=0;
    double r=36.0/cntMin;
    for(int j=0;j<37;j++){
        if(v[j].first==minV){
            z+=r*v[j].second;
        }
        //else break;
    }
    //printf("z= %lf\n",z);
    return z;
}
void solve(){
    ll b;
    ll n;
    scanf("%lld %lld",&b,&n);
    vector<pair<ll,ll > > v;

    for(int i=0;i<n;i++){
        ll a;
        scanf("%lld",&a);
        v.push_back ( make_pair(a,0)  ) ;
    }
    if(n==0||n==1){
        printf("%.10lf\n",0);
        return ;
    }
    for(int i=0;i<37-n;i++){
        v.push_back(make_pair(0,0));
    }
    v.push_back(make_pair(100000000000000LL,0));
    double ans=0;
    ll rem=b;
    while(rem){
        //printf("a\n");

        sort(v.begin(),v.end());
        //for(int i=0;i< v.size();i++)printf("%lld ",v[i].first);
        //printf("\n");
        int nxt=0;
        while(nxt<v.size()&&v[nxt].first==v[0].first)nxt++;

        ll mx=v[nxt].first-v[0].first-1;
        ans=max(ans,calE(v,nxt,v[0].first)-(b-rem));
        //printf("%d %lld\n",nxt,mx);
        //system("pause");
        if(rem<nxt){
            //printf("remlnxt %lld %d\n",rem,nxt);
            for(int i=0;rem;i++){

                v[i].first++;
                v[i].second++;
                rem--;
                ans=max(ans,calE(v,nxt-i-1,v[nxt-1].first)-(b-rem));
            }
        //for(int i=0;i< v.size();i++)printf("%lld ",v[i].first);
        //printf("\n");
            break;
        }
        for(int i=0;i<nxt;i++){
            v[i].first++;
            v[i].second++;
            rem--;
            if(i+1<nxt)
            ans=max(ans,calE(v,nxt-i-1,v[nxt-1].first)-(b-rem));
        }

        for(int i=0;i<nxt;i++){
            v[i].first--;
            v[i].second--;
            rem++;
            //ans=max(ans,calE(v,nxt-i-1,v[nxt-1].first)-(b-rem));
        }

        if(mx==0){
            for(int i=0;i<nxt;i++){
                v[i].first++;
                v[i].second++;
                rem--;
                if(nxt>i+1)
                ans=max(ans,calE(v,nxt-i-1,v[nxt-1].first)-(b-rem));
            }
            while(nxt<v.size()&&v[nxt].first==v[0].first)nxt++;
            ans=max(ans,calE(v,nxt,v[0].first)-(b-rem));
            continue;
        }
        mx=min(mx,rem/nxt);
        //printf("mx=%d\n",mx);
        rem-=mx*nxt;
        for(int i=0;i<nxt;i++){
            v[i].first+=mx;
            v[i].second+=mx;
            //rem-=mx;
        }
        for(int i=nxt-1;i>=0;i--){
            v[i].first--;
            v[i].second--;
            rem++;
            ans=max(ans,calE(v,nxt-i,v[i].first)-(b-rem));
        }
        for(int i=0;i<nxt;i++){
            v[i].first++;
            v[i].second++;
            rem--;
                //ans=max(ans,calE(v,nxt-i-1,v[nxt-1].first)-(b-rem));
        }
        if(v[nxt].first>v[0].first)
            ans=max(ans,calE(v,nxt,v[0].first)-(b-rem));
        else{
            while(nxt<v.size()&&v[nxt].first==v[0].first)nxt++;
            ans=max(ans,calE(v,nxt,v[0].first)-(b-rem));
        }
    }
    printf("%.10lf\n",ans);
}
int main(){
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++){
        printf("Case #%d: ",i);
        solve();
    }
}
