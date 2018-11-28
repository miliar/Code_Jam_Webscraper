#include<bits/stdc++.h>

using namespace std;

string str;

int main()
{
//    freopen("a.txt","r",stdin);
//    freopen("b.txt","w",stdout);
    int T,cased=0;
    scanf("%d",&T);
    while(T--)
    {
        printf("Case #%d: ", ++cased);
        cin>>str;
        char prev = str[0];
        int ans = 0;
        for(int i=1;i<str.size();i++){
            ans += (str[i]!=prev);
            prev = str[i];
        }
        if(prev=='-') ans++;
        printf("%d\n",ans);
    }

    return 0;
}
