#include <iostream>
#include <stdio.h>
#include <string>
#include <bitset>
#include <math.h>
#include <stdlib.h>

using namespace std;

long long getDenominator(long long number);
long long convertBase(long long n, string binary);

int main() {
    freopen("C-small-attempt0.in","rt",stdin);
	freopen("C-small-attempt0.out","wt",stdout);
    int T;
	scanf("%d",&T);
    int input [T][2];
    bool stop = false;

    for (int i=0; i<T; i++) {
        cin >> input[i][0]; // length
        cin >> input[i][1]; // number of
        int maxnum = 65535;
        long long result[9];
        int resultSize = 0;
        string resultBinary[input[i][1]];

        cout << "Case #" << i+1 << ":" << endl;

        for (int j=1; j<=maxnum; j++) {
            if (resultSize < input[i][1]) {
                int num = j;
                bitset<16> bin(num);
                string bits = bin.to_string();
                if (bits.at(0) == '1' && bits.at(bits.length()-1) == '1') {
                    long long bin2 = convertBase(2, bits);
                    long long bin3 = convertBase(3, bits);
                    long long bin4 = convertBase(4, bits);
                    long long bin5 = convertBase(5, bits);
                    long long bin6 = convertBase(6, bits);
                    long long bin7 = convertBase(7, bits);
                    long long bin8 = convertBase(8, bits);
                    long long bin9 = convertBase(9, bits);
                    long long bin10 = convertBase(10, bits);
                    bool yes = false;

                    resultBinary[resultSize] = bits;
                    long long den2 = getDenominator(bin2);
                    if (den2 != -1) {
                        result[0] = den2;
                        // cout << "ok1" << endl;

                        long long den3 = getDenominator(bin3);
                        if (den3 != -1) {
                            result[1] = den3;
                            // cout << "ok" << endl;

                            long long den4 = getDenominator(bin4);
                            if (den4 != -1) {
                                result[2] = den4;
                                // cout << "ok" << endl;

                                long long den5 = getDenominator(bin5);
                                if (den5 != -1) {
                                    result[3] = den5;
                                    // cout << "ok" << endl;

                                    // cout << "bin6 " << bin6 << endl;
                                    long long den6 = getDenominator(bin6);
                                    // cout << "den6 " << den6 << endl;
                                    if (den6 != -1) {
                                        result[4] = den6;
                                        // cout << "ok" << endl;

                                        // cout << "bin7 " << bin7 << endl;
                                        long long den7 = getDenominator(bin7);
                                        if (den7 != -1) {
                                            result[5] = den7;
                                            // cout << "ok" << endl;

                                            // cout << "bin8 " << bin8 << endl;
                                            long long den8 = getDenominator(bin8);
                                            if (den8 != -1) {
                                                result[6] = den8;
                                                // cout << "ok" << endl;

                                                // cout << "bin9 " << bin9 << endl;
                                                long long den9 = getDenominator(bin9);
                                                if (den9 != -1) {
                                                    result[7] = den9;
                                                    // cout << "ok" << endl;

                                                    // cout << "bin10 " << bin10 << endl;
                                                    long long den10 = getDenominator(bin10);
                                                    if (den10 != -1) {
                                                        result[8] = den10;
                                                        // cout << "ok" << endl;

                                                        yes = true;
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }

                    if (yes) {
                        cout << resultBinary[resultSize] << " ";
                        printf("%lld %lld %lld %lld %lld %lld %lld %lld %lld\n", result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7], result[8]);
                        resultSize++;
                    }
                    }
                }
            }
        }

    return 0;
}

long long convertBase(long long n, string binary) {
    long long decimal = 0;
    long long iter = 0;
    switch(n) {
        case 2:
            for (long long i=binary.length()-1; i>=0; i--) {
                char c = binary.at(i);
                if (c == '1') {
                    decimal += pow(2,iter);
                }
                iter++;
            }
            return decimal;
            break;
        case 3:
            for (long long i=binary.length()-1; i>=0; i--) {
                char c = binary.at(i);
                if (c == '1') {
                    decimal += pow(3,iter);
                }
                iter++;
            }
            return decimal;
            break;
        case 4:
            for (long long i=binary.length()-1; i>=0; i--) {
                char c = binary.at(i);
                if (c == '1') {
                    decimal += pow(4,iter);
                }
                iter++;
            }
            return decimal;
            break;
        case 5:
            for (long long i=binary.length()-1; i>=0; i--) {
                char c = binary.at(i);
                if (c == '1') {
                    decimal += pow(5,iter);
                }
                iter++;
            }
            return decimal;
            break;
        case 6:
            for (long long i=binary.length()-1; i>=0; i--) {
                char c = binary.at(i);
                if (c == '1') {
                    decimal += pow(6,iter);
                }
                iter++;
            }
            return decimal;
            break;
        case 7:
            for (long long i=binary.length()-1; i>=0; i--) {
                char c = binary.at(i);
                if (c == '1') {
                    decimal += pow(7,iter);
                }
                iter++;
            }
            return decimal;
            break;
        case 8:
            for (long long i=binary.length()-1; i>=0; i--) {
                char c = binary.at(i);
                if (c == '1') {
                    decimal += pow(8,iter);
                }
                iter++;
            }
            return decimal;
            break;
        case 9:
            for (long long i=binary.length()-1; i>=0; i--) {
                char c = binary.at(i);
                if (c == '1') {
                    decimal += pow(9,iter);
                }
                iter++;
            }
            return decimal;
            break;
        case 10:
            for (long long i=binary.length()-1; i>=0; i--) {
                char c = binary.at(i);
                if (c == '1') {
                    decimal += pow(10,iter);
                }
                iter++;
            }
            return decimal;
            break;
        default:
            decimal = -1;
            cout << decimal << endl;
            break;
    }
}

long long getDenominator(long long number) {
    long long tgh = ceil(sqrt(number));
    for (long long i=2; i<tgh; i++) {
        // printf("akisu: %lld\n",i);
        if (number % i == 0) {
            return i;
        }
    }
    return -1;
}
