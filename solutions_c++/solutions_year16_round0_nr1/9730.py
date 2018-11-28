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
    for(int z=1;z<=t;z++)
    {
        int n, seen[10]={0,0,0,0,0,0,0,0,0,0},curr,temp;
        bool done =false;
        scanf("%d",&n);
        for(int i=1; i<10000; i++){
            curr = n*i;
            if(curr==n&&i>1){
                printf("Case #%d: INSOMNIA\n",z);
                break;
            }
            temp = curr;
            while(temp>0){
                seen[temp%10]++;
                temp/=10;
            }
            done = true;
            for(int j=0; j<10; j++){
                if(seen[j]==0){
                    done=false;
                }
                //cout<<seen[j];
            }
            if(done){
                printf("Case #%d: %d\n",z,curr);
                break;
            }
        }
    }
    return 0;
}
