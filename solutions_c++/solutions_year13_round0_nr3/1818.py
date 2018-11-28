#include <iostream>
#include <fstream>
#include <string>
#include <math.h>

using namespace std;
ifstream in;
ofstream out;
long long ti4 = 10000;
long long ti5 = 100000;
long long ti6 = 1000000;
long long ti7 = 10000000;
long long ti8 = 100000000;
long long ti9 = 1000000000;
long long ti10 = 10000000000;
long long ti11 = 100000000000;
long long ti12 = 1000000000000;
long long ti13 = 10000000000000;
long long ti14 = 10000000000000;

void print(int caseNumber, int solutionNumber){
    out << "Case #" << caseNumber << ": " << solutionNumber << endl;
}

bool palindrome(long long number){
    if(number<10){
        return true;
    }
    if(number<100){
        if(number/10==number%10){
            return true;
        }else{return false;}
    }
    if(number<1000){
        if(number/100==number%10){
            return true;
        }else{return false;}
    }
    if(number<ti4){
        if(number/1000==number%10 && (number%1000)/100==(number%100)/10){
            return true;
        }else{return false;}
    }
    if(number<ti5){
        if(number/ti4==number%10 && (number%ti4)/1000==(number%100)/10){
            return true;
        }else{return false;}
    }
    if(number<ti6){
        if(number/ti5==number%10 && (number%ti5)/ti4==(number%100)/10 && (number%ti4)/1000==(number%1000)/100){
            return true;
        }else{return false;}
    }
    if(number<ti7){
        if(number/ti6==number%10 && (number%ti6)/ti5==(number%100)/10 && (number%ti5)/ti4==(number%1000)/100){
            return true;
        }else{return false;}
    }
    if(number<ti8){
        if(number/ti7==number%10 && (number%ti7)/ti6==(number%100)/10 && (number%ti6)/ti5==(number%1000)/100 && (number%ti5)/ti4==(number%10000)/1000){
            return true;
        }else{return false;}
    }
    if(number<ti9){
        if(number/ti8==number%10 && (number%ti8)/ti7==(number%100)/10 && (number%ti7)/ti6==(number%1000)/100 && (number%ti6)/ti5==(number%ti4)/1000){
            return true;
        }else{return false;}
    }
    if(number<ti10){
        if(number/ti9==number%10 && (number%ti9)/ti8==(number%100)/10 && (number%ti8)/ti7==(number%1000)/100 && (number%ti7)/ti6==(number%ti4)/1000 && (number%ti6)/ti5==(number%ti5)/ti4){
            return true;
        }else{return false;}
    }
    if(number<ti11){
        if(number/ti10==number%10 && (number%ti10)/ti9==(number%100)/10 && (number%ti9)/ti8==(number%1000)/100 && (number%ti8)/ti7==(number%ti4)/1000 && (number%ti7)/ti6==(number%ti5)/ti4){
            return true;
        }else{return false;}
    }
    if(number<ti12){
        if(number/ti11==number%10 && (number%ti11)/ti10==(number%100)/10 && (number%ti10)/ti9==(number%1000)/100 && (number%ti9)/ti8==(number%ti4)/1000 && (number%ti8)/ti7==(number%ti5)/ti4 && (number%ti7)/ti6==(number%ti6)/ti5){
            return true;
        }else{return false;}
    }
    if(number<ti13){
        if(number/ti12==number%10 && (number%ti12)/ti11==(number%100)/10 && (number%ti11)/ti10==(number%1000)/100 && (number%ti10)/ti9==(number%ti4)/1000 && (number%ti9)/ti8==(number%ti5)/ti4 && (number%ti8)/ti7==(number%ti6)/ti5){
            return true;
        }else{return false;}
    }
    if(number<ti14){
        if(number/ti13==number%10 && (number%ti13)/ti12==(number%100)/10 && (number%ti12)/ti11==(number%1000)/100 && (number%ti11)/ti10==(number%ti4)/1000 && (number%ti10)/ti9==(number%ti5)/ti4 && (number%ti9)/ti8==(number%ti6)/ti5 && (number%ti8)/ti7==(number%ti7)/ti6){
            return true;
        }else{return false;}
    }else{return false;}
}

int main()
{
    out.open("out.txt");
    in.open("C-large-1.in");
    int T;
    in >> T;
    for(int i=1; i<=T; i++){
        cout << i << endl;
        double tald1,tald2;
        long long tali1, tali2;

        in >> tali1 >> tali2;

        tald1=tali1;
        tald2=tali2;

        long long tal1, tal2;
        tal1=sqrt(tald1);
        while(tal1*tal1<tali1){
            tal1++;
        }
        tal2=sqrt(tald2);
        while(tal2*tal2>tali2){
            tal2--;
        }
        long long output=0;
        for(long long j=tal1; j<=tal2; j++){
            if(palindrome(j)){
                if(palindrome(j*j)){
                    output++;
                }
            }
        }
        print(i,output);
    }
    out.close();
    in.close();
    return 0;
}
