#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>


using namespace std; // since cin and cout are both in namespace std, this saves some text

bool isJamCoin(string, string&);
bool IsPrime(unsigned long);
int getDivisor(unsigned long);

bool isJamCoin(string numstr, string &divisors){
    unsigned long num;
    for(int b=2; b<=10; b++){
        num = std::stoul (numstr,nullptr,b);
        //cout<<"next num "<<num<<endl;
        int result = getDivisor(num);
        //cout<<"result "<<result<<endl;
        if(result==0){
            return false;
            }else{
            divisors = divisors + to_string(result) + " ";
        }
    }
    return true;
}


/*int getDivisor(unsigned long number)
{
    unsigned long i;
    for (i=2; i<number; i++)
    {
        if (number % i == 0)
        {
            return i;
        }
    }
    return 0;
}*/

int getDivisor(unsigned long num)
{
    
    if (num % 2 == 0)
        return 2;
    else
    {
        int divisor = 3;
        double num_d = static_cast<double>(num);
        int upperLimit = static_cast<int>(sqrt(num_d) +1);
        
        while (divisor <= upperLimit)
        {
            if (num % divisor == 0){
              return divisor;
            }

            divisor +=2;
        }
        return 0;
    }
}


void printCoingJams(int N, int J){
    int generatedJ = 0 ;
    
    for(int i=0; i<(N-2)*(N-2); i++){
        string str = std::bitset<30>(i).to_string();
        str = '1' + str.substr(30-(N-2)) + '1';
        //cout<<"next string = " << str<<endl;
        //check if it's jamcoin
        string divisors="";
        bool result = isJamCoin(str, divisors);
        if(result){
            generatedJ++;
            cout<<str<<" "<<divisors<<endl;
        }
        if(generatedJ==J){
            break;
        }
        
    }
    
}

int main() {
    int t,N,J;
    cin >> t; // read t. cin knows that t is an int, so it reads it as such.
    for (int i = 1; i <= t; ++i) {
        cin >> N >>J; // read n and then m.
        cout << "Case #" << i << ":" << endl;
        printCoingJams(N,J);
        //cout << "Case #" << i << ": " << (n + m) << " " << (n * m) << endl;
        // cout knows that n + m and n * m are ints, and prints them accordingly.
        // It also knows "Case #", ": ", and " " are strings and that endl ends the line.
    }
}