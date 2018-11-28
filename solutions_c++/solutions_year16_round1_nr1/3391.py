#include<stdio.h>
int a[1005],an[1005];
void insb(int n, int d)
{
    int i;
    for(i=n;i>0;i--)
    {
        an[i]=an[i-1];
    }
    an[0]=d;
}
int main()
{
  // freopen("input2.in","r",stdin);
  // freopen("output4.txt","w",stdout);
    int t;
    scanf("%d",&t);
    char ch;
    int l=0;
    scanf("%c",&ch);
    while(l<t)
    {   l++;
        int k=0;
        ch=getchar();
        an[0]=ch-'A';
        k++;
        while((ch=getchar())!='\n')
        {
            int d=ch-'A';
            if(d>=an[0])
            {
                insb(k,d);
                k++;
            }
            else
            {
                an[k++]=d;
            }
        }
        int i;
        printf("Case #%d: ",l);
        for(i=0;i<k;i++)
        {
            ch=an[i]+'A';
            printf("%c",ch);
        }
        printf("\n");
    }
    return 0;
}
