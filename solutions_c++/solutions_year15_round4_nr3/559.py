#include <bits/stdc++.h>
#define MA(a,b) ((a)>(b)?(a):(b))
#define MI(a,b) ((a)<(b)?(a):(b))
#define AB(a) (-(a)<(a)?(a):-(a))
#define C first
#define R second
#define mp make_pair
#define pb push_back
#define pob pop_back
#define ep 0.00000005
#define ep22 0.000000005
using namespace std;
const int N=2000002;
int n;
int v[N];
int ms;

void input(){
    cin>>n;
    string s;
    map <string ,int> M;
    getline(cin,s);
    ms=0;

    for (int i=0;i<n;i++){
        getline(cin,s);
        string ss="";
        s+=" ";
        for (int j=0;j<s.size();j++)
        {
            if (s[j]==' ') {
                if (M[ss]==0) ms++,M[ss]=ms;
                v[M[ss]]|=(1<<i);
                ss="";
            } else ss+=s[j];
        }
    }
}

int sol(){
    int ans=10000000;

    for (int B=0;B<(1<<n);B++)
    if ((B&3)==2 || (B&3)==1  ){
        int k=0;
        for (int i=1;i<=ms;i++)
        k+=(((B&v[i])!=0) && ((B&v[i])!=v[i]));
        ans=min(ans,k);
    }
    for (int i=1;i<=ms;i++) v[i]=0;
    return ans;
}

int main() {
    freopen("C2.in","r",stdin);
    freopen("ans.txt","w",stdout);
    int testn=1;
    cin>>testn;
    for (int test=1;test<=testn;test++){
        input();
        printf("Case #%d: %d\n",test,sol());
    }

    return 0;
}
