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
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef vector<vs> vvs;
#define pb push_back
#define sz(v) ((int)(v).size())

long long m=1000000007;
long long fact[200];


int main()
{
  int i=0,j=0,k=0; char buf[100000]="";
  fact[0]=1;
  for(i=1;i<200;i++) fact[i]=(i*fact[i-1])%m;
  int _cases=0, _case=0;
  scanf("%d",&_cases);
  for(_case=1;_case<=_cases;_case++) {
    int n; scanf("%d",&n);
    vs words;
    long long ant=1;
    set<char> lockedin;
    for(k=0;k<n;k++) {
      scanf("%s",buf);
      string s=buf;
      string t;
      for(i=0;i<sz(s);i++)
        if(i==0||s[i]!=s[i-1]) t+=s[i];
      words.pb(t);
      for(i=1;i<sz(t)-1;i++) {
        if(lockedin.find(t[i])!=lockedin.end())
          ant=0;
        lockedin.insert(t[i]);
      }
    }

    string L, R;
    for(k=0;k<n;k++) {
      char x = words[k][0], y=words[k][sz(words[k])-1];
      if(x==y && sz(words[k])>1)
        ant=0;
      if(lockedin.find(x)!=lockedin.end()||lockedin.find(y)!=lockedin.end())
        ant=0;
      L+=x; R+=y;
    }

    string L2, R2;
    for(char C='a';C<='z';C++) {
      int lcount=0,rcount=0,mcount=0;
      int wherel=-1,wherem=-1,wherer=-1;
      for(k=0;k<sz(L);k++) {
        if(L[k]==C&&R[k]==C) {
          mcount++;
          ant=(mcount*ant)%m;
          if(mcount==1) {
            wherem=k;
          } else {
            L[k]='.'; R[k]='.';
          }
        } else if(L[k]==C) {
          lcount++;
          wherel=k;
        } else if(R[k]==C) {
          rcount++;
          wherer=k;
        }
      }
      if(rcount>1||lcount>1) {
        ant=0;
      }
      if(rcount>0||lcount>0) {
        for(k=0;k<sz(L);k++) {
          if(L[k]==C&&L[k]==R[k]) {L[k]='.'; R[k]='.';}
        }
      }
      if(rcount && lcount) {
        L[wherel] = L[wherer];
        R[wherer] = '.';
        L[wherer] = '.';
        if(L[wherel]==R[wherel]) ant=0; //cycle
      }

      for(i=0;i<sz(L);i++) {
        if(L[i]!='.') {L2+=L[i]; R2+=R[i];}
      }
//printf("C=%c L2=%s, R2=%s lcount=%d, mcount=%d, rcount=%d, ant=%lld\n",C,L2.c_str(),R2.c_str(),lcount, mcount, rcount, ant);
      L=L2; R=R2;
      L2=""; R2="";
    }    
    for(k=1;k<=sz(L);k++) ant=(ant*k)%m;

    printf("Case #%d: %lld\n", _case, ant);
  }

  return 0;
}
