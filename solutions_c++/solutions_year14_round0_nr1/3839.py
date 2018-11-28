#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <iostream>
#include <iterator>
#include <string>
#include <algorithm>

#include <vector>
#include <list>
#include <queue>
#include <map>
#include <set>

using namespace std;

#define PB push_back
#define whole(v) v.begin(), v.end()
#define FOR(i,a,b) for(int i=a ; i<b ; i++)
#define FORE(i,n) FOR(i,0,n)

typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<char> vc;
typedef vector<unsigned> vu;
typedef vector<long> vl;
typedef vector<int>::iterator vii;
typedef vector<double>::iterator vdi;
typedef vector<char>::iterator vci;
typedef vector<unsigned>::iterator vui;
typedef vector<long>::iterator vli;

typedef unsigned long long ull;

template<class Container>
void print(const Container& c) {
#ifdef Cpp11
    for (auto const &item : c)
        cout << item << endl;
#else
    copy(whole(c), ostream_iterator<typename Container::value_type > (cout, "\n"));
#endif
}

// function prototypes

int main(int argc, char** argv) {
    unsigned T, a1, a2;
    cin >> T;
    
    vu v1, v2;
    
    unsigned x1,x2,x3,x4;
    FORE(i, T){
        // read answer 1
        cin >> a1;
        
        FORE(j, 4){     // each row
            cin >> x1 >> x2 >> x3 >> x4;    
            if(j == a1-1){
                v1.PB(x1);
                v1.PB(x2);
                v1.PB(x3);
                v1.PB(x4);
            }
        }
        
        // read answer 2
        cin >> a2;
        FORE(j, 4){     // each row
            cin >> x1 >> x2 >> x3 >> x4;    
            if(j == a2-1){
                v2.PB(x1);
                v2.PB(x2);
                v2.PB(x3);
                v2.PB(x4);
            }
        }
        
        /*cout << "a1 = " << a1 << "\t a2 = " << a2 << endl;
        cout << "v1:" << endl;
        print(v1);
        cout << endl << "v2:" << endl;
        print(v2);
        cout << endl;*/
        
        int found = 1;
        unsigned card;
        FORE(j, 4){
            FORE(k, 4){
                if(v1[j] == v2[k]){
                    card = v1[j];
                    found--;
                    break;
                }
            }
        }
        
        cout << "Case #" << i+1 << ": ";
        if(found < 0){
            cout << "Bad magician!"; 
        }
        else if (found == 1){
            cout << "Volunteer cheated!";
        }
        else if (found == 0){
            cout << card;
        }
        
        cout << endl;
        v1.clear();
        v2.clear();
        
    }


    return 0;
}
