#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    int k=1;
    while(t--)
    {
        string s;
        cin>>s;
       reverse(s.begin(),s.end());
       int c=1;
       for(int i=1;i<s.size();i++)
       {
           if(s[i]!=s[i-1])
            c++;
       }
       if(s[0]=='+')
        c--;

       printf("Case #%d: %d\n",k,c);
       k++;
    }
}
