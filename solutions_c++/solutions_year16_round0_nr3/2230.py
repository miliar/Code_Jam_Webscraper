/* @coder: Sidharth Gupta */

#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <string>
#include <cassert>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>


#define MOD 109546051211ll
#define MIN(a,b) ((a)>(b)?(b):(a))
#define MAX(a,b) ((a)>(b)?(a):(b))
#define ABS(a) MAX(a,-(a))
#define SET(a,b) memset(a, b, sizeof(a))
#define EVEN(a) ((a&1)==0)
#define SQR(a) ((a)*(a))
#define EPS 0.0001

typedef long long int lli;
typedef unsigned long long int llui;
typedef unsigned int uint;

using namespace std;

lli multipliers[50][505] = {0};
string multiplicands[50][505];
int multipliersSz = 500;
int multiplicandsSz = 500;
int tot = 0;

int genMultiplicands(int numOfDigits, int minGap) {
    int i=0;
    int gap = minGap;
    int arr[50];

    while(gap <= (numOfDigits-2)/2) {
        SET(arr, 0);
        int start = gap + 2;
        int stop = numOfDigits - gap - 1;
        int numOfOnes = (stop - start) / (gap+1);

        arr[1] = arr[numOfDigits] = 1;

        for(int s = start; s < start + numOfOnes; ++s) {
            arr[s] = 1;
        }

        do {
            int indx = start;
            bool valid = true;
            while(1) {
                while(indx <= stop && arr[indx] == 0) {
                    ++indx;
                }
                if(indx > stop) {
                    break;
                }
                int prevOne = indx;
                ++indx;
                while(indx <= stop && arr[indx] == 0) {
                    ++indx;
                }
                if(indx > stop) {
                    break;
                }
                int nextOne = indx;
                if(nextOne - prevOne < gap + 1) {
                    valid = false;
                    break;
                }
            }
            if(valid) {
                char str[50];
                SET(str, 0);
                for(int s=1;s<=numOfDigits;++s) {
                    if(arr[s] == 0) {
                        str[s-1] = '0';
                    } else {
                        str[s-1] = '1';
                    }
                }

                multiplicands[numOfDigits][i] = str;
                ++i;
            }
        } while ( std::prev_permutation(arr+start,arr+stop+1) );
        ++gap;
    }
    return i;
}

int genMultipliers(int numOfDigits) {

    int i=0;
    if(numOfDigits == 2) {
        multipliers[numOfDigits][i] = 11ll;
        return 1;
    }

    lli mask = 1ll<<((lli)(numOfDigits-2));

    for(lli m = 0; m < mask; ++m) {
        lli multiplier = 10ll;
        lli temp = m;
        for(int d = 0; d < numOfDigits-2; ++d) {
            if(EVEN(temp)) {
                multiplier += 1ll;
            }
            multiplier *= 10ll;
            temp >>= 1;
        }
        multiplier += 1ll;
        multipliers[numOfDigits][i] = multiplier;
        ++i;
        if(multipliersSz == i) {
            break;
        }
    }
    return i;
}

string add(string a, string b) {
    string c(a);

    int alen = a.length();
    int blen = b.length();

    for(int i=alen-1, j=blen-1; i>=0 && j>=0; --i, --j) {
        if(c[i] == '1' && b[j] == '1') {
            system("pause");
        } else if(c[i] == '0' && b[j] == '1') {
            c[i] = '1';
        }
    }

    return c;
}

int main() {

    int cnt = 0;

    for(int i = 2; i <= 16; ++i) {
        int x = genMultipliers(i);
        int y = genMultiplicands(33-i, i-1);

        map<string, int> mp;
        for(int yindx = 0; yindx < y; ++yindx) {
            mp.insert(make_pair(multiplicands[33-i][yindx],1));
        }


        cout << "Case #1:" << endl;
        for(map<string,int>::iterator it = mp.begin(); it != mp.end(); ++it) {
            for(int xindx = 0; xindx < x; ++xindx) {
//                cout << it->first << " " << multipliers[i][xindx] << endl;
                string str = it->first + "0";
                cout << add(str, it->first) << " 3 4 5 6 7 8 9 10 11";
                cnt++;
                if(cnt != 500) cout << endl;
                if(cnt == 500) break;
            }
            if(cnt == 500) break;
        }
//
//        tot += x*(mp.size());
//        if(tot >= 50) {
//            break;
//        }
        if(cnt == 500) break;
    }

    //cout << tot;

    return 0;
}
