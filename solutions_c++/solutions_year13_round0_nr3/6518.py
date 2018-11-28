#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>

bool cek(int x)
{
    int y[100],z[100];int k=0,xx=0,l=0;
    bool a;
    while(x>0)
    {
        y[k]=x%10;
        //z[k]=x%10;
        x=x/10;
        k++;
    }
    //printf("%s\n",y);
    //printf("%s",zz);
    //strrev(z);
    //if(x<10)strrev(z);
    l=k-1;
    for(int aa=0;aa<k;aa++)
    {
        //printf("%i-%i ",y[aa],y[l]);
        if(y[aa]!=y[l]) 
        {
            xx=9;
            break;
        }
        else xx=0;
        l--;
    }
    //printf("%i\n",xx);
    if(xx==0)
    {
        a=true;
        //printf("Sukses  ");
        return a;
    }
    else 
    {
        a=false;
        return a;    
    }
    
}

int main()
{
    int testcase;
    scanf("%i",&testcase);
    //bool b=cek(testcase);
    //if(b) printf("SUKSES");
    for(int i=1;i<=testcase;i++)
    {
        unsigned long long int a,b,hasil=0;
        scanf("%lli %lli",&a,&b);
        int d=sqrt(a);
        int c=sqrt(b);
        for(int j=d;j<=c;j++)
        {
            bool b=cek(j);
            //printf("\n");
            if(b)
            {
                int k=j*j;
                b=cek(k);
                //printf("%i %i AA\n",j,k);
                if(b&&k>=a)
                {
                    //printf("%i ",j);
                    hasil++;    
                }
            } 
        }
        printf("Case #%i: %i\n",i,hasil);
    }
}
