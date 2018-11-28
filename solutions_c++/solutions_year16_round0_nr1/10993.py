#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES

#include "bits/stdc++.h"
#include <vector>
#include <set>
#include <string>
#include <queue>
#include <list>
#define REP(i,a,b) for(i=a;i<b;++i)
#define rep(i,n) REP(i,0,n)
#define ll long long
#define ull unsigned ll
typedef long double ld;
#define SQR(X)  ( (X)*(X) )
#define CUBE(X) ( (X)*(X)*(X) )
#define ALL(a) (a).begin(),(a).end()
// #define int ll
#define ifnot(a) if(not a)
#define dump(x)  cerr << #x << " = " << (x) << endl
using namespace std;


void reader(int &a){scanf("%d",&a);}
void reader(double &a){scanf("%lf",&a);}
void reader(char a[]){scanf("%s",a);}
void reader(ll &a){scanf("%lld",&a);}
void reader(ull &a){scanf("%llu",&a);}
// void reader(string& a){cin >> a;};
template<class T,class U>
void reader(T& t,U& u){
  reader(t); reader(u);
}
template<class T,class U,class V>
void reader(T& t,U& u,V& v){
  reader(t); reader(u); reader(v);
}

void writer(int a,char c) {printf("%d",a); putchar(c);}
void writer(double a,char c) {printf("%.20lf",a); putchar(c);}
void writer(char a[]) {printf("%s",a);};
void writer(char a[],char c) {printf("%s",a);putchar(c);};
void writer(char a,char c) {putchar(a); putchar(c);};
template<class T>
void writerLn(T t){
  writer(t,'\n');
}
template<class T,class U>
void writerLn(T t,U u){
  writer(t,' ');
  writer(u,'\n');
}
template<class T,class U,class V>
void writerLn(T t,U u,V v){
  writer(t,' '); 
  writer(u,' '); 
  writer(v,'\n'); 
}
template<class T> 
void writerArr(T x[], int n){
  int i;if(!n){putchar('\n');return;}
  rep(i,n-1) writer(x[i],' ');
  writer(x[n-1],'\n');
}
template<class T> 
void writerVec(vector<T> x,int n){
  int i;if(!n){putchar('\n');return;}
  rep(i,n-1) writer(x[i],' ');
  writer(x[n-1],'\n');
}

vector<std::string> split(const std::string &str, char sep)
{
  std::vector<std::string> v;
  std::stringstream ss(str);
  std::string buffer;
  while( std::getline(ss, buffer, sep) ) {
    v.push_back(buffer);
  }
  return v;
}

bool test = 1;

//.....................

signed main(void)
{
  int i,j;
  freopen("A-large.in","r",stdin);
  freopen("out.txt","w",stdout);
  int T; cin >> T;
  rep(i,T) {
    int N; cin >> N;
    set<int> a;
    printf("case #%d: ",i+1);
    if(N == 0) {
      puts("INSOMNIA");
      continue;
    }
    for(j=1;;j++) {
      int b = N*j;
      while(b) {
        a.insert(b%10);
        b/=10;
      }
      if(a.size() == 10) break;
    }
    writerLn(N*j);
  }
  return 0;
}