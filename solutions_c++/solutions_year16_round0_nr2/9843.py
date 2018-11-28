// Coder nyble
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
typedef vector<string> vs;

#define fi          first
#define se          second
#define all(x)      (x).begin(), (x).end()
#define ini(a, v)   memset(a, v, sizeof(a))
#define re(i,s,n)  	for(int i=s;i<(n);++i)
#define fr(i,n)     re(i,0,n)
#define tr(i,x)     for(__typeof(x.begin()) i=x.begin();i!=x.end();++i)
#define pu          push_back
#define mp          make_pair
#define sz(x)       (int)(x.size())
#define nl          printf("\n")

int main()
{
    int t;
    scanf("%d",&t);
    for(int z=1; z<=t; z++)
    {
        string p;
        cin>>p;
        int len = p.length(), lastMinus=-1,flips=0;
        for(int i=0; i<len;i++){
            if(p[i]=='-'){
                lastMinus = i;
            }
        }
        if(lastMinus==-1){
            printf("Case #%d: 0\n",z);
        }
        else{
            for(int i=0;i<=lastMinus ;i++){
                if(p[i]=='+'&&i+1<=lastMinus&&p[i+1]=='-'){
                    flips++;
                }
                else if(p[i]=='-'){
                    if(i==lastMinus){
                        flips++;
                    }
                    else if(p[i+1]=='+'){
                        flips++;
                    }
                }
            }
            printf("Case #%d: %d\n",z,flips);
        }
    }
    return 0;
}
