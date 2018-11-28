#include<bits/stdc++.h>
using namespace std;
#define  mp make_pair
#define  pb push_back
#define fi first
#define se second
#define inf 99999999LL
#define  M 1000000007
#define PI 3.1415926535897932
typedef long long int ll;
char ch[1004];
int mad=1;
int main()
{
    int i,j,t;
    scanf("%d",&t);
    while(t--)
    {
        scanf("%s",ch);
        int len=strlen(ch);
        int count=0;
        int start=1000;
        int minus=0;
        int en;
        char a[5000];
        for(i=0;i<len;i++)
        {
            if(count==0)
            {
                a[start]=ch[i];
                en=start;
            }
            else
            {
                if(ch[i]<a[start])
                {
                    a[++en]=ch[i];
                }
                else
                {
                    a[--start]=ch[i];
                    minus--;
                }
            }
            count++;
        }
        //printf("%d %d\n",start,en);
        printf("Case #%d: ",mad++);
        for(i=start;i<=en;i++)
        {
            printf("%c",a[i]);
        }
        cout<<endl;
    }       
    return 0;
}