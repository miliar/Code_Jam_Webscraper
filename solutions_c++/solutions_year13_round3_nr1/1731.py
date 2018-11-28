#include<stdio.h>
#include<string.h>
#include<math.h>
#include<string>
#include<vector>
#include<map>
#include<algorithm>
#include<iostream>
#include<queue>
#include<set>
using namespace std;
#define PI 2 * acos (0.0)

int cnt(string s)
{
    int x=0,c;
    for(int i=0;i<s.size();i++)
    {
        c=0;
        for(int j=i;j<s.size();j++)
        {

            if(s[j]!='a' && s[j]!='e' && s[j]!='i' && s[j]!='o' && s[j]!='u' )
            c++;
            else
                break;
        }
        x=max(x,c);
    }
    return x;
}
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    string s;
    int tc,t=1,i,j,n,c;
    scanf("%d",&tc);
    while(tc--)
    {
        cin>>s>>n;
        c=0;
        for(i=0;i<s.size();i++)
        {
            for(j=1;i+j<=s.size();j++)
            {

                //cout<<s.substr(i,j+1)<<endl;
                if(cnt(s.substr(i,j))>=n)
                {
                    //cout<<s.substr(i,j)<<endl;
                    c++;
                }
            }
        }
        printf("Case #%d: %d\n",t++,c);
    }
    return 0;
}
