#include <string>
#include <vector>
#include <algorithm>
#include <iostream>
#include <set>
#include <map>
#include <sstream>
#include <queue>
#include <stack>
#include <math.h>
#include <utility>
#include <iterator>
#include <fstream>
#include <stdio.h>
#include <cstring>

using namespace std;

template<class T>
string tostring(T a){stringstream ss; ss<<a; return ss.str();}

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> II;
typedef long long LL;
#define SZ(a) int((a).size()) 
#define PB push_back 
#define ALL(c) (c).begin(),(c).end() 
#define FOR(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
#define LOOP(i,a,b) for((i)=(a);(i)<(b);(i)++)
#define MP(a,b) make_pair((a),(b))
#define LAST(t) (t[SZ(t)-1])



bool pali(LL n){
	string s1=tostring(n);
	string s2=s1;
	reverse(ALL(s1));
	return s1==s2;
}


int main(){
	/*cout<<(LL)sqrt(16)<<endl;
	system("PAUSE");*/

	ifstream be("C-small-attempt0.in");
	ofstream ki("ki.txt");
	int T; be>>T;
	FOR(tt,T){
		LL a,b; be>>a>>b;
		LL ra=sqrt(a), rb=sqrt(b);
		if(ra*ra!=a)
			ra++;

		LL c=0;
		for(LL i=ra; i<=rb; i++){
			if(pali(i) && pali(i*i))
				c++;
		}

		ki<<"Case #"<<tt+1<<": "<<c<<endl;
	}
	
	ki.close();
	return 0;
}