#include<cstdio>
#include<iostream>
using namespace std;
int main()
{
    int t,n,c;
    scanf("%d",&t);

    string str;
    c=0;
    while(t--)
    {
        c++;
        scanf("%d",&n);
        cin>>str;

        int curr=0;
        int ans=0;

        for(int i=0; i<str.size(); i++)
        {
            if(curr+ans>=i)
            {
                //ok;
                curr+=str[i]-48;
            }
            else
            {
                int diff=i-(curr+ans);
                ans+=diff;
                curr+=str[i]-48;
            }
        }
        printf("Case #%d: %d\n",c,ans);
    }
    return 0;
}
