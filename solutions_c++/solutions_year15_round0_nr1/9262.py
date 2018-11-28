#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    scanf("%d",&t);
    char s[10005];
    int k=t;
    while(t--)
    {
        int smax;
        scanf("%d",&smax);
        scanf("%s",s);
        int len=strlen(s),c=0,sum=0,z=0;
        for(int i=0;i<len;i++)
        {
            if(sum<i)
            {
                z=i-sum;
                c+=z;
                sum+=z;
            }
            //cout<<sum<<endl;
            sum+=s[i]-'0';
        }
        printf("Case #%d: %d\n",k-t,c);
    }
    return 0;
}
