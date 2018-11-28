#include<bits/stdc++.h>

using namespace std;
typedef long long ll;

string s;
int b[1234];

int pan()
{
    for (int i=0;i<s.size();i++)
    if (s[i]=='-') return 0;

    return 1;
}
int main()
{
    int T;
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>T;
    for (int _=1;_<=T;_++){
         int ans=0;
         cin>>s;

         int n=s.size();

             for (int j=n-1;j>=0;j--)
             if (s[j]=='-')
             {
                 s[j]='+';
                 for (int k=j-1;k>=0;k--)
                 {
                     if (s[k]=='-') s[k]='+';
                     else s[k]='-';
                 }
                 ans++;
             }



         printf("Case #%d: %d\n",_,ans);
        }

    return 0;
}
