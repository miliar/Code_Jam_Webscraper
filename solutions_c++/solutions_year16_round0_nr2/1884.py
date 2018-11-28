#include<bits/stdc++.h>
#define MAX 200
using namespace std;
int main()
{
    int t;
    freopen("input1.txt","r",stdin);
    freopen("output1.txt","w",stdout);
    scanf("%d",&t);
    for(int x1=1;x1<=t;x1++)
    {
        char s[MAX];
        scanf("%s",s);
        int n=strlen(s);
        int cnt=0;
       // int i=0;
        while(1)
        {
            int j;
            for(j=0;j<n;j++)
            {
                if(j==0)
                    continue;
                if(s[j]!=s[j-1])
                {
                    break;
                }
            }
            if(j==n)
            {
                //cout<<j<<" "<<cnt<<endl;
                if(s[j-1]=='-')
                    cnt+=1;
                break;
            }
            j-=1;
            //i=j;
            cnt++;
            for(int k=0;k<=j;k++)
            {
                if(s[k]=='+')
                    s[k]='-';
                else
                    s[k]='+';
            }
        }
        printf("Case #%d: %d\n",x1,cnt);
    }
    return 0;
}
