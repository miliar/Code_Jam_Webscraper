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
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

#define _f(i,x,n) for(int i=x;i<n;i++)
#define _if(i,x,n) for(int i=(n);i>=x;i++)
#define _fv(it,v) for(typeof((v).begin()) it=(v).begin(); it!=(v).end(); it++)

#define _d(var) cout<<"L"<<__LINE__<<": "<<#var<<": "<<var<<endl;
#define _dv(v) cout<<"L"<<__LINE__<<": "<<#v<<": "; di((v).begin(),(v).end());
#define _dvf(v) cout<<"L"<<__LINE__<<": "<<#v<<": "; di((v).begin(),(v).end()); *************************
template<typename it> void di(it i,it f) { cout<<"[ "; while(i!=f) cout<<*(i++)<<" "; cout<<"]"<<endl; }
template<typename it> void dif(it i,it f,string ) { cout<<"[ "; while(i!=f) cout<<*(i++)<<" "; cout<<"]"<<endl; }
#define _ln cout<<"_ln: "<<__LINE__<<endl;

template<class Origen,class Destino> Destino convertir(Origen entrada)
	{ stringstream flujo; flujo<<entrada; Destino salida; flujo>>salida; return salida; }

set<long long> palindromes;
set<long long> res;
long long limit = pow(10,7);

bool isPalindrome(long long n){
	string ns = convertir<long long,string>(n);
	_f(i, 0, ns.length() / 2)
		if(ns[i] != ns[ns.length() - i - 1])
			return false;
	return true;
}

int searchPalindromes(long long a, long long b){
  long long res = 0;
  long long sqb = sqrt(b);
	for(long long i=sqrt(a); i<=sqb; i++){
		if(isPalindrome(i)){
      if(i <= limit){
        long long p = i*i;
        if(a <= p && p <= b && isPalindrome(p)){
          res++;
        }
        else if(p > b)
          break;
      }
		}
	}
  return res;
}

int main(){
    int T;
    cin>>T;
    _f(tt,1,T+1){
        long long a, b;
        cin>>a>>b;
        cout<<"Case #"<<tt<<": "<<searchPalindromes(a,b)<<endl;
    }
    return 0;
}
