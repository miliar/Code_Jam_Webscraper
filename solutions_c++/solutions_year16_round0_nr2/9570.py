#include <iostream>
#include <stdio.h>
#include <string.h>
#include <math.h>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#define lli long long int
#define pb push_back
#define mod 1000000007
#define pii pair<int,int>
using namespace std;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,count=0,i,j,ans;
    string s;
    cin>>t;
    for(j=1; j<=t; j++)
    {
        count=0;
        cin>>s;
        for(i=0; i<s.size(); i++)
        {
            if(s[i]=='+')
            {
                count++;
                while(s[i]=='+')
                {
                    i++;
                }
            }
        }
        if(s[s.size()-1]=='+')
            count-=1;
        if(s[0]=='+')
            ans=count*2;
        else if(s[0]=='-')
            ans=(count*2)+1;
        cout<<"Case #"<<j<<": "<<ans<<endl;
    }
    return 0;
}
