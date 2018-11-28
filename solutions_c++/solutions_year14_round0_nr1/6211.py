/*
 * 	Author : Pallab
 * 
 * "I have not failed, I have just found 10000 ways that won't work."
*/
#include <iostream>
#include <algorithm>
#include <vector>
#include <sstream>
#include <fstream>
#include <string>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <numeric>
#include <stack>
#include <functional>
#include <bitset>
#include <iomanip>

#include <ctime>
#include <cassert>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <climits>
#include <cstring>
#include <cstdlib>

using namespace std;

#define foR(i1,st,ed) for(int i1 = st , j1 = ed ; i1 < j1 ; ++i1 )
#define fo(i1,ed) foR( i1 , 0 , ed )
#define foE(i1,st,ed) foR( i1, st, ed+1 )
#define foit(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define bip system("pause")
#define Int long long
#define pb push_back
#define SZ(X) (int)(X).size()
#define LN(X) (int)(X).length()
#define mk make_pair
#define SET( ARRAY , VALUE ) memset( ARRAY , VALUE , sizeof(ARRAY) )
#define line puts("")

inline void wait(double seconds) {
        double endtime = clock() + (seconds * CLOCKS_PER_SEC);
        while (clock() < endtime) {
                ;
        }
}
template<class T>
inline T fastIn() {
    register char c=0;
    register T a=0;
    bool neg=false;
    while(c<33)c=getchar();
    while(c>33) {
        if(c=='-') {
            neg=true;
        } else {
            a= (a*10)+(c-'0');
        }
        c=getchar();
    }
    return neg?-a:a;
}

int one[10][10];
int two[10][10];
int oneRow,twoRow;

inline void read(){
	set<int> got;
	oneRow =fastIn<int>();
	foR(i,0,4){
		foR(j,0,4){
			int const tmp =fastIn<int>();
			if(i+1==oneRow){
				got.insert(tmp);
			}
		}
	}
	twoRow =fastIn<int>();
	set<int> match;
	foR(i,0,4){
		foR(j,0,4){
			int const tmp = fastIn<int>();
			if(i+1==twoRow){
				if( got.find(tmp) != got.end() ){
					match.insert(tmp);
				}
			}
		}
	}
	if(SZ(match) ==1 ){
		cout<<(*match.begin())<<"\n";
	}else{
		if(SZ(match)>1 ){
			cout<<"Bad magician!\n";
		}else{
			cout<<"Volunteer cheated!\n";
		}
	}

}
inline void proc(){}
int main() {
        int kase = 1;
#if defined( xerxes_pc )
        if (!freopen("in1", "r", stdin))
                puts("error opening file in "), assert(0);
        kase = 1;
#endif
        kase = fastIn<int>();
        fo(i,kase){
        		cout<<"Case #"<<i+1<<": ";
                read();
                proc();
        }
        return 0;
}