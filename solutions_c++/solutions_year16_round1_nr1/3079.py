/*coder:abhi2110*/
#include <bits/stdc++.h>
using namespace std;
#define TC int tc; scanf("%d",&tc); while(tc--)
#define sii(i,j) scanf("%d%d",&i,&j)
#define si(i) scanf("%d",&i)
#define sl(i) scanf("%lld",&i)
#define ss(i) scanf("%s",i)
#define m0(a) memset(a,0,sizeof(a))
#define m1(a) memset(a,-1,sizeof(a))
#define pb push_back
#define mp make_pair
#define FILEIO(x) freopen(#x ".in","r",stdin);freopen(#x ".out","w",stdout);
#define FILEIOS freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef long long int ll;
int main(){
        FILEIOS
        int a=1;
        char S[1004];
        string t;
        TC{
            ss(S);
            int n=strlen(S);
            t="";
            t=t+S[0];
            char l=S[0],r=S[0];
            for(int i=1;i<n;i++){
                if(l>S[i]){
                    t+=S[i];
                    r=S[i];
                }
                else{
                    string y=S[i]+t;
                    t=y;
                    l=S[i];
                }
            }
            printf("Case #%d: %s\n",a,t.c_str());
            a++;
        }
	return 0;
}
