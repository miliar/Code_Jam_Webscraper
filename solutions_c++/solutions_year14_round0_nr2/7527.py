#include<iostream>
#include<stack>
#include<vector>
#include<algorithm>
#include<stack>
#include<queue>
#include<cstdio>
#include<string>
#include<cstring>
#include<cmath>
#include<complex>
#include<sstream>
#include<map>
#include<set>
#define DEBUG(x) cout<<"line"<<__LINE__<<":"<<#x" == "<<x<<endl
#define REP(i,n) for(int i = 0; i < (int)(n); i++)
#define ALL(x) (x).begin(),(x).end()
#define INF 1000000
#define isValid(x,y,p,q) (x>=0 && x<p &&y>=0 && y<q)

using namespace std;

inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}
typedef long long ll;
typedef pair<int,int> P;

int dx[]={-1,0,1,0};
int dy[]={0,-1,0,1};
  
///////////////////////////////////////////////////////////////

double calc(double C,double F,double X){
  double ans = 0.0;
  double gain = 2.0;  
  while(1){
    if (((C/gain)+(X/(gain+F))) < X/gain){
      ans += C/gain;
      gain += F;
    }else{
      ans += X/gain;
      break;
    }
  }
  return ans;
}

int main(){
  int n = 0;
  cin>>n;
  REP(num,n){
    double C=0.0,F=0.0,X=0.0;
    scanf("%lf %lf %lf",&C,&F,&X);
    printf("Case #%d: %0.7lf\n",num+1,calc(C,F,X));
  }
  return 0;
}

