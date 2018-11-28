#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
    FILE *fp,*op;
    fp=fopen("D-small-attempt1.in","r");
    op=fopen("output.txt","w");
    int t,n,r,c,p;
    fscanf(fp,"%d",&t);
    p=1;
    while(t--)
    {
        fscanf(fp,"%d %d %d",&n,&c,&r);
        if(n==1)
        {
            fprintf(op,"Case #%d: GABRIEL\n",p);

        }
        else if(n==2)
        {
            if(r%2==0||c%2==0)
                fprintf(op,"Case #%d: GABRIEL\n",p);
            else
               fprintf(op,"Case #%d: RICHARD\n",p);
        }
        else if(n==3)
        {
            if((r%3==0&&c>=2)||(c%3==0&&r>=2))
                 fprintf(op,"Case #%d: GABRIEL\n",p);
            else
                 fprintf(op,"Case #%d: RICHARD\n",p);
        }
        else
        {
            if(c>2&&r==4||r>2&&c==4)
                fprintf(op,"Case #%d: GABRIEL\n",p);
            else
               fprintf(op,"Case #%d: RICHARD\n",p);
        }
        p++;
    }
}
