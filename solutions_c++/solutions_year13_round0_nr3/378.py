#include <iostream> 
#include <sstream> 
#include <string> 
#include <vector> 
#include <queue> 
#include <set> 
#include <map> 
#include <cstdio> 
#include <cstdlib> 
#include <cctype> 
#include <cmath> 
#include <list> 
#include <numeric>
#include <regex.h>  
#include <algorithm>
using namespace std; 
 
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef vector<string> vs; 
typedef vector<vs> vvs;
#define pb push_back 
#define sz(v) ((int)(v).size()) 
 
bool ispalin(long long n) {
  char buf[100];
  sprintf(buf,"%lld",n);
  string s=buf;
  for(int i=0;i<sz(s);i++)
    if(s[i]!=s[sz(s)-1-i])
      return false;
  return true;
}

 
int main()
{
  int i=0,j=0; char buf[100000]="";

  int run,runs;
  scanf("%d",&runs);

  vector<long long> answers;

  for(long long k=1;k<=10000000;k++) {
    if(ispalin(k)&&ispalin(k*k))
      answers.pb(k*k);
  }
    
  long long a,b;
  for(run=1;run<=runs;run++) {
    scanf("%lld %lld",&a,&b);  
    int up = upper_bound(answers.begin(),answers.end(),b) - answers.begin();
    int lo = lower_bound(answers.begin(),answers.end(),a)- answers.begin();
    printf("Case #%d: %d\n",run, up - lo);
  }






  return 0;
}
