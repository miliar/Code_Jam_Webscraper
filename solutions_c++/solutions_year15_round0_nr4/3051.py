#include <iostream>
#include <stdio.h>

int main()
{
    // Hacked approached.
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);


    int tcase,a,b,c,casecount,temp;

    scanf("%d",&tcase);
    casecount=0;

    while(tcase--)
    {


        scanf("%d%d%d",&a,&b,&c);

        if(b>c)
        {
            temp=b;
            b=c;
            c=temp;
        }

        casecount++;

        if(a==1)
        {

            printf("Case #%d: GABRIEL\n",casecount);
        }
        else if(a==2)
        {
            if((b==1 && c ==1)||(b==3 && c==3)||(b==1 && c==3))
            {
                    printf("Case #%d: RICHARD\n",casecount);
            }
            else
            {
                    printf("Case #%d: GABRIEL\n",casecount);
            }
        }
        else if(a==3)
        {
            if((b==2 && c ==3)||(b==3 && c==3)||(b==3 && c==4))
            {
                    printf("Case #%d: GABRIEL\n",casecount);
            }
            else
            {
                    printf("Case #%d: RICHARD\n",casecount);
            }
        }
        else if(a==4)
        {
            if((b==4 && c==4)||(b==3 && c==4))
            {
                    printf("Case #%d: GABRIEL\n",casecount);
            }
            else
            {
                    printf("Case #%d: RICHARD\n",casecount);
            }
        }

    }
    return 0;
}
