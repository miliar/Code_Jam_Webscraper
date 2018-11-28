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
string s1,s2;
int l1,l2;
int n;
inline void read(){
    cin>>n;
    cin>>s1>>s2;
    l1 = LN(s1),l2 = LN(s2);
}
int dp[105][105];

int go(int i, int j){
    if(i>=l1 || j>=l2 ){
        return (i<l1 || j<l2 ? 1023456789 : 0);
    }
    int &bst = dp[i][j];
    if(bst!=-1)return bst;

    bst = 1023456789;
    if( s1[i]==s2[j] ){
        //do nothing
        bst = min( bst, go(i+1,j+1));

        //increate s1
        if( i+1<l1 && s1[i]==s1[i+1] ){
            bst = min(bst, go(i+2,j+1)+1 );
        }
        //increase s2
        if( j+1<l2 && s2[j]==s2[j+1] ){
            bst = min(bst, go(i+1,j+2)+1 );
        }
    }
    //consume s1
    if( i+1<l1 && s1[i]==s1[i+1] ){
        bst = min(bst, go(i+1,j)+1 );
    }
    //consume s2
    if( j+1<l2 && s2[j]==s2[j+1] ){
        bst = min(bst, go(i,j+1)+1 );
    }
    return bst;
}
inline void proc(){
    SET(dp,-1);
    int val = go(0,0);
    if(val>=1023456789){
        cout<<"Fegla Won\n";
    }else{
        cout<<val<<"\n";
    }
}
int main() {
        int kase = 1;
#if defined( xerxes_pc )
        if (!freopen("in1", "r", stdin))
                puts("error opening file in "), assert(0);
        kase = 1;
#endif
        kase = fastIn<int>();
        fo(i,kase){
                read();
                cout<<"Case #"<<i+1<<": ";
                proc();
        }
        return 0;
}