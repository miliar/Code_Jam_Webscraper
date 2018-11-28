#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    int t;
    FILE *fp,*op;

    fp=fopen("D-small-attempt0.in","r");
    op=fopen("output.txt","w");
    fscanf(fp,"%d",&t);
    int p=1;
    while(t--)
    {
        int x,r,c;

        fscanf(fp,"%d %d %d",&x,&r,&c);
        if(x==1)
            fprintf(op,"Case #%d: GABRIEL\n",p);
        if(x==2)
        {
            if(r%2==0 || c%2==0)
                fprintf(op,"Case #%d: GABRIEL\n",p);
            else
                fprintf(op,"Case #%d: RICHARD\n",p);
        }
        if(x==3)
        {
            if(r%3==0 && c>=2)
               fprintf(op,"Case #%d: GABRIEL\n",p);
            else if(c%3==0 && r>=2)
                fprintf(op,"Case #%d: GABRIEL\n",p);
            else
                fprintf(op,"Case #%d: RICHARD\n",p);

        }
        if(x==4)
        {
            if(r==4 && c>2)
                fprintf(op,"Case #%d: GABRIEL\n",p);
            else if(c==4 && r>2)
                fprintf(op,"Case #%d: GABRIEL\n",p);
            else
                fprintf(op,"Case #%d: RICHARD\n",p);


        }
        p++;
    }
}

