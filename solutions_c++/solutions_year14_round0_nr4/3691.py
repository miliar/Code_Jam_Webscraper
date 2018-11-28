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

int countWar(vd, vd);
int countDecWar(vd, vd);

int main(int argc, char** argv) {

    int T;
    cin >> T;
    
    
    
    FORE(i, T){
        int N;
        cin >> N;
        vd naomi, ken;
        FORE(j, N){
            double d;
            cin >> d;
            naomi.PB(d);
        }
        FORE(j, N){
            double d;
            cin >> d;
            ken.PB(d);
        }
        
        sort(whole(naomi));
        sort(whole(ken));
        
        int war = 0, decwar = 0;        
        decwar = countDecWar(naomi, ken);
        
        
        reverse(whole(naomi));
        reverse(whole(ken));
        war = countWar(naomi, ken);
        
        
        
        cout << "Case #" << i+1 << ": " << decwar << " " << war << endl;
    }

    return 0;
}

int countWar(vd naomi, vd ken){
    int war = 0;
    while(naomi.empty() == false){
            
        /*cout << endl << "===========" << endl;

        print(naomi);
        cout << endl;
        print(ken);*/

        if(naomi.front() > ken.front()){
            war++;
            naomi.erase(naomi.begin());
            ken.erase(ken.end()-1);
        }
        else{
            vdi it = ken.begin();
            while(*it > naomi.front() && it != ken.end()){
                it++;
            }
            it--;
            naomi.erase(naomi.begin());
            ken.erase(it);
        }
    }
    return war;
}

int countDecWar(vd naomi, vd ken){
    int decwar = 0;
    /*cout << endl << "===========" << endl;

    print(naomi);
    cout << endl;
    print(ken);*/
    
    while(ken.empty() == false){
        vdi it = naomi.begin();
        while(ken.front() > *it && it != naomi.end()){
            it++;
        }
        if(it != naomi.end()){
            decwar++;
            ken.erase(ken.begin());
            naomi.erase(it);
        }
        else{
            ken.erase(ken.begin());
            naomi.erase(naomi.begin());
        }
        
    }
    
    
    return decwar;
}