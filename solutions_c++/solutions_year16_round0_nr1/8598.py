#include<bits/stdc++.h>
using namespace std;
bool check(int a[])
{
    int f=true;
    for(int i=0;i<10;i++)
        if(a[i]==0)
            f=false;
    return f;
}


int main()
{
    FILE *fr , *fw;
    fr=fopen("in.txt","a+");
    fw=fopen("out.txt","w+");
    int t,n;
    fscanf(fr,"%d",&t);
    for(int k=1;k<=t;k++)
    {
        fscanf(fr,"%d",&n);
        int a[10]={0,0,0,0,0,0,0,0,0,0};
        if(n==0)
            fprintf(fw,"Case #%d: INSOMNIA\n",k);
        else
        {
            int i;
            for(i=1;1;i++)
            {
                if(check(a))
                    break;
                else
                {
                    int m=i*n;
                    while(m>0)
                    {
                        a[m%10]++;
                        m/=10;
                    }
                }
            }

           fprintf(fw,"Case #%d: %d\n",k,(i-1)*n);
        }
    }
    fclose(fw);
    fclose(fr);
    return 0;
}
