#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<queue>
#include<stack>
#include<vector>
#include<iostream>
#include<algorithm>
using namespace std;
char a[1000100];
int main()
{
    int t;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.txt","w",stdout);

    while(cin>>t)
    {
        int n;
        for(int i=1;i<=t;i++)
        {
            cin>>a>>n;
            int ans=0;
            int l=strlen(a);
            for(int j=l;j>=n;j--)
            {
                for(int k=0;k+j-1<l;k++)
                {
                    int sum=0;
                    bool flag=false;
                    for(int x=k;x<j+k;x++)
                    {
                        if(a[x]=='a'||a[x]=='e'||a[x]=='i'||a[x]=='o'||a[x]=='u')
                        {
                            if(sum>=n)
                            {
                                ans++;
                                flag=true;
                                break;
                            }
                            sum=0;
                        }
                        else
                        {
                            sum++;
                        }
                    }
                    if(flag)
                    {
                        continue;
                    }
                    if(sum>=n)
                    {
                        ans++;
                    }
                }
            }
            cout<<"Case #"<<i<<": "<<ans<<endl;
        }
    }
    return 0;
}
/*

4
quartz 3
straight 3
gcj 2
tsetse 2
*/
