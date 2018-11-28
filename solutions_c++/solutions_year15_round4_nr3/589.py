#include <bits/stdc++.h> //includes everything.
#define pb push_back
#define mp make_pair
#define fs first
#define sc second
using namespace std;

int N,x;
int ind = 0;
int T = 0;
vector<int> v[100];
vector<string> allv,vx[1010];
int nrc[1010];
int nrl[1010],M;
int en[1010];
int startret=0;
unordered_map<int,int> h,hx,ah,hr,bh;
map<string,int> hv;
int rez = 100;
inline void calc(int x){
    unordered_set<int> S;
    h.clear();
    for(int i=0;i<N-2;++i){
        if((1<<i) & x){
            en[i+2]=1;
        } else en[i+2]=0;
    }
    for(int i=2;i<N;++i){
       if(en[i]){
        for(auto x:v[i]){
                if(hr[x]){
                    continue;
                }
                h[x]=1;
                if(bh[x]){
                    S.insert(x);
                }
            }
        }
    }
    //printf("\n");
    int ret = 0;
    for(int i=2;i<N;++i){
       if(en[i]==0){
        for(auto x:v[i]){
               if(hr[x]){
                    continue;
                }
               if((ah[x] || h[x])){
                S.insert(x);
               }
            }
        }
    }
    //printf("!!!%d!!!\n",ret);
    rez = min((int)S.size()+startret,rez);

}

int main(){
    freopen("test.in","r",stdin);
    freopen("out.out","w",stdout);
    scanf("%d\n",&T);
    int st = 1,dr=25;
    while(T--){
        ah.clear();
        hr.clear();
        bh.clear();
        allv.clear();
        hv.clear();
        startret=0;
        rez=1000;
        ++ind;
        scanf("%d\n",&N);
        for(int i=0;i<100;++i){
            v[i].clear();
            vx[i].clear();
        }
        for(int i=0;i<N;++i){
            string x;
            while ((cin.peek()!='\n') && (cin>>x)){
                vx[i].pb(x);
                allv.pb(x);
            }
            scanf("\n");
        }
        if(ind < st || ind > dr){
            continue;
        }
        sort(allv.begin(),allv.end());
        allv.erase( unique( allv.begin(), allv.end() ), allv.end() );
        for(int i=0;i<allv.size();++i){
            hv[allv[i]]=i+1;
        }
        for(int i=0;i<N;++i){
            for(int j=0;j<vx[i].size();++j){
                //printf("%d",hv[vx[i][j]]);
                v[i].pb(hv[vx[i][j]]);
                if(i==0){
                    ah[hv[vx[i][j]]]=1;
                }
                if(i==1){
                    if(ah[hv[vx[i][j]]] && hr[hv[vx[i][j]]]==0){
                        hr[hv[vx[i][j]]]=1;
                        ++startret;
                    }
                    bh[hv[vx[i][j]]]=1;
                }
            }
            sort(v[i].begin(),v[i].end());
            v[i].erase( unique( v[i].begin(), v[i].end() ), v[i].end() );
        }
        en[0]=1;
        en[1]=0;
        int num = (1<<(N-2));
        //printf("%d\n",num);
        for(int i=0;i<num;++i){
            calc(i);
        }
        printf("Case #%d: %d\n",ind,rez);

    }
    cout<<endl;


}
