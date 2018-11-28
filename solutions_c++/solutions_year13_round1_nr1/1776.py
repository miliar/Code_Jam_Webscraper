#include<stdio.h>

int main()
{
    
    FILE *fp=fopen("input.txt","r");
    FILE *f2=fopen("output.txt","w");
    long long int t,r,T,x=1;
    fscanf(fp,"%lld",&T);
        
    while(T--)
    {
              fscanf(fp,"%lld %lld",&r,&t);
              long long int temp=0,cnt=0;
              temp=2*r+1;
              while(t>=temp)
              {
                        t-=temp;
                        temp+=4;
                        cnt++;
              }
              fprintf(f2,"Case #%lld:%lld\n",x,cnt);x++;
    }
    return 0;
    
}
