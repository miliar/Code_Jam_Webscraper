#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;

int main()
{
    int t,x=1;
    scanf("%i",&t);
    while(t--)
    {
        int n,j,b[16],f,div[9];
        long long int c;
        scanf("%i%i",&n,&j);
        printf("Case #%i:\n",x);
        b[0]=b[15]=1;
        for(int i=1;i<15;i++)
        {
            b[i]=0;
        }
        for(int i=0;i<9;i++)
        {
            div[i]=0;
        }
        while(j!=0)
        {
            for(int i=0;i<9;i++)
            {
                div[i]=0;
            }
            f=1;
            for(int i=2;i<=10;i++)
            {
                c=0;
                for(int k=0;k<16;k++)
                {
                    c+=b[k]*pow(i,k);
                }
                int srt=sqrt(c)+1;
                for(int k=2;k<srt;k++)
                {
                    if(c%k==0)
                        div[i-2]=k;
                }
                if(div[i-2]!=0)
                {
                    f=0;
                    break;
                }
            }
            if(f==1)
            {
                for(int i=0;i<16;i++)
                {
                    printf("%i",b[i]);
                }
                for(int i=0;i<9;i++)
                {
                    printf(" %i",div[i]);
                }
                printf("\n");
                j--;
            }
            b[1]+=1;
            for(int i=1;i<15;i++)
            {
                b[i+1]+=b[i]/2;
                b[i]%=2;
            }
        }
        x++;
    }
	return 0;
}
