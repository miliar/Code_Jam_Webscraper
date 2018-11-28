//
//  main.cpp
//  googleJam
//
//  Created by Nguyen Viet Trung on 3/29/16.
//  Copyright © 2016 Nguyen Viet Trung. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <istream>
#include <string>
#include <sstream>
#include <algorithm>    // std::set_intersection, std::sort
#include <vector>       // std::vector
#include <iomanip>
#include <math.h>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <list>
#include <complex>
#include <stack>
#include <cmath>
#include <iostream>
#include <sstream>
#include <cctype>
#include <cstdlib>
#include <utility>
#include <bitset>
#include <assert.h>
#include <stdio.h>      /* printf, NULL */
#include <stdlib.h>

using namespace std;

struct BigNumber
{
    int arr[100] = {0};
    int cursor = 0;
};
BigNumber makeInterger (int c)
{
    BigNumber result;
    result.arr[0] = c;
    result.cursor = 0;
    return result;
}

BigNumber multi(BigNumber a, int c)
{
    BigNumber result;
    result.cursor = a.cursor;
    int temp = 0;
    for (int i = 0; i <= a.cursor; i++) {
        int x = a.arr[i] * c + temp;
        result.arr[i] = x%10;
        temp = x/10;
    }
    while(temp > 0)
    {
        result.cursor++; // increments digit counter
        result.arr[result.cursor] = temp % 10;
        temp = temp/10;
    }
    return result;
}

BigNumber add(BigNumber a, int c)
{
    int temp = c;
    for (int i = 0; i <= a.cursor; i++) {
        int x = a.arr[i] + temp;
        a.arr[i] = x%10;
        temp = x/10;
    }
    while(temp > 0)
    {
        a.cursor++; // increments digit counter
        a.arr[a.cursor] = temp % 10;
        temp = temp/10;
    }
    return a;
}

BigNumber subtract(BigNumber a, BigNumber b)
{
    BigNumber result;
    result.cursor = a.cursor;
    int temp = 0;
    for (int i = 0; i <= a.cursor; i++)
    {
        if (a.arr[i] < b.arr[i] + temp)
        {
            result.arr[i] = (a.arr[i] + 10) - b.arr[i] - temp;
            temp = 1;
        }
        else
        {
            result.arr[i] = a.arr[i] - b.arr[i] - temp;
            temp = 0;
        }
    }
    for (int i = a.cursor; i > 0; i--)
    {
        if (result.arr[i] != 0)
            break;
        result.cursor--;
    }
    return result;
}

bool compareBigNumber (BigNumber a, BigNumber b)
{
    //1: a, 0:b
    if (a.cursor == b.cursor)
    {
        for (int i = a.cursor; i >= 0; i--) {
            if (a.arr[i] == b.arr[i])
                continue;
            return (a.arr[i] > b.arr[i]);
        }
    }
    return (a.cursor > b.cursor);
}

//BigNumber devide(BigNumber a, BigNumber b, bool* stillHaveRemainer)
//{
//    
//}
bool checkIsEqualZero (BigNumber a)
{
    //1: a, 0:b
    for (int i = a.cursor; i >= 0; i--) {
        if (a.arr[i] != 0)
            return false;
    }
    return true;
}

BigNumber devide(BigNumber a, BigNumber b, BigNumber &remainer)
{
    BigNumber result;
    int count = a.cursor;
    BigNumber temp;
    temp.cursor = b.cursor;
    for (int i = b.cursor; i >= 0; i--) {
        temp.arr[i] = a.arr[a.cursor - (b.cursor - i)];
        count = a.cursor - (b.cursor - i);
    }
    while(count >= 0){
        if(compareBigNumber(b, temp)){
            if (count == 0)
                break;
            count--;
            temp = add(multi(temp, 10), a.arr[count]);
            if (compareBigNumber(makeInterger(b.arr[b.cursor]), temp))
                result = multi(result, 10);
        }
        else{
            int did;
            if (temp.arr[b.cursor + 1] != 0)
                did = (temp.arr[b.cursor + 1] * 10 + temp.arr[b.cursor]) / b.arr[b.cursor];
            else
                did = temp.arr[b.cursor] / b.arr[b.cursor];
            
            BigNumber did2 = multi(b, did);
            
            while (compareBigNumber(did2, temp))
            {
                did--;
                did2 = multi(b, did);
            }
            temp = subtract(temp, did2);
            result = multi(result, 10);
            result = add(result, did);
        }
    }
    remainer = temp;
    result.cursor = a.cursor;
    for (int i = a.cursor; i >= 0; i--)
    {
        if (result.arr[i] != 0)
            break;
        result.cursor--;
    }
    return result;
}

BigNumber isPrime (BigNumber num)
{
    BigNumber result = makeInterger(0);
    if (num.arr[0] <=1 && num.cursor == 0)
        return makeInterger(1);
    else if (num.arr[0] == 2 && num.cursor == 0)
        return makeInterger(0);
    else if (num.arr[0] % 2 == 0)
        return makeInterger(2);
    else
    {
        BigNumber divisor = makeInterger(3);
        BigNumber remainer;
        while (!compareBigNumber(divisor, devide(num, makeInterger(2), remainer)))
        {
            devide(num, divisor, remainer);
            if (checkIsEqualZero(remainer))
            {
                result = divisor;
                break;
            }
            divisor = add(divisor, 2);
        }
        return result;
    }
}

//Coin Jam
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
int main(int argc, const char * argv[]) {
    // insert code here...
    ifstream input;
    input.open("input.txt");
    
    ofstream output;
    output.open("output.txt");
    int T;
    input >> T;
    for (int t = 1; t <= T; t++) {
        int N;
        int J;
        input >> N >> J;
        BigNumber arr[100];
        int count = 0;
        output << "Case #" << t << ": " << endl;
        for(long long i = 0; i < pow(2, N/2 - 1); ++i) {
            BigNumber a;
            a.arr[N - 1] = 1;
            a.arr[0] = 1;
            a.cursor = N - 1;
            for(int j = 0; j < N/2 - 1; j++) {
                long long temp = i / pow(2, j);
                a.arr[j + 1] = (temp % 2);
                a.arr[N - 2 - j] = a.arr[j + 1];
            }
            for (int b = a.cursor; b >= 0; b--) {
                cout << a.arr[b];
            }
            cout << endl;
            int countJ = 0;
            for (int c = 2; c <= 10; c++) {
                //tinh ra so base
                BigNumber baseNumber;
                for (int b = 0; b < N; b++) {
                    baseNumber = add(multi(baseNumber, c),a.arr[b]);
                }
                
                BigNumber divisor = isPrime(baseNumber);
                if (compareBigNumber(divisor, makeInterger(0)))
                {
                    arr[c] = divisor;
                    countJ++;
                }
                else
                    break;
            }
            if (countJ == 9)
            {
                for (int b = a.cursor; b >= 0; b--) {
                    output << a.arr[b];
                }
                output << " ";
                for (int c = 2; c <= 10; c++) {
                    for (int b = arr[c].cursor; b >= 0; b--) {
                        output << arr[c].arr[b];
                    }
                    output << " ";
                }
                output << endl;
                count++;
            }
            
            if (count == J)
                break;
        }
    }
    
    
    input.close();
    return 0;
}
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////