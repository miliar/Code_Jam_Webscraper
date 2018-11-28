#include<bits/stdc++.h>

#define mod 1000000007
#define ll long long
#define F first
#define S second
#define maxs 100045
#define INF INT_MAX
#define dbg(x) cout<<#x<<"="<<x<<endl
#define sc scanf
#define pb push_back
#define pf push_front
#define mp make_pair
#define pii pair<int,int>
#define f(i,n) for(i=0;i<n;i++)
#define FOR(i,j,n) for(i=j;i<n;i++)

#define CASET int ___T, case_n = 1; scanf("%d ", &___T); while (___T-- > 0)

using namespace std;
list<char>v;
list<char>::iterator it;

int main(){
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    long long int i, j;
    CASET{
        string str;
        cin>>str;
        ll len=str.length();
        ll stt,cur;
        v.pb(str[0]);
        //start=0;
        char fl;
        fl = str[0];
        FOR(i,1,len)
        {
          //cur=i;
          if(str[i]>=fl)
           {
            v.pf(str[i]);
            fl = str[i];
            //cout<<str[i]<<" ";
          }
          else{
            v.pb(str[i]);
          }
        }

        cout<<"Case #"<<case_n<<": ";
        case_n++;
        for(it=v.begin();it!=v.end();it++)
        cout<<*it;
        cout<<endl;
        v.clear();
    }
}
