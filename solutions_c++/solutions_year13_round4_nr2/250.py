#include<cstdio>
#include<ctime>
#include<cmath>
#include<cctype>
#include<iomanip>
#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<set>
#include<algorithm>
#include<utility>
#include<stack>
#include<queue>
using namespace std;
#define pb push_back
#define mp make_pair
#define FILEIN "B.in"
#define FILEOUT "B.txt"
int main(){
    freopen(FILEIN,"r",stdin);
    freopen(FILEOUT,"w",stdout);
    int t;
    cin>>t;
    for(int u=1;u<=t;++u){
        int N;
        long long P;
        cin>>N>>P;
        int A[N];
        long long t=P-1;
        for(int i=N-1;i>=0;--i){
            A[i]=t%2;
            t/=2;
        }
        //for(int i=0;i<N;++i)
            //cout<<A[i]<<" ";
        //cout<<endl;
        cout<<"Case #"<<u<<": ";
        if(P==1ll<<N)
        {
            cout<<(P-1)<<" "<<(P-1)<<endl;
        }
        else{
            long long res=0;
            bool b=false;
            for(int i=0;i<N;++i){
                if(A[i]==0){
                    cout<<res<<" ";
                    b=true;
                    break;

                }
                res=2*res+2;

            }
            if(!b) cout<<(P-1)<<" ";
            if(P==1) cout<<0<<endl;
            else{
            int numofw=0;
            for(int i=0;i<N;++i){
                if(A[i]==0)
                    numofw++;
                else{
                    bool f = false;
                    for(int j=i+1;j<N;++j){
                        if(A[j]==0)
                        {
                            f=true;
                            numofw++;
                            break;
                        }
                    }
                    break;
                }
            }
            //cout<<numofw<<" ";
            if(numofw==N)
                cout<<0<<endl;
            long long r=0;
            for(int i=N-1;i>=numofw;--i){
                r+=(1ll)<<i;
            }
            cout<<r<<endl;
            }
        }

    }
    return 0;
}
