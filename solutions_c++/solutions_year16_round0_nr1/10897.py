#include<iostream>
#include<stdio.h>

using namespace std;

FILE *in,*out;

int main()
{
    in = fopen("YO.in","r");
    out = fopen("YO.out","w");
    int t;
    fscanf(in,"%d",&t);
    for(int I=0;I<t;++I)
    {
        int n,N;
        fscanf(in,"%d",&N);
        n = N;
        int i = 1;
        int v[10];
        bool vnow[10];
        for(int i=0;i<10;++i)
            v[i] = 0;
        int curr = 0;
        fprintf(out,"Case #%d: ",I+1);
        while(1)
        {
            int tmp = n;
            for(int i=0;i<10;++i)
                        vnow[i] = false;
            int i = 0 , j = 0;
            if(n == 0)
            {
                fprintf(out,"INSOMNIA\n");
                break;
            }
            else
            while(tmp)
            {
                if(!v[tmp%10])
                {
                    ++curr;
                }
                if(!vnow[tmp%10] && v[tmp%10])
                    ++i;
                if(!vnow[tmp%10])
                    ++j;
                vnow[tmp%10] = true;
                v[tmp%10] = true;
                tmp /= 10;
            }
            if(curr == 10)
            {
                fprintf(out,"%d\n",n);
                break;
            }
            else n += N;
        }
    }
    fclose(in);
    fclose(out);
    return 0;
}
