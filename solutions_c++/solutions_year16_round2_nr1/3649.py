// #CodeLikeTheMartian
#include <bits/stdc++.h>

#define     MOD       1000000007
#define     mp(a,b)   make_pair(a,b)
#define     pb        push_back
#define     lb        lower_bound
#define     ub        upper_bound
#define     SIZE      1000001
#define     MAX       INT_MAX
#define     fi        first
#define     se        second
#define     fastInput ios::sync_with_stdio(false); cin.tie(0);
using namespace std;

typedef long long int  ll;
typedef long double ld;
typedef unsigned int uint;
typedef unsigned long long int ull;
string arr[10]={"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
char e[5]={'Z','W','U','X','G'};
char o[5]={'O','T','F','S','N'};

/*
Z->0
W->2
U->4
X->6
G->8

O->1
T->3
F->5
S->7
N->9
*/
int main()
{
    int T;
    cin>>T;
    for(int t=1;t<=T;++t)
    {

        vector<int> ans;
        string s;
        cin>>s;
        int cnt[26]={0};
        for(int i=0;i<s.length();++i)
            cnt[s[i]-65]++;
        for(int i=0;i<5;i++)
        {
            for(;cnt[e[i]-65]>0;){
                    for(int j=0;j<arr[2*i].length();++j)
                        --cnt[arr[2*i][j]-65];
                    ans.pb(2*i);}
        }

        for(int i=0;i<5;i++)
        {
            for(;cnt[o[i]-65]>0;){
                    for(int j=0;j<arr[2*i+1].length();++j)
                        --cnt[arr[2*i+1][j]-65];
                    ans.pb(2*i+1);}
        }

        /*
        for(int i=0;i<10;++i)
        {
            bool y=true;
            while(y)
            {
            for(int j=0;j<arr[i].length();++j)
            {
                if(cnt[arr[i][j]-65]<=0)
                {y=false;}
                --cnt[arr[i][j]-65];
            }
            if(y)
            {
                ans.pb(i);
            }
            else{

                for(int j=0;j<arr[i].length();++j)
                {
                    ++cnt[arr[i][j]-65];
                }
            }
        }
    }
    */
    sort(ans.begin(),ans.end());
    cout<<"Case #"<<t<<": ";
        for(int i=0;i<ans.size();++i)cout<<ans[i];
        cout<<endl;
    }
	return 0;
}
