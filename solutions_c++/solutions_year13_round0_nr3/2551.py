#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cctype>
#include <cassert>
#include <iostream>
#include <sstream>
#include <iomanip>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>

#define D(x) cerr << #x << " = " << x << endl
#define REP(i,a,n) for(int i=(a); i<(int)(n); i++)
#define FOREACH(it,v) for(typeof((v).begin()) it=(v).begin(); it!=(v).end(); ++it)
#define ALL(v) (v).begin(), (v).end()

typedef long long int64;

const int INF = (int)(1e9);
const int64 INFLL = (int64)(1e18);
const double EPS = 1e-13;

using namespace std;
const int tSquare = 10000000;
const long long SIZE = 100000000000000;
string convertInt(long long number)
{  stringstream ss;
   ss << number;
   return ss.str();
}
vector<long long> squarePalindromes;

bool isPalindrome(string a){
    int midd = a.size()/2;    
    for(int i=0;i<midd; i++)
        if(a[i] != a[(int)a.size()-1-i])
          return false;
    return true;
}

bool isPalindromeSquare(long n, long square){
  string sn = convertInt(n);
  string sSquare = convertInt(square);  
  
  return isPalindrome(sn) && isPalindrome(sSquare);
}

int main() {
  ios_base::sync_with_stdio(false);
  freopen("c.in","r",stdin);
  freopen("c.out","w",stdout);
  
  
  for(long long i=1; i<=tSquare;i++){
    long long square = i*i;
    
    if(isPalindromeSquare(i,square)){
      squarePalindromes.push_back(square);
      //cout << square << endl;
    }
  }
  
  int t;
  cin >> t;
  for(int k=1;k<=t;k++){
    long long a,b;
    cin >> a >> b;
    int ans = 0;
    for(int i=0; i<(int)squarePalindromes.size(); i++){
        //cout << squares[i] << " "<< squarePalindromes[i] <<endl;
        if(a <= squarePalindromes[i] && squarePalindromes[i] <= b)
          ans++;
    }
    cout << "Case #"<<k<<": "<<ans<<endl;
  }
  
  
  
  
  return 0;
}
