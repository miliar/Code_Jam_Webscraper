#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<vector>
#include<set>
#include<map>
#include<algorithm>
#include<cmath>
#include<cstring>
#include<string>
#include<queue>
#include<stack>
#include<cctype>
using namespace std;

typedef long double ld;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef map<int,int> mii;
typedef vector<int> vi;
typedef vector< vector<int> > vvi;
typedef vector<char> vc;
typedef vector<bool> vb;
typedef vector<string> vs;

#define rep(i,n) for(int i=0;i<n;i++)
#define forup(i,a,b) for(int i=a;i<=b;i++)
#define fordn(i,a,b) for(int i=a;i>=b;i--)
#define all(x) x.begin(),x.end()
#define permute(x) next_permutation(all(x))
#define pb push_back

#define debug if(printf("JJ "))

int main(){
    int t;
    ld C,F,X;
    scanf("%d",&t);
    forup(z,1,t){
        scanf("%LF %LF %LF",&C,&F,&X);
        ld R = 2.0;
        ld ans = X/R;
        ld tim = 0;
        while(1){
            tim += C/R;
            R+=F;
            ld local = tim + X/R;
            //cout<<tim<<" "<<X/R<<endl;
            //cout<<"J "<<local<<endl;
            if(ans <= local)break;
            else ans = local;
        }
        printf("Case #%d: %.7LF\n",z,ans);
    }
}
