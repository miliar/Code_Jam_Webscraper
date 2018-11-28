#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <set>
#include <cmath>
#include <sstream>
#include <utility>
#include <cctype>
#include <numeric>
#include <queue>
#include <deque>
#include <list>
#include <stack>
#include <bitset>
#include <limits>
#include <ctime>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <functional>
using namespace std;
#define REP(i,n)    for(int i=1;i<=(n);++i)
#define FOR(n)    for(int i=1;i<(n);++i)
#define FORE(i,e,n) for(int i=(e);i<(n);++i)

#define out(v) cout<<(v)<<endl
#define _(A,v) memset(A,v,sizeof(A))
#define all(A)  (A).begin(), (A).end()
#define rall(A) (A).rbegin(),(A).rend()
#define pb push_back
#define             incontainer(c,x)            ( (c).find(x) != (c).end() )
# define nodo pair <int,int>

#define MAX 10000
#define LMT 100
/*
unsigned flag[MAX>>6];
//vector<int>primos;
string mov="";
#define ifc(x) (flag[x>>6]&(1<<((x>>1)&31)))
#define isc(x) (flag[x>>6]|=(1<<((x>>1)&31)))

void sieve1()
{
	int i, j, k;
	for(i=3; i<LMT; i+=2)
		if(!ifc(i))
			for(j=i*i,k=i<<1; j<MAX; j+=k)
				isc(j);

	for(i=3; i<MAX; i+=2){
		if(!ifc(i)){
			cout<<i<<endl;
		}
	}
}*/

bool numArr [1001]= {0};

string tostring( int a ) {
    stringstream ss;
    ss<<a;
    return ss.str();
}


bool isPalindrome(int num) {
    string numString= tostring(num);
    string prueba="";
    for(int j=numString.size()-1; j>=0; j--) {
        prueba+=numString[j];
    }
    if(prueba==numString) return true;
    return false;
}

void findPalSq() {
    for(int i=1; i<=1000; i++) {
        if(isPalindrome(i)) {
            double sq= sqrt(i+0.0);
            if(fmod((i+0.0),sq) ==0) {
                if(isPalindrome(sq)) {
                    numArr[i]=1;
                }
            }
        }
    }
}

int main() {

    /*freopen("d.in",  "r", stdin);
    freopen("d.out", "w", stdout);*/
    int T;
    cin>>T;
    findPalSq();
    for( int cases =1; cases<=T; cases++) {
        cout<<"Case #"<<cases<<": ";
        int a,b,sum=0;
        cin>>a>>b;
        for(a; a<=b; a++) {
            if(numArr[a]){ sum++;}
        }
        cout<<sum;
        if(cases!=T)cout<<endl;
    }

    return 0;
}
