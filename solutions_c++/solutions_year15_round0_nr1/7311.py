#include<bits/stdc++.h>

using namespace std;



int main(){
    int T,cased=0;
    string s;
    int n,ans,stand,temp;
    freopen("a.txt","r",stdin);
    freopen("b.txt","w",stdout);
    cin>>T;
    while(T--)
    {
        cin>>n>>s;
        stand=ans=0;
        for(int i=0;i<=n;i++)
        {
            temp=i-stand;
            if(i>stand)ans+=i-stand;
            if(temp>0)stand+=temp;
            stand+=s[i]-'0';
        }

        printf("Case #%d: %d\n",++cased,ans);
    }

    return 0;
}
