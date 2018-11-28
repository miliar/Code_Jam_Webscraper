#include <stdio.h>
using namespace std;

int main() 
{
    long long int tc,copy,i,t,j,n,k;
    scanf("%lld",&tc);k=1;
    while(tc--)
    {
        int a[11]={0};
        j=1;
        int flag=0;
        i=1;
        scanf("%lld",&n);
        while((i<1000)&&(flag!=1)&&(n!=0))
        {
            t=j*n;
            copy=t;
            while(t!=0)
            {
                a[t%10]=1;
                t=t/10;
            }
            if((a[0]==1)&&(a[1]==1)&&(a[2]==1)&&(a[3]==1)&&(a[4]==1)&&(a[5]==1)&&(a[6]==1)&&(a[7]==1)&&(a[8]==1)&&(a[9]==1))
            {
                flag=1;
                printf("Case #%lld: %lld\n",k,copy);
            }
            else
            j++;
            i++;
        }
        if(flag==0)
        printf("Case #%lld: INSOMNIA\n",k);
        k++;
    }
	return 0;
}
