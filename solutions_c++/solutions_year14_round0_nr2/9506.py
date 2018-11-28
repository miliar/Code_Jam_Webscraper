#include <iostream>
#include<cstdio>
using namespace std;

int main()
{
    int T;
    double C,F,X;
    double Init_Time=2.0,CT=0.0,XT=0.0,Min_Time=2000.0000000;
    int flag,case_num=1;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%lf %lf %lf",&C,&F,&X);
        flag=1;
        Init_Time=2.0;
        CT=0.0;
        XT=0.0;
        Min_Time=2000.0000000;
        do
        {
            XT=CT+(X/Init_Time);
            CT+=C/Init_Time;
            Init_Time+=F;
            if(Min_Time>XT)
            {
                Min_Time=XT;
            }
            else
            {
                    flag=0;
                  //  break;
            }
        }while(flag);
        printf("Case #%d: %lf\n",case_num,Min_Time);
        case_num+=1;
    }
    return 0;
}
