#include<iostream>
#include<fstream>
using namespace std;

long long ipow(long long base, long long exp)
{
    long long result = 1;
    while (exp)
    {
        if (exp & 1)
            result *= base;
        exp >>= 1;
        base *= base;
    }

    return result;
}

int main(){

ifstream input("D-small-attempt1.in");
ofstream out("D.txt");
long long T , k  , s , c;
input >> T;
for(int t = 1; t <= T; t++){

input >> k >> c >> s;
out << "Case #"<< t << ": ";
c = ipow(k , (int)c-1);
for(int i = k-1 ; i >= 0 ; i--){
out << (long long)c*(k-i) << " ";

}
out << endl;

}
}

