#include <iostream>
#include <string>
#include <math.h>
#include <sstream>


using namespace std;

bool is_palindrome(int number);
bool perfect_root(int number);

int main()
{

    int a,b;
    int number;
    int p = 0;

    cin >> number;
    for(int i = 0; i < number; ++i){
        cin >> a;
        cin >> b;
        p = 0;
        cout << "Case #" << i+1 << ": ";
        for(int x = a; x <= b; ++x){
            if(perfect_root(x) && is_palindrome(x) && is_palindrome(sqrt(float(x)))){
                p++;
            }
        }
        cout << p << endl;
    }
    return 0;
}

bool perfect_root(int number){
    double d_sqrt = sqrt(number);
    int i_sqrt = d_sqrt;
    if ( d_sqrt == i_sqrt ){
        return true;
    }
    return false;
}

string convertInt(int number)
{
   stringstream ss;//create a stringstream
   ss << number;//add number to the stream
   return ss.str();//return a string with the contents of the stream
}

bool is_palindrome(int number){
    string n = convertInt(number);
    for(int i = 0; i < n.length()/2+1; ++i){
        if(n.at(n.length()-i-1) != n.at(i)){
            return false;
        }
    }
    return true;
}
