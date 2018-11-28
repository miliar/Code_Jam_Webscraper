#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef pair<int,int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;

const int  MOD=1000000007;
const int  INF= int(1e9);
const int  N=100005;
int n,standing,res;

int main()
{
	ios_base::sync_with_stdio(false);
    int testCases;
    cin>>testCases;
    for(int k=1;k<=testCases;k++) {
        string s;
        res=0;
        cin>>n>>s;
        standing=s[0]-'0';
        for(int i=1;i<=n;i++) {
            if(s[i]=='0'){
                continue;
            }
            if(standing < i ) {
                res+=(i-standing);
                standing+=(i-standing+s[i]-'0');
            } else {
                standing+=s[i]-'0';
            }
         //   cout<<i<<" "<<standing<<" "<<res<<endl;
        }
        cout<<"Case #"<<k<<": "<<res<<endl;
    }




	return 0;

}
