#include<bits/stdc++.h>
using namespace std;
string s;
int main()
{
    freopen("B-large.in","rb",stdin);
    freopen("B-large.out","wb",stdout);
    int t,ct=0;
    cin>>t;


    while(t--){

        cin>>s;
        int n=s.size();
        int ans=0;
        for(int i=0;i<n-1;i++){
            if(s[i]!=s[i+1])ans++;
        }
        if(s[n-1]=='-')ans++;
        printf("Case #%d: %d\n",++ct,ans);

    }
}
