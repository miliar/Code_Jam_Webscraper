#include <iostream>
#include<algorithm>
#include<cstdio>
using namespace std;
#define ll  int
int main()
{
    ios_base::sync_with_stdio(0);
    cin.tie(0);
    ll i,j,t,mx,k,y,c;
    cin>>t;
    string s;
    for(i=1;i<=t;i++)
    {
        cin>>mx;
        cin>>s;
        c=s[0]-48;y=0;//cout<<c<<endl;
        for(j=1;j<mx+1;j++)
        {
           if(c<j)
           {
               if(s[j]-48)
               {
               y+=j-c;
               c=j+s[j]-48;
               // cout<<c<<" "<<y<<endl;
              // cout<<j<<" a"<<endl;
               }
           }
           else
            c+=s[j]-48;
           //y+=s[j]-48;

        }
      printf("Case #%d: %d\n",i,y);
    }



    return 0;
}
