#include <iostream>
#include <map>
#include <cmath>

using namespace std;

unsigned long long pow2(unsigned long long i, int p) {
    if(p == 0) return 1;
    if(p == 1) return i;
    return i * pow2(i, p-1);
}

unsigned long long* getRepresentations(int i) {
    unsigned long long* result = new unsigned long long[9];
    result[0]=i;

    for(int j=1; j<9; j++) {
        result[j] = 0;
    }

    int pos = 0;
    while(i>0) {
        if(i%2==1) {
            for(int j=3; j<11; j++) {
                result[j-2] += pow2(j, pos);
            }
        }

        i /= 2;
        pos++;
    }

    return result;
}

unsigned long long* getDivisors(unsigned long long* vec) {
    unsigned long long* result = new unsigned long long[9];
    
    for(int i=0; i<9; i++) {
        result[i] = 0;
        for(unsigned long long j=2, sqI=sqrt(vec[i]); j<sqI; j++) {
            if(vec[i] % j == 0) {
                result[i] = j;
                break;
            }
        }

        if(result[i] == 0) {
            result[0] = 0;
            break;
        }
    }

    return result;
}

int main() {
    int T, N, J, count;
    cin >> T;

    for (int i = 0; i < T; i++) {
        cin >> N >> J;
        cout << "Case #" << (i+1) << ":" << endl;
        count = 0;
        map<unsigned long long, unsigned long long*> m;
        for(int j = pow2(2, N-1)+1, last = pow2(2,N); j<last; j+=2) {
            unsigned long long* vec = getRepresentations(j);
            unsigned long long* divisors = getDivisors(vec);
            if(divisors[0] != 0) {
                count++;
                m[vec[8]] = divisors;

                if(count == J) {
                    for(auto it=m.begin(); it != m.end(); it++) {
                        cout << it->first << " ";
                        for(int l=0; l<8; l++) {
                            cout << it->second[l] << " ";
                        }
                        cout << it->second[8] << endl;
                    }
                }
            } else {
                delete divisors;
            }
            delete vec;
        }
    }
    return 0;
}
