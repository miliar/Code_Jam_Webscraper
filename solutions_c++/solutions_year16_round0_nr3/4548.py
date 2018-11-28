//
//  main.cpp
//  Coin Jam Cpp
//
//  Created by jarvis on 4/10/16.
//  Copyright © 2016 jarvis. All rights reserved.
//

#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>

using namespace::std;

bool isPrime(long num);
void check();
char s[32] = {0};
long val[9] = {0};
int T, N, J;
long factor;
long i, j, sum, value, count;
char *p;
short isPrimeFlag, visited;

void generate(int ones, int zeros, string str, int len);


int main(int argc, const char * argv[]) {
    scanf("%d", &T);
        scanf("%d%d", &N, &J);
        printf("Case #1:\n");
        memset(s, 0, sizeof(s));
        memset(val, 0l, sizeof(val));
//        s[0] = '1';
        //        s[N - 1] = '1';
        
//        p = s;
//        ++p;
//        visited = 0;
        ::count = 0;
        
        string str = "";
        generate(0, 0, str, N - 2);
        
        
        
    
    return 0;

}

void generate(int ones, int zeros, string str, int len)
{
    if (len == str.length()) {
        str = "1" + str;
        str = str + "1";
        memset(s, 0, sizeof(s));
        strcpy(s, str.c_str());
        if (::count < J) {
            check();

        }
        return;
    }
 
    generate(ones + 1, zeros, str + "1", len);
    if (ones > zeros) {
            generate(ones, zeros + 1, str + "0", len);

    }
}

bool isPrime(long num)
{
    if (num==2||num==3||num==5)
        return true;
    unsigned long c=7;
    if (num%2==0||num%3==0||num%5==0||num==1)
        return false;
    int maxc=int(sqrt(num));
    while (c<=maxc)
    {
        if (num%c==0)
            return false;
        c+=4;
        if (num%c==0)
            return false;
        c+=2;
        if (num%c==0)
            return false;
        c+=4;
        if (num%c==0)
            return false;
        c+=2;
        if (num%c==0)
            return false;
        c+=4;
        if (num%c==0)
            return false;
        c+=6;
        if (num%c==0)
            return false;
        c+=2;
        if (num%c==0)
            return false;
        c+=6;
    }
    return true;
}

void check()
{
    isPrimeFlag = 0;
    for (i = 2; i <= 10; ++i) {
        factor = i;
        sum = 0;
        for (j = 0; j < N - 1; ++j) {
            if (s[j] == '1') {
                sum += 1;
            }
            sum *= factor;
        }
        if (s[N - 1] == '1') {
            sum += 1;
        }
        if (isPrime(sum)) {
            isPrimeFlag = 1;
            break;
        }
        val[i - 2] = sum;
    }
    if (!isPrimeFlag && ::count <= J) {
        // print nontrivial divisor
        ::count++;
//        printf("%ld: %s ", ::count, s);
        printf("%s ", s);

        for (i = 2; i <= 10; ++i) {
            value = val[i - 2];
            for (j = 2; j * j < val[i - 2]; ++j) {
                if (!(val[i - 2] % j)) {
                    value = j;
                    break;
                }
            }
            if (i != 10) {
                printf("%ld ", value);
            } else {
                printf("%ld\n", value);
            }
        }
    }
}