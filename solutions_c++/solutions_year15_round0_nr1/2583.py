#include<cstdio>
#include<iostream>
#include<map>
#include<set>
#include<stack>
#include<queue>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<cstring>

#define INF 2000000000
#define INF_LL 2000000000000000000ll
#define MOD_7 1000000007
#define MOD_9 1000000009

typedef long long ll;

using namespace std;

int main()
{
    int t,i;
    string s;
    
    ios::sync_with_stdio(false);
    
    freopen("A_in_large.txt","r",stdin);
    freopen("A_out_large.txt","w",stdout);
    cin>>t;
    int sv=t;
    
    while(t--)
    {
              int n,ans=0;
              
              cin>>n>>s;
              int tot=0;
              for(i=0;i<int(s.length());i++)
              {
                                            if(tot<i && s[i]>'0')
                                            {
                                                     ans+=i-tot;
                                                     tot=i;
                                            }
                                            tot+=s[i]-'0';
              }
              cout<<"Case #"<<sv-t<<": "<<ans<<endl;
              
              
              
    }
    //system("pause");
    return 0;
}
