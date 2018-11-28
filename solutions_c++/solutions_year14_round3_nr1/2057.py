#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cctype>
#include<cstring>
#include<vector>
#include<list>
#include<queue>
#include<deque>
#include<stack>
#include<set>
#include<utility>
#include<algorithm>
#include<map>
#include<numeric>
#include<limits>
#include<iomanip>
#include<fstream>
// for print binary 
// char a = -58; bitset<8> x(a); cout<< x;
#include<bitset>
// to use limit -> numeric_limits<type>::max()
// to set precision after decimal point -->  cout.setf(ios::fixed,ios::floatfield);
using namespace std;

template <typename T, size_t N>
T* begin(T(&arr)[N]) { return &arr[0]; }
template <typename T, size_t N>
T* end(T(&arr)[N]) { return &arr[0]+N; }

typedef pair<int,int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
// initialise -> VVI a(size,VI(subsize,0));
typedef vector<vector<int> > VVI;
typedef vector<double> VD;

#define IFOR(i, a, b) for(int i = (a); i < (b); ++i)
#define DFOR(i, a, b) for(int i = (a)-1; i>=(b);--i)
#define EFOR(i, a, b) for(int i = (a); i <= (b); ++i)
#define RESET(a, b) memset(a, b, sizeof(a))
// for sorting --> sort(ALL(a))
#define ALL(a) (a).begin(), (a).end()
#define PB push_back
#define MP make_pair
#define REVERSE_INT greater<int>()


int main(){
  // loading all primes
  long long primes[1000000];
  ifstream pfile;
  pfile.open("primes.txt");
  long long num_prime = 0;
  while(!pfile.eof()){
    long long val=0;
    pfile>>val;
    if(val>1000000) break;
    primes[num_prime++]=val;
  }
  // create power of 2 lists
  long long twos[41] = {1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768,65536,131072,262144,524288,1048576,2097152,4194304,8388608,16777216,33554432,67108864,134217728,268435456,536870912,1073741824,2147483648,4294967296,8589934592,17179869184,34359738368,68719476736,137438953472,274877906944LL,549755813888LL,1099511627776LL};

  int T;
  cin>>T;
  IFOR(t, 0, T){
    // get inputs
    int a,b;cin>>a>>b;      
    //cout<< "My Elf: "<<a<<" "<<b<<endl; 
    // solution
    // find common factors
    IFOR(i,0,num_prime){
      if(primes[i]>a) break;
      while(true){
        if(a%primes[i]==0 && b%primes[i]==0){
          a/=primes[i]; b/=primes[i];
        }else{
          break;
        }
      }
    }
    // check if b is not in the list
    bool correctb=false;
    IFOR(i,0,41){
      if(b==twos[i]){
        correctb=true;
      }
    }
    if(!correctb) {
      cout<< "Case #"<<t+1<<": impossible\n";
      continue;
    }

    // find elf
    int curElf=a;
    int elfGen=-1;
    IFOR(i, 0, 40){
      curElf*=2;
      if(curElf>=b){
        elfGen = i+1;
        break;
      }
    }
    // print answers
    if(elfGen!=-1)
      cout<< "Case #"<<t+1<<": "<< elfGen <<"\n";
    else 
      cout<< "Case #"<<t+1<<": impossible\n";
  }


  return 0;
}
