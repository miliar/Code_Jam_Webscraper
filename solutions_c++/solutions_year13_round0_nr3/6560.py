#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <cmath>

#include <stdio.h>
#include <string.h>

using namespace std;

bool ispal(long long pal){
    int n1, n2;
    if (pal%10==pal){
        return true;
    }
    else if ((pal<100) && (pal%10==(pal-pal%10)/10)){
        return true;
    }
    else if ((pal<1000) && (pal%10==(pal-pal%100)/100)){
        return true;
    }
    else{
        if (pal % 2==0){
            n1=pal/2;
            n2=pal/2;
        }
        else{
            n1=int(pal/2)+1;
            n2=int(pal/2);
        }
    }
    return false;
}

int main()
{
    ifstream input ("C-small-attempt0.in");
    ofstream output ("sqr.out");

    int T;

    input >> T;

    for (int test=0; test<T; test++){
        int A, B;
        long long ctr=0;
        input >> A >> B;
        for(int num=sqrt(A); num<sqrt(B)+1; num++){
            if ((ispal(num)==true) && (ispal(num*num)==true)){
                if ((num*num>A-1) && (num*num<B+1)){
                    ctr++;
                    //output << num*num << "\n";
                }
            }
        }
        output << "Case #" << test+1 << ": " << ctr << "\n";
    }

    return 0;
}
