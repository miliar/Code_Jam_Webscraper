#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
#define pb push_back
#define mp make_pair
#define MOD 1000000007
#define PI 3.1415926535897932
#define inf 10000000000000
char str[109];

int main()
{   
    int t,n,y;
    scanf("%d",&t);
    y=t;
    while(t--)
    {
        scanf("%s",str);
        n=strlen(str);
        int i,j;
        int count=0;
        while(1)
        {
            //rintf("%s\n",str);
            for(j=n-1;j>=0;j--)
            {
                if(str[j]=='-')
                break;
            }
            if(j==-1)
            break;
            if(str[0]=='+')
            {
                for(i=0;i<n;i++)
                {
                    if(str[i]=='+')
                    str[i]='-';
                    else
                    break;
                }
                count++;
                continue;
            }
            count++;
            for(i=0;i<=j;i++)
            {
                if(str[i]=='+')
                str[i]='-';
                else
                str[i]='+';
            }
            for(i=0;i<=j/2;i++)
            {
                char ch=str[j-i];
                str[j-i]=str[i];
                str[i]=ch;
            }
        }
        printf("Case #%d: %d\n",y-t,count);
    }
    return 0;
}