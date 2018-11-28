#include <iostream>
#include <vector>
//#include <algorithm>
#include <string>
//#include <stack>
#include <unordered_map>
//#include <limits.h>
#include <time.h>
//#include <queue>
#include <fstream>
using namespace std;

bool isComposite(long n, long& minDivisor){
    for(long i = 2; i * i <= n; ++i){
        if(n % i == 0){
            minDivisor = i;
            return 1;
        }
    }
    return 0;
}

string binary(unsigned x)
{
    string s;
    do
    {
        s.push_back('0' + (x & 1));
    } while (x >>= 1);
    reverse(s.begin(), s.end());
    return s;
    
}
long baseAt(string str, int base){
    long result = 0;
    for(int i = str.length() - 1, j = 0; i >= 0; --i, ++j){
        if(str[i] == '1') result += (long)pow(base, j);
    }
    return result;
}

int main(){
    int t; cin >> t; //t == 1
    int n, j;
    cin >> n >> j;
    cout << "Case #1:" << endl;
    long min;
//    unordered_map<int, int> composites;
//    ////////////
//    long range = 0;
//    for(int i = 0; i < n; ++i){
//        range *= 10;
//        ++range;
//    }
//    for(int i = 4; i < range + 1; ++i){    //store all prime numbers
//        if(isComposite(i, min)){
//            composites[i] = min;
//        }
//    }
    //////////////////////
    //test all primes;
    /*
    unordered_map<int, int>::iterator q = composites.begin();
    while(q != composites.end()){
        cout << q -> first << ": " << q -> second << endl;
        ++q;
    }
    return 0;
     */
    ///////////////////
    int number = 0; number |= 1; number |= 1 << (n - 1);
    int count = 0;
    bool state;
    int minDivisor[9];
    while(number < (1 << n)){
        state = 1;
        string str = binary(number);
        for(int i = 2; i <= 10; ++i){
            long interpretation = baseAt(str, i);
            if(!isComposite(interpretation, min)){
                state = 0;
                break;
            }
            minDivisor[i - 2] = min;
        }
        if(state){
            ++count;
            cout << binary(number);
            for(int i = 0; i < 9; ++i)
                cout << ' ' << minDivisor[i];
            cout << endl;
        }
        if(count == j)
            break;
        number += 2;
    }
    return 0;
}

