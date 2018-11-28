#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <sstream>
#include <cmath>
#include <bitset>
#define ll long long
using namespace std;

bool checkprime(double num) {
     if ((ll)num%2==0) {
        return false;
     }
     ll limit = (ll)round(sqrt(num));
     for (ll i=3;i<=limit;i=i+2) {
         if (((ll)num%i)==0) {
            //cout << num << " this is not prime" << endl;
            return false;
         }
     }
     //cout << num << " prime" << endl;
     return true;
}

string ConvertToBinary(double n)
{
    string binary;
    if ((ll)n / 2 != 0) {
        binary += ConvertToBinary(n / 2);
    }
    ll result = (ll) n%2;
    stringstream ss;
    ss << result;
    string str = ss.str();
    binary += str;
    return binary;
}

double conversion(string binary,double base,int n) {
       double result=0;
       for (int i=0;i<n;i++) {
           string str = binary.substr(i,1);
           double a = atoi( str.c_str() );
           result += a*pow(base,n-1-i);
       }
       return result;
}

ll findfactor(double num) {
    ll limit = (ll)round(sqrt(num));
    for (ll i=2;i<limit;i++) {
        if ((ll)num%i==0) {
           return i;
        }
    }
}

int main() {
    int t;
    cin >> t;
    for (int i=0;i<t;i++) {
        int n,j;
        cin >> n >> j;
        ll answer[j][9];
        string answerbinary[j];
        double num[9];
        double first = pow(2.0,n-1) + 1;
        ll lim = (int)pow(2.0,n-2)-1;
        int loopend = 0;
        for(ll k=0;k<=1000;k++) {
                      num[0] = first + k*2;
                      if (checkprime(num[0])==false) {
                         string binary = ConvertToBinary(num[0]);
                         //cout << binary << " " << num[0] << endl;
                         bool prime = false;
                         for (double a=3.0;a<=10;a++) {
                             if (checkprime(conversion(binary,a,n))) {
                                prime = true;
                                break;
                             }
                         }
                         if (prime==false) {
                            for (double a=0;a<9;a++) {
                                double abc = conversion(binary,a+2,n);
                                answer[loopend][(int)a] = findfactor(abc);
                                //cout << answer[loopend][(int)a] << " " << abc << " " << num[0] << endl;;
                                answerbinary[loopend] = binary;
                            }
                            loopend++;
                            //cout << loopend << endl;
                         } else {
                           //cout << k << "prime" << endl;
                         }
                       } else {
                         //cout << k << "prime" << endl;
                       }
                       if (loopend==j) {
                          break;
                       }
        }
        cout << "Case #1:" << endl;
        for (int k=0;k<loopend;k++) {
            cout << answerbinary[k] << " ";
            for (int a=0;a<9;a++) {
                cout << answer[k][a] << " ";
            }
            cout << endl;
        }
    }
    /*for (int i=0;i<t;i++) {
        cout << "Case #" << i+1 << ": " << answer[i] << endl;
    }*/
    return 0;
}
