#include<stdio.h>
#include<math.h>
#include<string.h>
#include<algorithm>
#include<vector>
#include<set>
#include<iostream>
#include<map>
#include<queue>
#include<bitset>
#include<string>
#include<stdlib.h>
#include<sstream>
#include<stack>
#define pb push_back
#define MOD 1000002013
using namespace std;
int cs,N,M;
long long cost(long long x){
    return (N+(N-x+1))*x/2;
}
struct data{
    int x,ty,num;
    data(int _x=0,int _ty=0,int _num=0){x=_x;ty=_ty;num=_num;}
    bool operator<(const data& b)const{
        return x<b.x||(x==b.x&&ty>b.ty);
    }
};
int main(){
    int T,i,j,k;
    scanf("%d",&T);
    while(T--){
        long long res=0;
        vector<data>qq;
        cin>>N>>M;
        for(i=0;i<M;i++){
            int o,e,p;
            scanf("%d%d%d",&o,&e,&p);
            res+=cost(e-o)*p%MOD;
            qq.pb(data(o,1,p));
            qq.pb(data(e,-1,p));
        }
        res%=MOD;
        sort(qq.begin(),qq.end());
        stack<pair<int,int> >pp;
        for(i=0;i<qq.size();i++){
            if(qq[i].ty==1){
                pp.push(make_pair(qq[i].x,qq[i].num));
            }
            else{
                while(qq[i].num>0){
                    int use=min(pp.top().second,qq[i].num);
                    qq[i].num-=use;
                    pp.top().second-=use;
                    res-=cost(qq[i].x-pp.top().first)*use%MOD;
                    res%=MOD;
                    if(pp.top().second==0)pp.pop();
                }
            }
        }
        if(res<0)res+=MOD;
        printf("Case #%d: %lld\n",++cs,res);
    }
    return 0;
}

