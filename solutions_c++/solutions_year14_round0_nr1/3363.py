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
    int t,x,y,arr[4]; 
    bool save[17];
    scanf("%d",&t);
    forup(z,1,t){
        rep(i,17)save[i]=0;
        int cnt=0, ans=-1;
        scanf("%d",&x);
        rep(i,4)
        {
            rep(j,4)scanf("%d",&arr[j]);
            if(i==x-1)
                rep(j,4)save[arr[j]]=1;            
        }

        scanf("%d",&y);
        rep(i,4)
        {
            rep(j,4)scanf("%d",&arr[j]);
            if(i==y-1){
                rep(j,4){
                    if(save[arr[j]]){
                        cnt++;
                        ans = arr[j];
                    }
                }
            }
        }
        printf("Case #%d: ",z);
        if(cnt==0)
            puts("Volunteer cheated!");
        else if(cnt>1)
            puts("Bad magician!");
        else
            printf("%d\n",ans);
        
    }
}
