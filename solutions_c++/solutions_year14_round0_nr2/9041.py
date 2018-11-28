
#include <iostream>
using namespace std;

int main(int argc, const char * argv[])
{

    int TestNum;
    scanf("%d", &TestNum);
    
    int test=81;
    while (test <= TestNum) {
        double     C,F,X;
        scanf("%le %le %le", &C,&F, &X);

        double currentF=2;
        double NOW=X/currentF;
        double NEXT=(C/currentF)+(X/(currentF+F));
        
        double totatTime=0;

        
        while (NEXT < NOW) {

            totatTime+=(C/currentF);
            currentF+=F;
            NOW=X/currentF;
            NEXT=(C/currentF)+(X/(currentF+F));

        }
        
        totatTime+=NOW;
        
        printf("Case #%i: %0.7f \n",test,totatTime);

        
        test++;
        
    }
    return 0;

}

