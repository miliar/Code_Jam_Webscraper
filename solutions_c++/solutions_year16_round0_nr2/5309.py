#include<bits/stdc++.h>
#define rep(i, begin, end) for (__typeof(end) i = (begin) - ((begin) > (end)); i != (end) - ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))
#define pb push_back
using namespace std;
int solve()
{
    string s;
    cin >> s;
    int i;
    int cnt=0,ans=0;int cnt1=0;
    int n=s.size();
    if(n==1)
    {
     if(s[0]=='+')
        return 0;
     else
        return 1;
    }
    else
    {
        rep(i,0,n-1)
        {
            if(s[i]!=s[i+1])
                cnt++;
        }
    }
    if(s[n-1]=='-')
        cnt++;
    return cnt;
}



int main()  
{
    int t;
    cin >> t;
    int j;
    for(j=0;j<t;j++)
    {
         cout << "Case #" << j+1 << ": " << solve() << "\n";
    }
    return 0;
    
}