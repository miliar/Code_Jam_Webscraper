#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
using namespace std;
#define MOD 1000002013
//typedef pair<long long,long long> pi;

struct mys{
    long long o;
    long long e;
    long long p;
    int cnt;
};

vector<mys> holder;
vector<mys> sv;
long long rcst,cst;
long long n,m;

bool myf(mys x,mys y){
    if(x.o<y.o) return true;
    if(x.o==y.o && x.cnt<y.cnt) return true;
    return false;
}
long long clc(long long d,long long d2,long long p){
    long long res= (2*n);
    res= res*(d2-d);
    res= res- (d2*d2) + (d*d);
    res= res+ d2 - d;
    res=res/2;
    res= res%MOD;
    long long pp= p%MOD;
    res= (res*pp)%MOD;
    return res;
}

int main(){
    freopen("a.txt","rt",stdin);
    freopen("a.out","wt",stdout);
    int gt;
    cin>>gt;
    mys ts;
    for(int run=1;run<=gt;run++){
        sv.clear();rcst=0;cst=0;
        cin>>n>>m;
        for(int i=0;i<m;i++){
            cin>>ts.o;
            cin>>ts.e;
            cin>>ts.p;

            //cst+= clc(ts.e-ts.o,p);

            ts.cnt=1;
            sv.push_back(ts);
            long long tt= ts.o;
            ts.o=ts.e;
            ts.e=tt;
            ts.cnt=2;
            sv.push_back(ts);
        }
        sort(sv.begin(),sv.end(),myf);

        holder.clear();
        for(int i=0;i<sv.size();i++){
            if(sv[i].cnt==1){
                ts.o= sv[i].o;
                ts.p= sv[i].p;
                holder.push_back(ts);
            }
            else{
                long long curc= sv[i].p;
                for(int j=holder.size()-1;j>=0;j--){
                    if(curc<=0) break;
                    if(holder[j].p==0) continue;
                    if(curc<=holder[j].p){
                        holder[j].p-=curc;
                        rcst+= clc(sv[i].o-holder[j].o,sv[i].o-sv[i].e,curc);
                        curc=0;
                    }
                    else{
                        rcst+= clc(sv[i].o-holder[j].o,sv[i].o-sv[i].e,holder[j].p);
                        curc-=holder[j].p;
                        holder[j].p=0;
                    }
                }
            }


        }



        cout<<"Case #"<<run<<": "<<rcst<<endl;
    }
    return 0;
}



