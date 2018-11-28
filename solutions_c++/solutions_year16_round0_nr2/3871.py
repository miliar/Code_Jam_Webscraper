//solution by Wsl_F
#include <bits/stdc++.h>

using namespace std;
#pragma comment(linker, "/STACK:1024000000,1024000000")


typedef long long LL;
typedef unsigned long long uLL;
typedef double dbl;
typedef vector<int> vi;
typedef vector<LL> vL;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef pair<LL,LL> pLL;

#define mp(x,y)  make_pair((x),(y))
#define pb(x)  push_back(x)
#define sqr(x) ((x)*(x))

int solve(string s)
{
//    cout<<"solve("<<s<<")"<<endl;
    if (s.length()==0) return 0;
    if (s.length()==1)
    {
        if (s[0]=='+') return 0;
        else return 1;
    }

    int l= s.length()-1;
    while (l>=0 && s[l]=='+') l--;
    if (l<0) return 0;

    string s2= "";
    for (int i= l; i>=0; i--)
        s2+= s[i] == '+' ? '-' : '+';

    if (s2[l]=='+')
        return 1 + solve(s2);

    while (l>=0 && s2[l]=='-') l--;
    return 2 + solve(s2.substr(0,l+1));
}

void solve()
{
 string s;
 cin>>s;
 cout<<solve(s)<<endl;
}

int main()
{
 ios_base::sync_with_stdio(0);
 cin.tie(0);
 srand(__rdtsc());
 // LL a[110];
 // memset(a,0,sizeof(a));

 freopen("B-large.in","r",stdin);
 freopen("output.txt","w",stdout);
 //cout<<fixed;
 //cout<<setprecision(9);

 int T;
 cin>>T;
 for (int testCase= 1; testCase <= T; testCase++)
 {
     cout<<"Case #"<<testCase<<": ";
     solve();
 }


 return 0;
}
