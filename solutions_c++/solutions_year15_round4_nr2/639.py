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
unordered_map<int,int> h;
map<string,int> hv;
int rez = 100;
inline void calc(int x){

    h.clear();
    for(int i=0;i<N-2;++i){
        if((1<<i) & x){
            en[i+2]=1;
        } else en[i+2]=0;
    }
    for(int i=0;i<N;++i){
       if(en[i]){
        for(auto x:v[i]){
               // printf("@");
                h[x]=1;
            }
        }
    }
    //printf("\n");
    int ret = 0;
    for(int i=0;i<N;++i){
       if(en[i]==0){
        for(auto x:v[i]){
               // printf("@");
               if(h[x]){
                ++ret;
                h[x]=0;
               }
            }
        }
    }
    //printf("!!!%d!!!\n",ret);
    rez = min(ret,rez);

}
double R[1010],C[1010];
double V,X;
#define eps 0.0000001
double ret=0;
int main(){
    freopen("2.in","r",stdin);
    freopen("2.out","w",stdout);
    scanf("%d\n",&T);
    int st = 1,dr=8;
    while(T--){
        ++ind;
        cin>>N>>V>>X;
        for(int i=1;i<=N;++i){
            cin>>R[i]>>C[i];
        }
        if(N==1){
            if(C[1] == X){
                ret = V/R[1];
            }
            else ret = -1;
        }
        if(N==2){
            if(C[1] == C[2]){
                if(C[1] == X){
                    ret = V/(R[1]+R[2]);
                }
                else ret = -1;
            }
            else if(C[1] == X && C[2]!=X){
                ret = V/(R[1]);
            }
            else if(C[2] == X && C[1]!=X){
                ret = V/(R[2]);
            }
            else if(C[1] < X && C[2] < X){
                ret = -1;
            }
            else if(C[1] > X && C[2] > X){
                ret = -1;
            }
            else {
                double calcv1 = (X * V - C[2] * V) / (R[1]*C[1] - R[1]*C[2]);
                double calcv2 = (V - calcv1 * R[1]) / R[2];
                if(calcv1 < -eps || calcv2 < -eps){
                    ret = -1;
                }
                else ret = max(calcv1,calcv2);
            }
        }
        if(ret == -1){
            printf("Case #%d: IMPOSSIBLE\n",ind);
        } else {
            printf("Case #%d: %.8f\n",ind,ret);
        }
    }
    cout<<endl;


}
