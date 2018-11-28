#include<iostream>
#include<map>
using namespace std;

typedef long long LL;

const LL MD = 1000002013;

int T;
int N,M;
int O[1010],E[1010],P[1010];

map<int,LL> m;
LL start[10000];
LL pop[100000];
int lc;

LL calc(int diff,LL pop){
    if(diff==0) return 0;
    LL ret = diff*N;
    LL t1 = diff;
    t1=t1*(diff-1);
    return (ret-t1/2)*pop;
}


int main(){
    int i,j,k;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>T;
    for(int cs=1;cs<=T;++cs){
        cin>>N>>M;
        m.clear();
        LL res = 0;
        for(i=0;i<M;++i){
            cin>>O[i]>>E[i]>>P[i];
            m[2*O[i]]+=P[i];
            m[2*E[i]+1]+=P[i];
            res = res+calc(E[i]-O[i],P[i]);
            res%=MD;
        }
        lc = 0;
        LL res1 = 0;
        for(map<int,LL>::iterator it= m.begin();it!=m.end();++it){
            if(it->first%2){
                LL t1 = it->second;
                int t2 = (it->first)/2;
                while(t1>0&&pop[lc-1]<=t1){
                    if(pop[lc-1]==0){
                        lc--;
                        continue;
                    }
                    t1-=pop[lc-1];
                    res1 = res1+calc(t2-start[lc-1],pop[lc-1]);
                    res1%=MD;
                    lc--;
                }
                if(lc>0&&t1){
                    res1 = res1+calc(t2-start[lc-1],t1);
                    res1%=MD;
                    pop[lc-1]-=t1;
                }

            }   
            else{
                start[lc] = (it->first)/2;
                pop[lc] = it->second;
                ++lc;
            } 
        }       
        LL t3 = (res-res1+MD)%MD;
        cout<<"Case #"<<cs<<": "<<t3<<endl;
    }
    return 0;
}

