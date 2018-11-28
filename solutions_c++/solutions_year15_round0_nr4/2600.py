#include<bits/stdc++.h>
int main()
{
    int t;
    FILE *f,*g;
    f=fopen("InputFile1.txt","r");
    g=fopen("OutputFile1.txt","w");
    fscanf(f,"%d",&t);
    int u=t;
    while(t--)
    {
        int x,r,c;
        fscanf(f,"%d %d %d",&x,&r,&c);
        if(r>c)
        {
            int temp=r;
            r=c;
            c=temp;
        }
        if(r==1 && c==1)
        {
            if(x==1)
            {
                 fprintf(g,"Case #%d: GABRIEL\n",u-t);
            }
            else if(x==2)
            {
                 fprintf(g,"Case #%d: RICHARD\n",u-t);
            }
            else if(x==3)
            {
                 fprintf(g,"Case #%d: RICHARD\n",u-t);
            }
            else if(x==4)
            {
                 fprintf(g,"Case #%d: RICHARD\n",u-t);
            }
        }
        else if(r==1 && c==2)
        {
            if(x==1)
            {
                 fprintf(g,"Case #%d: GABRIEL\n",u-t);
            }
            else if(x==2)
            {
                 fprintf(g,"Case #%d: GABRIEL\n",u-t);
            }
            else if(x==3)
            {
                 fprintf(g,"Case #%d: RICHARD\n",u-t);
            }
            else if(x==4)
            {
                 fprintf(g,"Case #%d: RICHARD\n",u-t);
            }
        }
        else if(r==1 && c==3)
        {
            if(x==1)
            {
                 fprintf(g,"Case #%d: GABRIEL\n",u-t);
            }
            else if(x==2)
            {
                 fprintf(g,"Case #%d: RICHARD\n",u-t);
            }
            else if(x==3)
            {
                 fprintf(g,"Case #%d: RICHARD\n",u-t);
            }
            else if(x==4)
            {
                 fprintf(g,"Case #%d: RICHARD\n",u-t);
            }
        }
        else if(r==1 && c==4)
        {
            if(x==1)
            {
                 fprintf(g,"Case #%d: GABRIEL\n",u-t);
            }
            else if(x==2)
            {
                 fprintf(g,"Case #%d: GABRIEL\n",u-t);
            }
            else if(x==3)
            {
                 fprintf(g,"Case #%d: RICHARD\n",u-t);
            }
            else if(x==4)
            {
                 fprintf(g,"Case #%d: RICHARD\n",u-t);
            }
        }
        else if(r==2 && c==2)
        {
            if(x==1)
            {
                 fprintf(g,"Case #%d: GABRIEL\n",u-t);
            }
            else if(x==2)
            {
                 fprintf(g,"Case #%d: GABRIEL\n",u-t);
            }
            else if(x==3)
            {
                 fprintf(g,"Case #%d: RICHARD\n",u-t);
            }
            else if(x==4)
            {
                 fprintf(g,"Case #%d: RICHARD\n",u-t);
            }
        }
        else if(r==2 && c==3)
        {
           if(x==1)
            {
                 fprintf(g,"Case #%d: GABRIEL\n",u-t);
            }
            else if(x==2)
            {
                 fprintf(g,"Case #%d: GABRIEL\n",u-t);
            }
            else if(x==3)
            {
                 fprintf(g,"Case #%d: GABRIEL\n",u-t);
            }
            else if(x==4)
            {
                 fprintf(g,"Case #%d: RICHARD\n",u-t);
            }
        }
        else if(r==2 && c==4)
        {
            if(x==1)
            {
                 fprintf(g,"Case #%d: GABRIEL\n",u-t);
            }
            else if(x==2)
            {
                 fprintf(g,"Case #%d: GABRIEL\n",u-t);
            }
            else if(x==3)
            {
                 fprintf(g,"Case #%d: RICHARD\n",u-t);
            }
            else if(x==4)
            {
                 fprintf(g,"Case #%d: RICHARD\n",u-t);
            }
        }
        else if(r==3 && c==3)
        {
            if(x==1)
            {
                 fprintf(g,"Case #%d: GABRIEL\n",u-t);
            }
            else if(x==2)
            {
                 fprintf(g,"Case #%d: RICHARD\n",u-t);
            }
            else if(x==3)
            {
                 fprintf(g,"Case #%d: GABRIEL\n",u-t);
            }
            else if(x==4)
            {
                 fprintf(g,"Case #%d: RICHARD\n",u-t);
            }
        }
        else if(r==3 && c==4)
        {
            if(x==1)
            {
                 fprintf(g,"Case #%d: GABRIEL\n",u-t);
            }
            else if(x==2)
            {
                 fprintf(g,"Case #%d: GABRIEL\n",u-t);
            }
            else if(x==3)
            {
                 fprintf(g,"Case #%d: GABRIEL\n",u-t);
            }
            else if(x==4)
            {
                 fprintf(g,"Case #%d: GABRIEL\n",u-t);
            }
        }
        else if(r==4 && c==4)
        {
            if(x==1)
            {
                 fprintf(g,"Case #%d: GABRIEL\n",u-t);
            }
            else if(x==2)
            {
                 fprintf(g,"Case #%d: GABRIEL\n",u-t);
            }
            else if(x==3)
            {
                 fprintf(g,"Case #%d: RICHARD\n",u-t);
            }
            else if(x==4)
            {
                 fprintf(g,"Case #%d: GABRIEL\n",u-t);
            }
        }
    }
    return(0);
}
