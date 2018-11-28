#include<bits/stdc++.h>
using namespace std;
char shy[1010];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("MajicTric1.txt","w",stdout);
    long int t,s,required,current_total,ans,k=1;
    scanf("%d",&t);
    while(t--)
    {
        ans=current_total=0,required=0;
        scanf("%d",&s);
        scanf("%s",shy);
        for(int i=0;i<s+1;i++)
        {
            if(i==0)
            {
                current_total=shy[0]-'0';
                continue;
            }
            if(current_total>=i)
            {
                required=0;
            }
            else
            {
                required=i-current_total;
                ans+=required;
            }
            current_total+=(required+shy[i]-'0');
        }
        printf("Case #%ld: %d\n",k,ans);
        k++;
    }
}
