#include <bits/stdc++.h>

using namespace std;

int n,m,a,b,s,i,j,ans;
char ch;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin >> n;
    n++;
    for(i=1;i<n;i++){
        cout << "Case #" << i << ": ";
        cin >> m;
        m++;
        cin >> ch;
        s=int(ch)-48;
        ans=0;
        for(j=1;j<m;j++){
            cin >> ch;
            a=int(ch)-48;
            ans+=max(j-s,0);
            s+=(a+max(j-s,0));
        }
        cout << ans << "\n";
    }
    return 0;
}
