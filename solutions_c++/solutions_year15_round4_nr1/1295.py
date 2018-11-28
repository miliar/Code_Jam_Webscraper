#include<bits/stdc++.h>
#define ll long long
#define pn() printf("\n")
#define si(x) scanf("%lld",&x)
#define pi(x) printf("%d",x)
#define sll(x) scanf("%I64d",&x)
#define pll(x) printf("%I64d",x)
#define sc(x) scanf("%c",&x)
#define pc(x) printf("%c",x)
#define sf(x) scanf("%f",&x)
#define pf(x) printf("%f",x)
#define sd(x) scanf("%lf",&x)
#define pd(x) printf("%lf",x)
#define sld(x) scanf("%Lf",&x)
#define pld(x) printf("%Lf",x)
#define MOD 1000000007LL
using namespace std;
char a[101][101];
int r,c;
bool impossible(){
    int cntr[101],cntc[101];
    for(int i=0;i<101;i++){
        cntr[i]=cntc[i]=0;
    }
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            if(a[i][j]!='.'){
                cntr[i]++;
                cntc[j]++;
            }
        }
    }
    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            if(a[i][j]!='.'){
                if(cntr[i]==1&&cntc[j]==1){
                    return true;
                }
            }
        }
    }
    return false;
}
int main(void){
    ifstream f1("C:\\Users\\Shivam Goel\\Desktop\\input.txt");
    ofstream f2("C:\\Users\\Shivam Goel\\Desktop\\output.txt");
    int t,tt=1;
    f1>>t;
    while(t--){
        ll finalans=0;
        f1>>r>>c;
        for(int i=0;i<r;i++){
            f1>>a[i];
        }
        if(impossible()){
            f2<<"Case #"<<tt<<": "<<"IMPOSSIBLE"<<"\n";
            printf("Case #%d: IMPOSSIBLE\n",tt);
            tt++;
            continue;
        }
        for(int i=0;i<r;i++){
            bool found=false;
            for(int j=0;j<c&&!found;j++){
                if(a[i][j]!='.'){
                    found=true;
                    if(a[i][j]=='<'){
                        //cout<<"1";
                        finalans++;
                    }
                }
            }
        }
        for(int i=0;i<r;i++){
            bool found=false;
            for(int j=c-1;j>-1&&!found;j--){
                if(a[i][j]!='.'){
                    found=true;
                    if(a[i][j]=='>'){
                       // cout<<"2";
                        finalans++;
                    }
                }
            }
        }
        for(int i=0;i<c;i++){
            bool found=false;
            for(int j=0;j<r&&!found;j++){
                if(a[j][i]!='.'){
                    found=true;
                    if(a[j][i]=='^'){
                           // cout<<"3";
                        finalans++;
                    }
                }
            }
        }
        for(int i=0;i<c;i++){
            bool found=false;
            for(int j=r-1;j>=0&&!found;j--){
                if(a[j][i]!='.'){
                    found=true;
                    if(a[j][i]=='v'){
                          //  cout<<"4";
                        finalans++;
                    }
                }
            }
        }
        f2<<"Case #"<<tt<<": "<<finalans<<"\n";
        printf("Case #%d: %lld\n",tt,finalans);
        //cout<<winner<<endl;
        tt++;
    }
    return 0;
}
