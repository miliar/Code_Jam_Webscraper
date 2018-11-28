#include <iostream>
#include <fstream>
#include <bitset>
#include <cmath>

#define BSETC 16

using namespace std;

bool isPrime (unsigned long long num)
{
    if (num <=1)
        return false;
    else if (num == 2)         
        return true;
    else if (num % 2 == 0)
        return false;
    else
    {
        bool prime = true;
        unsigned long long divisor = 3;
        unsigned long long num_d = static_cast<unsigned long long>(num);
        unsigned long long upperLimit = static_cast<unsigned long long>(sqrt(num_d) +1);
        
        while (divisor <= upperLimit)
        {
            if (num % divisor == 0)
                prime = false;
            divisor +=2;
        }
        return prime;
    }
}

int main() {
    ifstream fi("in");
    ofstream fw("out");

    int T, size, count;

    fi >> T >> size >> count;
    for(int i=0; i<T ; ++i) {
        fw << "Case #" << (i+1) << ":"<<endl;
        unsigned long long j = (1 << (size-1)) + 1;
        
        while(count) {
            bool correct = true;
            bitset<BSETC> bset(j);
            cout << "Try with bitset " << bset << endl;
            unsigned long long d[9] = {0};
            for(int k=2; k<=10; ++k) {
                unsigned long long jrep = 0;

                for(int l=0; l<size; l++) {
                    if ((1 << l) & j) {
                        jrep += pow(k, l);
                    }
                }
                cout << "jrepr in base=" << k << " is " << jrep << endl;

                cout << "Check is prime"<< endl;
                if(isPrime(jrep)) {
                    correct = false;
                    break;
                }
                cout << "Try to find the divisor"<< endl;

                /* Find divisor for base k */
                for(unsigned long long m=2; m<jrep; ++m) {
                    if(jrep % m == 0) {
                        cout << "jrep is divisible by " << m << endl;
                        d[k-2] = m;
                        break;
                    }

                }

                if(d[k-2] == 0) {
                    correct = false;
                    break;
                }
            }

            if(correct) {
                count --;
                bitset<BSETC> bs(j);
                fw << bs ;
                for(int k=0;k<9; ++k) {
                    fw << " " << d[k];
                }
                fw << endl;
                cout << "IS A JAM " << bs << endl;
            }

            j+=2;
        }





    }


    fw.close();
    fi.close();
    return 0;
}