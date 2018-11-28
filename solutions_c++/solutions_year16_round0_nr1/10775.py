#include <stdio.h>

int main()
{
    int a[10],t,n,i,j,k,count,temp,num,factor;
    long long int ne;
    scanf("%d",&t);
    for(i=0;i<t;i++)
    {
        scanf("%d",&n);
        for(j=0;j<10;j++)
        {a[j]=0;}
        k=2;
        factor=1;
        count=0;
        ne=n;
        while(count<10 && n!=0)
        {
            num=ne;
            temp=num;
            while(temp)
            {
                temp=temp/10;
                factor=factor*10;
            }
            while(factor>1)
            {
                factor=factor/10;
                for(j=0;j<10;j++)
                {
                    if((num/factor)==j && a[j]==0)
                    {
                        a[j]=1;
                        count++;
                        break;
                    }
                }
                num=num%factor;
            }
            if(count<10)
            {
                ne=k*n;
                k++;
            }
        }
        if(n!=0)
        	printf("Case #%d: %d\n",i+1,ne);
        if(n==0)
        	printf("Case #%d: INSOMNIA\n",i+1);
    }
    return 0;
}
