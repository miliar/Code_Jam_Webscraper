#include<algorithm>
#include<stdio.h>
#include<iostream>
#include<string>
#include<string.h>
#include<stdlib.h>
#include<vector>
#include<stack>
#include<queue>
#include<list>
#include<bitset>
#include<map>
//Template V1
#define nl printf("\n")
#define in(x) scanf("%d",&x)
#define out(x) printf("%d",x)
#define inll(x) scanf("%lld",&x)
#define outll(x) printf("%lld",x)
#define inc(x) scanf("%c",&x)
#define outc(x) printf(x)
#define ins(x) scanf("%s",&x)
#define outs(x) printf("%s",x)
#define loop(var,x,y) for(int var=x;var<y;var++)
#define rloop(var,x,y) for(int var=x-1;var>=y;var--)
#define cins(x) cin>>x
#define couts(x) cout<<x
#define reset(x,y) memset(x,y,sizeof(x));
#define stop fflush(stdin);getchar()
#define PB push_back
#define GOD using
#define BLESS namespace
#define YOU std;
GOD BLESS YOU

typedef long long ll;
typedef vector<int> vi;


inline void OPEN(const string &s) {
freopen((s + ".in").c_str(), "r", stdin);
freopen((s + ".out").c_str(), "w", stdout);
}

bool rev(float x,float y){return x>y;}
int main(){

OPEN("DL");

int T;in(T);
int kasus=1;
while(T--){
int N;in(N);
vector<float> vf1,vf2;

for(int i=0;i<N;i++){float temp;scanf("%f",&temp);vf1.PB(temp);}
for(int i=0;i<N;i++){float temp;scanf("%f",&temp);vf2.PB(temp);}

sort(vf1.begin(),vf1.end());
sort(vf2.begin(),vf2.end());


vector<float> vfc1(vf1),vfc2(vf2);

int y=0,x=0;
while(!vf1.empty()){
                    float minn=1.0;
                    
                    float min=1.0;
                    int imin=-1;
                    float max=0.0;
                    int imax=-1;
                    
                    int idx=-1;
                    for(int i=0;i<vf2.size();i++){
                            vf2[i]>max?max=vf2[i],imax=i:max;
                            vf2[i]<min?vf2[i],imin=i:min;
                            
                            if(vf2[i]<minn&&vf2[i]>vf1[0]){
                               minn=vf2[i];
                               idx=i;
                            }
                    }
                    if(minn==1.0){
                                 y++;
                                 vf1.erase(vf1.begin());
                                 vf2.erase(vf2.begin()+imin);
                    }
                    else{
                         vf1.erase(vf1.begin());
                         vf2.erase(vf2.begin()+idx);                 
                    }
}
while(!vfc1.empty()){
                     if(vfc1[0]<vfc2[0]){
                       vfc1.erase(vfc1.begin());
                       vfc2.erase(vfc2.begin()+vfc2.size()-1);
                     }
                     else{
                          x++;
                          vfc1.erase(vfc1.begin());
                       vfc2.erase(vfc2.begin());
                     }
}

printf("Case #%d: %d %d\n",kasus++,x,y);

}

}
