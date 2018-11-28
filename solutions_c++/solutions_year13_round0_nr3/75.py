// compile with "g++ XXX.cc -mno-cygwin -O2" in Cygwin

#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstdarg>
#include<cstring>
#include<algorithm>
#include<string>
#include<vector>
#include<cmath>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<numeric>
#include<functional>
#include<complex>
#include<bitset>

using namespace std;
#define BET(a,b,c) ((a)<=(b)&&(b)<(c))
#define FOR(i,n) for(int i=0,i##_end=(int(n));i<i##_end;i++)
#define FOR3(i,a,b) for(int i=a,i##_end=b;i<i##_end;i++)
#define FOR_EACH(it,v) for(__typeof(v.begin()) it=v.begin(),it_end=v.end() ; it != it_end ; it++)
#define SZ(x) (int)(x.size())
#define ALL(x) (x).begin(),(x).end()
#define MP make_pair
#define CLS(x,val) memset((x) , val , sizeof(x)) 
typedef long long ll_t;
typedef long double ld_t;
typedef vector<int> VI; 
typedef vector<VI> VVI;
typedef complex<int> xy_t;

template<typename T> void debug(T v , string delimiter = "\n")
{ for(__typeof(v.begin()) it=v.begin(),it_end=v.end() ; it != it_end ; it++) cout << *it << delimiter; cout << flush ;}

int dx[]  = {0,1,0,-1};
int dy[]  = {1,0,-1,0};
string ds = "SENW";

#define DIGIT 300 
#define ONE_LENGTH 9
#define MAX_LENGTH (DIGIT/ONE_LENGTH+2)
#define ONE_MAX (1000000000)
#define BUFSIZE 256

class big_int
{
  int body[MAX_LENGTH];
  int& operator[](const int index){return body[index];}
  const int& operator[](const int index) const {return body[index];}
  int last()
  {
    int i;
    for(i = MAX_LENGTH-1 ; i >= 0 ; i--)
      if(body[i])break;
    return i+1;
  }
public:
  big_int(long long n=0)
  {
    fill(body,body+MAX_LENGTH,0);
    for(int i = 0 ; n ; i++ , n/= ONE_MAX)
      body[i] = n%ONE_MAX;
  }
  big_int(const big_int& a)
  {
    copy(a.body,a.body+MAX_LENGTH,body);
  }
  big_int(string str)
  {
    string::reverse_iterator p=str.rbegin(),end=str.rend();
    fill(body,body+MAX_LENGTH,0);
    for(int i = 0 ; p != end ; i++)
      for(int j = 0,t=1 ; j < ONE_LENGTH && p != end ; j++,p++,t*=10)
        body[i]  += (*p - '0')*t;
  }
  void operator=(const big_int& b)
{copy(b.body,b.body+MAX_LENGTH,this->body);}
  int compare(const big_int& a) const
  {
    for(int i = MAX_LENGTH-1 ; i >= 0 ; i--)
      if(body[i] > a[i])return 1;
      else if(body[i] < a[i])return -1;
    return 0;
  }
#define DEF_COMP(op) \
  friend bool operator op (const big_int& r1 , const big_int& r2) { return r1.compare(r2) op 0 ; } 
  DEF_COMP(==) DEF_COMP(!=) DEF_COMP(>=) DEF_COMP(<=) DEF_COMP(>) DEF_COMP(<) 
#undef DEF_COMP

  string toString()
  {
    string str("");
    char buf[BUFSIZE];
    int i = last()-1;
    if(i==-1)return string("0");
    sprintf(buf,"%d",body[i]);
    str += buf;
    while(--i >= 0)
      {
	sprintf(buf,"%0*d", ONE_LENGTH ,body[i]);
	str+= buf;
      }
    return str;
  }
  friend int DivMod(big_int a,int b,big_int& c)
  {
    long long rem=0;
    for(int i = a.last()-1 ; i >= 0 ; i--)
      {
	long long d = a[i]+rem;
	c[i] = d/b;
	rem = d%b;
	if(i)rem *= ONE_MAX;
      }
    return (int)rem;
  }
  friend big_int DivMod(big_int a,big_int b,big_int& c)
  {
    c = big_int();
    while(a>=b)
      {
	big_int tmp(1),d(b);
	for(int i = 0 ; a>=d ; i++){ d = d<<1; tmp = tmp<<1; }
	d = d>>1; tmp = tmp>>1;
	while(a >= d) { d = d*10; tmp = tmp*10; }
	d = d/10; tmp = tmp/10;
	while(a >= d) { c = c+tmp; a = a-d;}
      }
    return a;
  }
  friend istream& operator>>(istream& is,big_int& a)
  {
    string str;
    is >> str;
    a = big_int(str);
    return is;
  }
  friend ostream& operator<<(ostream& os,big_int a)
  {
    return os << a.toString();
  }
  friend big_int operator>>(big_int a,int n)
  {
    for(int i = 0 ; i < MAX_LENGTH-n ; i++) a[i] = (i+n<MAX_LENGTH)?a[i+n]:0;
    return a;
  }
  friend big_int operator<<(big_int a,int n)
  {
    for(int i = MAX_LENGTH-1 ; i >= 0 ; i--) a[i] = (i-n>=0)?a[i-n]:0;
    return a;
  }
  friend big_int operator+(big_int a,big_int b)
  {
    long long carry=0;
    for(int i = 0 ; i < MAX_LENGTH ; i++)
      {
	a[i] += b[i]+carry;
	carry = a[i]/ONE_MAX;
	a[i] %= ONE_MAX;
      }
    return a;
  }
  friend big_int operator-(big_int a,big_int b)
  {
    long long borrow=0;
    for(int i = 0 ; i < MAX_LENGTH ; i++)
      {
	a[i] -= b[i]+borrow;
	if(a[i] >= 0)borrow = 0;
	else
	  {
	    a[i] += ONE_MAX;
	    borrow = 1;
	  }
      }
    return a;
  }
  friend big_int operator*(big_int a,long long b)
  {
    long long carry=0;
    for(int i = 0 ; i < MAX_LENGTH ; i++)
      {
	long long tmp = a[i]*b + carry;
	a[i] = tmp%ONE_MAX;
	carry = tmp/ONE_MAX;
      }
    return a;
  }
  friend big_int operator*(big_int a,big_int b)
  {
    big_int c;
    for(int i = MAX_LENGTH-1 ; i >= 0 ; i--)
      {
        c = (c<<1) + (a*b[i]);
      }
    return c;
  }
  template<typename T>
  friend big_int operator/(big_int a,T b)
  {
    big_int c;
    (void)DivMod(a,b,c);
    return c;
  }
  template<typename T>
  friend T operator%(big_int a,T b)
  {
    big_int c;
    return DivMod(a,b,c);
  }
  friend big_int operator^(big_int a,int b)
  {
    big_int ans(1);
    if(b > 0)
      {
	if(b&1)ans = a;
	ans = ans * ((a*a)^(b>>1));
      }
    return ans;
  }
};

string format(const char* format, ...)
{
  char buf[10000];
  va_list ap;
  va_start(ap, format);
  vsprintf(buf, format, ap);
  va_end(ap);
  return buf;
}

bool isPalindrome(ll_t x)
{
  string s = format("%lld",x);
  for(int i=0,j=SZ(s)-1;i<=j;i++,j--) {
    if(s[i] != s[j]) return false;
  }
  return true;
}

vector<big_int> fairAndSquares;

set<string> memo;

void initFairAndSquareNumbers()
{
  queue<string> qu;
  qu.push("1");
  qu.push("2");
  qu.push("3");
  qu.push("11");
  qu.push("22");
  qu.push("111");
  qu.push("121");
  qu.push("212");
  qu.push("1111");
  qu.push("11111");
  qu.push("11211");
  qu.push("111111");
  qu.push("1111111");
  qu.push("11111111");
  qu.push("111111111");
  while(!qu.empty()){
    string now = qu.front(); qu.pop();
    if(SZ(now) >= 55) continue;
    if(memo.count(now)) continue;
    memo.insert(now);
    //cout<<" "<<now<<endl;
    FOR(i,(SZ(now))/2){
      string next = now;
      int insert1 = i + 1;
      int insert2 = (SZ(now) - i) - 1;
      next.insert(insert2, "0");
      if(insert1 == insert2)
        qu.push(next);
      next.insert(insert1, "0");
      qu.push(next);
    }
  }
  FOR_EACH(it , memo){
    big_int b(*it);
    fairAndSquares.push_back(b * b);
  }
  sort(ALL(fairAndSquares));
  //FOR(i,SZ(fairAndSquares)) cout<<fairAndSquares[i]<<endl;
  //cout<<SZ(fairAndSquares.back().toString())<<" "<<fairAndSquares.back()<<endl;
}

ll_t solve()
{
  string sA,sB;
  cin>>sA>>sB;
  big_int A(sA) , B(sB);

  vector<big_int>::iterator p1,p2;

  p1 = lower_bound(ALL(fairAndSquares), A);
  p2 = lower_bound(ALL(fairAndSquares), B + 1);

  return p2 - p1;
}

int main() {
  int t,case_no=1;
  initFairAndSquareNumbers();
  cin>>t;
  while(t--){
    printf("Case #%d: %lld\n" , case_no++ , solve());    
  }
  return 0 ;
}
