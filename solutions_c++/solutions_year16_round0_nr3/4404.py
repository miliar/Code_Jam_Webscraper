#include <bits/stdc++.h>

using namespace std;

 long long isPrime(long long val){
    long long i;
    for(i = 2; i * i <= val; i ++){
        if(val % i == 0)
            return i;
    }
    return -1;
}

long long power(long long int x, long long  int y)
{
    long long int temp;
    if( y == 0)
        return 1;
    temp = power(x, y/2);
    if (y%2 == 0)
        return temp*temp;
    else
        return x*temp*temp;
}

int main() {
    ifstream fileIn;
    ofstream fileOut;
    fileIn.open("main.txt");
    fileOut.open("out.txt");

    int i = 1, results = 0;
    fileOut << "Case #1:\n";
    while(i <= 16384 && results < 50){
        string num;
        bool flag = false;
        int factors[10] = {0};

        fileIn >> num;

        long long no = 0, count = 0;

        for(int base = 2; base <= 10; base ++){
            no = 0;
            int p = 0;

            for(p = 15; p >= 0; p --){
                no = no + (num[15 - p] - '0') * power(base, p);
            }

            long long ans = isPrime(no);
            if(ans > 0){
                factors[count] = ans;
                count ++;
            }
            else{
                flag = true;
                break;
            }
        }

        if(!flag){
            results ++;
            fileOut << num << " ";

            for(int base = 0; base < 9; base ++)
                fileOut << factors[base] << " ";
            fileOut << "\n";
        }
    }
    return 0;
}
