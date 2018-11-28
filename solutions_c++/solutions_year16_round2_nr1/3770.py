#include <stdio.h>
#include <string.h>

int main (void)
{
    int t;
    scanf ("%d",&t);
    int i;
    for (i=0;i<t;++i)
    {
        char a[2000];
        scanf ("%s",a);
        int l=strlen(a),x;
        int b['z'-'a'+1]={0};
        for (x=0;x<=l;++x)
        b[a[x]-'A']++;
        //check
       // for (x=0;x<='z'-'a';++x)
         //   printf("%d ",b[x]);
        int c[11];
        c[2]=b['w'-'a'];
        //printf("two:\n%d \n",c[2]);
        b['t'-'a']-=c[2];
        b['w'-'a']-=c[2];
        b['o'-'a']-=c[2];

        c[4]=b['u'-'a'];
       // printf("four:\n%d \n",c[4]);
        b['f'-'a']-=c[4];
        b['o'-'a']-=c[4];
        b['u'-'a']-=c[4];
        b['r'-'a']-=c[4];
        c[6]=b['x'-'a'];
       // printf("six:\n%d \n",c[6]);
        b['s'-'a']-=c[6];
        b['i'-'a']-=c[6];
        b['x'-'a']-=c[6];
        c[0]=b['z'-'a'];
       // printf("zero:\n%d \n",c[0]);
        b['z'-'a']-=c[0];
        b['e'-'a']-=c[0];
        b['r'-'a']-=c[0];
        b['o'-'a']-=c[0];
        c[8]=b['g'-'a'];
       // printf("eight:\n%d \n",c[8]);
        b['e'-'a']-=c[8];
        b['i'-'a']-=c[8];
        b['g'-'a']-=c[8];
        b['h'-'a']-=c[8];
        b['t'-'a']-=c[8];
        c[3]=b['h'-'a'];
       // printf("three:\n%d \n",c[3]);
        b['t'-'a']-=c[3];
        b['h'-'a']-=c[3];
        b['r'-'a']-=c[3];
        b['e'-'a']-=c[3];
        b['e'-'a']-=c[3];
        c[5]=b['f'-'a'];
       // printf("five:\n%d \n",c[5]);
        b['f'-'a']-=c[5];
        b['i'-'a']-=c[5];
        b['v'-'a']-=c[5];
        b['e'-'a']-=c[5];
        c[1]=b['o'-'a'];
       // printf("one:\n%d \n",c[1]);
        b['o'-'a']-=c[1];
        b['n'-'a']-=c[1];
        b['e'-'a']-=c[1];
        c[10]=b['t'-'a'];
       // printf("ten:\n%d \n",c[10]);
        b['t'-'a']-=c[10];
        b['e'-'a']-=c[10];
        b['n'-'a']-=c[10];
        c[7]=b['s'-'a'];
        //printf("seven:\n%d \n",c[7]);
        b['s'-'a']-=c[7];
        b['e'-'a']-=c[7];
        b['v'-'a']-=c[7];
        b['e'-'a']-=c[7];
        b['n'-'a']-=c[7];
        c[9]=b['n'-'a'];
        //printf("nine:\n%d \n",c[9]);
        int y[1000],p=0;
        for (x=0;x<1000;++x)
        y[x]=-1;
        for (x=0;x<11;++x)
        {
            int r=c[x],l=0;
            if(r>0)
            {
            while (l!=r)
            {
                y[p]=x;
                //printf("X:%d",x);
                //printf("y[%d]:%d\n",p,y[p]);
                p++;
                l++;
            }
            }


        }
        printf("Case #%d: ",i+1);
        for (l=0;l<1000;++l)
        {
            if (y[l]>=0)
            printf("%d",y[l]);
        }
        printf("\n");
    }
    return 0;
}
