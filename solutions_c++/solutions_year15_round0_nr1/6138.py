#include<iostream>
#include<cstdio>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("result.out","w",stdout);
    int T, n, people, added;
    string shy;
    cin>>T;
    for(int k=1; k<=T; k++)
    {
         cin>>n>>shy;
         people = added = 0;
         people += (int)(shy[0] - '0');

         for(int i = 1; i <= n; i++)
         {
             int level = (int)(shy[i] - '0');
             if(people < i and level)
             {
                 added +=  i - people;
                 people += i - people;
             }
             people +=level;
         }
         cout<<"Case #"<<k<<": "<<added<<endl;
    }
    return 0;
}
