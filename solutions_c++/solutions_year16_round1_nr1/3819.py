#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("codejam1.out","w",stdout);
    int has[26];
    char ar[1010];
    char br[2020];
    int testcases;
    cin>>testcases;
    for(int f=1;f<=testcases;f++)
    {
        int flag=0;
        int top=1000,top1=999;
        int k;
        cin>>ar;
        printf("Case #%d: ",f);
        memset(has,0,sizeof(has));
        for(int i=0;i<strlen(ar);i++)
        {
            has[ar[i]-'A']++;
        }
        for(int i=0;i<26;i++)
        {
            if(has[i])
                k=i;
        }
        for(int i=0;i<strlen(ar);i++)
        {
            if(ar[i]==k+'A')
            {
                br[top1--]=ar[i];
                flag++;
            }
            else if(flag==0&&(ar[i]>=br[top1+1]))
            {
                br[top1--]=ar[i];
            }
            else
            {
                br[top++]=ar[i];
            }

        }
        for(int i=top1+1;i<top;i++)
        {
            printf("%c",br[i]);
        }
        cout<<endl;

    }

}
