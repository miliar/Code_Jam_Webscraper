#include<stdio.h>
#include<math.h>

int check_pali(int num)
{
    int n,rev,dig;
    n=num;
    rev=0;
    while(num>0)
    {
        dig=num%10;
        rev=rev*10+dig;
        num=num/10;
    }
    if(n==rev) return 1;
    else return 0;
}

int main()
{
    int T,A,B,cases=1,i,j;
    int count,root,pali;
    freopen("C-small-attempt0.in","r",stdin);
    freopen("sub-1.out","w",stdout);
    scanf("%d",&T);
    while(T--)
    {
        count=0;
        scanf("%d %d",&A,&B);
        for(i=A;i<=B;i++)
        {
            root=sqrt(i);
            if(root*root!=i) continue;
  //          printf("%d %d\n",i,root);
            pali=check_pali(i);
            if(pali==0) continue;
            pali=check_pali(root);
            count+=pali;
        }
        printf("Case #%d: %d\n",cases++,count);
    }
    return 0;
}
