#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    FILE *inp, *outp;
    int cases, choose1, choose2, a, b, c, d, e, f, g, h, t, x=0, i=1;
    inp=fopen("A-small-attempt0.in","r");
    outp=fopen("output.txt","w");
    fscanf(inp,"%d",&cases);
    while(cases--)
    {
        fscanf(inp,"%d",&choose1);
        if(choose1==1)
            fscanf(inp,"%d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d",&a,&b,&c,&d,&t,&t,&t,&t,&t,&t,&t,&t,&t,&t,&t,&t);
        if(choose1==2)
            fscanf(inp,"%d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d",&t,&t,&t,&t,&a,&b,&c,&d,&t,&t,&t,&t,&t,&t,&t,&t);
        if(choose1==3)
            fscanf(inp,"%d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d",&t,&t,&t,&t,&t,&t,&t,&t,&a,&b,&c,&d,&t,&t,&t,&t);
        if (choose1==4)
            fscanf(inp,"%d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d",&t,&t,&t,&t,&t,&t,&t,&t,&t,&t,&t,&t,&a,&b,&c,&d);
        fscanf(inp,"%d",&choose2);
        if(choose2==1)
            fscanf(inp,"%d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d",&e,&f,&g,&h,&t,&t,&t,&t,&t,&t,&t,&t,&t,&t,&t,&t);
        if(choose2==2)
            fscanf(inp,"%d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d",&t,&t,&t,&t,&e,&f,&g,&h,&t,&t,&t,&t,&t,&t,&t,&t);
        if(choose2==3)
            fscanf(inp,"%d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d",&t,&t,&t,&t,&t,&t,&t,&t,&e,&f,&g,&h,&t,&t,&t,&t);
        if (choose2==4)
            fscanf(inp,"%d %d %d %d %d %d %d %d %d %d %d %d %d %d %d %d",&t,&t,&t,&t,&t,&t,&t,&t,&t,&t,&t,&t,&e,&f,&g,&h);
        if(a==e||a==f||a==g||a==h)
            x++;
        if(b==e||b==f||b==g||b==h)
            x++;
        if(c==e||c==f||c==g||c==h)
            x++;
        if(d==e||d==f||d==g||d==h)
            x++;
        if(x==0)
            fprintf(outp,"Case #%d: Volunteer cheated!\n",i);
        if(x>1)
            fprintf(outp,"Case #%d: Bad magician!\n",i);
        if(x==1)
        {
            if(a==e||a==f||a==g||a==h)
                fprintf(outp,"Case #%d: %d\n",i,a);
            if(b==e||b==f||b==g||b==h)
                fprintf(outp,"Case #%d: %d\n",i,b);
            if(c==e||c==f||c==g||c==h)
                fprintf(outp,"Case #%d: %d\n",i,c);
            if(d==e||d==f||d==g||d==h)
                fprintf(outp,"Case #%d: %d\n",i,d);
        }
        i++;
        x=0;
    }
    fclose(inp);
    fclose(outp);
    return 0;
}
