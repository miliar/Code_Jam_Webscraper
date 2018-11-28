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
#include <cstdio>
#include <functional>

using namespace std;

template<class T>
string tostring(T a){stringstream ss; ss<<a; return ss.str();}

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int,int> II;
#define SZ(a) int((a).size()) 
#define PB push_back 
#define ALL(c) (c).begin(),(c).end() 
#define FOR(i,n) for(int (i)=0;(i)<(int)(n);(i)++)
#define LOOP(i,a,b) for((i)=(a);(i)<(b);(i)++)
#define MP(a,b) make_pair((a),(b))
#define LAST(t) (t[SZ(t)-1])

int main(){
	ifstream be("B-small-attempt0.in");
	ofstream ki("ki.txt");
	int T;
	be>>T;
	FOR(tt,T){
		int n,p; be>>n>>p;
		//bool bok1=true, bok2=true;
		int ki1, ki2;
		FOR(i,1<<n){
			//legrosszabb esetben hol lesz
			{
				int a=i;
				int c=0; //hany jatszmat sikerult elveszteni
				while(a>0){
					c++;
					a=(a-1)/2;
				}
				bool ok1 = (1<<n)-(1<<(n-c))+1 <= p;
				/*if(bok1 && !ok1){
					bok1=false;
					ki1=i-1;
				}*/
				if(ok1)
					ki1=i;
			}

			//legjobb esetben hol lesz
			{
				int a=(1<<n)-i-1; //ell!!!
				int c=0; //hany jatszmat sikerult megnyerni
				while(a>0){
					c++;
					a=(a-1)/2;
				}
				bool ok2 = (1<<(n-c)) <= p; //could win a prize
				/*if(bok2 && !ok2){
					bok2=false;
					ki2=(1<<n)-i-1;
				}*/
				if(ok2)
					ki2=(1<<n)-i-1;
			}
		}

		////todo: meg le kell kezelni azokat az eseteket, amikor az utolso
		////cikluslefutasnal is teljesult
		ki<<"Case #"<<tt+1<<": "<<ki1<<" "<<((1<<n)-ki2-1)<<endl;
	}
	

	ki.close();
	return 0;
}