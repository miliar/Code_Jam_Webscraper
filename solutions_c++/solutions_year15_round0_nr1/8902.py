#include<bits/stdc++.h>

#define FASTIO ios_base::sync_with_stdio(0);cin.tie(0);
#define TESTCASE freopen("A-large.in","r",stdin);
#define FILEWRITE freopen("out.txt","w",stdout);

using namespace std;

int a[2000];

int main()
{
    FASTIO
    TESTCASE
    FILEWRITE
    int N,maxs;
    string str;
    cin>>N;
    for(int p=1;p<=N;p++){
        cin>>maxs;
        cin>>str;
        for(int i=0;i<=maxs;i++)a[i] = str[i]-'0';
        int ans;
        for(ans=0;ans<=maxs;ans++){
            int tot = ans + a[0];
            bool ok=true;
            for(int j=1;j<=maxs;j++){
                if( tot >= j )tot+=a[j];
                else {
                    ok=false;
                    break;
                }
            }
            if( ok == false )continue;
            printf("Case #%d: %d\n",p,ans);
            break;
        }
    }
    return 0;
}
