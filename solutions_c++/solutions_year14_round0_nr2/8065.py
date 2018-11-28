#include <stdio.h>


double c, f, x;
double answer;

int main()
{
    int casen;

    scanf("%d", &casen );

    for(int i=1;i<=casen;i++)
    {
        double newAnswer;
        scanf("%lf%lf%lf", &c, &f, &x);

        answer = x / 2.0;

        newAnswer = answer;

        for(int j=1;;j++)
        {
            double buying = c / ( 2.0 + (double)(j-1) * f );
            double notbuying = x / ( 2.0 + (double) j * f );

            newAnswer -= x / ( 2.0 + (double)(j-1) * f );
            newAnswer += c / ( 2.0 + (double)(j-1) * f );
            newAnswer += x / ( 2.0 + (double)j * f );


            if ( newAnswer < answer )
                answer = newAnswer;
            else
                break;
        }


        printf("Case #%d: %.7lf\n", i, answer);
    }
    return 0;
}
