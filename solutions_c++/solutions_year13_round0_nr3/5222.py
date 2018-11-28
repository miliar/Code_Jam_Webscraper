#include <iostream>
#include <fstream>
#include <cmath>
#include <sstream>
using namespace std;
bool isPalindrome(int test)
{
     int length, pos;
     string s, invS;
     stringstream out;
     out << test;
     s = out.str();
     invS = string (s.rbegin(), s.rend());
     if(invS == s)
             return true;
     else
         return false;
}

int main() {
    ofstream out;
    ifstream in;
    in.open("C-small-attempt3.in");
    out.open("C-small-attempt3.out");
    int N, start, end, count = 0;
    float root;
    in >> N;
    for(int i = 0; i < N; i++) {
            in >> start >> end;
            count = 0;
            for(int p = start; p <= end; p++) {
                    if(isPalindrome(p)) {
                              if(sqrt(p) == (int)(sqrt(p)) && isPalindrome(sqrt(p))) {
                                          count++;
                                          }
                    }
            }
            out << "Case #" << i + 1 << ": " << count << endl;
    }
}
