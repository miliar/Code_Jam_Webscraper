#include<bits/stdc++.h>
#define MAX 10000
#define pb push_back
#define mp make_pair
#define fi first
#define sc second
#define ellapse printf("Time : %0.3lf\n",clock()*1.0/CLOCKS_PER_SEC);
using namespace std;
typedef long long l64d;
typedef unsigned long int ud;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
const l64d inf=10000000;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("stand-large.txt","w",stdout);
    int T,n,cnt,p;
    string s;
    cin>>T;
    for(int i=1;i<=T;i++)
    {
        cin>>n>>s;
        cnt=0;
        p=0;
        for(int j=0;j<s.size();j++)
        {
            if(p<j)
            {
                cnt+=j-p;
                p=j;
                p+=s[j]-'0';
            }
            else
            {
                p+=s[j]-'0';
            }
        }
        printf("Case #%d: %d\n",i,cnt);

    }
}
