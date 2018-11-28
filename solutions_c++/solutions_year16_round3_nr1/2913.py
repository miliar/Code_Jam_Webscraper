// By: @shariquemohd

#include<iostream>
#include<cstdio>
#include<algorithm>
#include<string.h>
#include<vector>
#include<utility>

//-----------------

#define ull unsigned long long int
#define lli long long int
#define li long int
#define ft first
#define sc second
#define pb push_back
#define mp make_pair
#define pii pair<int,int>
#define pip pair<int,pii>

template <typename T>T power(T e, T n, T m){T x=1,p=e;while(n){if(n&1)x=mod(x*p,m);p=mod(p*p,m);n>>=1;}return x;}
template <typename T> T InverseEuler(T a, T m){return (a==1? 1:power(a, m-2, m));}
template <typename T> T gcd(T a, T b){return __gcd(a,b);}
template <typename T> T lcm(T a, T b){return (a*(b/gcd(a,b)));}

//-------------------

using namespace std;

const int MAX=1005;
int cnt[26];
int A[26];

vector< pii > P;


int main(){

    freopen("A-small-attempt0.in","r",stdin);
    freopen("A.out","w",stdout);

    int N,T,i,j;
    cin>>T;
    int num1,num2;
    for(int z=1;z<=T;z++){
        cin>>N;
        P.clear();
        for(i=0;i<N;i++){
            int tmp;
            cin>>tmp;
            P.pb(mp(tmp,i));
        }

        i=N-1;j=0;
        int res1=-1,res2=-1;
        //int cnt=0;

        cout<<"Case #"<<z<<": ";
        while(i>=0 && P[i].ft!=0){
            //cnt+=1;
            if(res1==-1)
                sort(P.begin(),P.end());
            if(i>=0 && P[i].ft==P[i-1].ft && res1==-1){
                res1=i,res2=i-1;
                i-=2;
            }
            else if(i>=0 && P[i].ft!=0){
                    P[i].ft-=1;
                    cout<<char('A'+P[i].sc)<<" ";
            }
        }

        while(P[res1].ft!=0){
            cout<<(char)('A'+P[res1].sc)<<(char)('A'+P[res2].sc)<<" ";
            P[res1].ft-=1; P[res2].ft-=1;
        }

        cout<<"\n";

    }
    return 0;
}
