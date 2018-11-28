#include <bits/stdc++.h>
using namespace std;
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int test=1;test<=t;test++){
        string s;
        cin >> s;
        int n=s.length();
        int addend=(s[0]=='+'?0:-1);
        int groups=0;
        if(addend==-1) groups++;
        for(int i=1;i<n;i++)
            if(s[i]=='-'&&s[i]!=s[i-1]) groups++;
        int ans=2*groups+addend;
        cout << "Case #" << test << ": " << ans << endl;
    }
    return 0;
}
