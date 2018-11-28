#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{

    FILE *fp,*op;

    fp=fopen("D-small-attempt0.in","r");
    op=fopen("output.in","w");
    int a=1;
    int t;
    fscanf(fp,"%d",&t);
    while(t--)
    {
        int x,r,c;
        fscanf(fp,"%d %d %d",&x,&r,&c);
        if(x==1)
            fprintf(op,"Case #%d: GABRIEL\n",a);
        if(x==2)
        {
            if(r%2==0 || c%2==0)
                fprintf(op,"Case #%d: GABRIEL\n",a);
            else
                fprintf(op,"Case #%d: RICHARD\n",a);
        }
        if(x==3)
        {
            if(r%3==0 && c>=2)
               fprintf(op,"Case #%d: GABRIEL\n",a);
            else if(c%3==0 && r>=2)
                fprintf(op,"Case #%d: GABRIEL\n",a);
            else
                fprintf(op,"Case #%d: RICHARD\n",a);
        }
        if(x==4)
        {
            if(r%4==0 && c>2)
                fprintf(op,"Case #%d: GABRIEL\n",a);
            else if(c%4==0 && r>2)
                fprintf(op,"Case #%d: GABRIEL\n",a);
            else
                fprintf(op,"Case #%d: RICHARD\n",a);
        }
        a++;
    }
}
