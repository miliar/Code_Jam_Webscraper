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
#include <algorithm>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef vector<vs> vvs;
#define pb push_back
#define sz(v) ((int)(v).size())




int main(){
  int run,runs;
  scanf("%d",&runs);
  map<int, string> M;
  M[0]="ZERO";
  M[1]="ONE";
  M[2]="TWO";
  M[3]="THREE";
  M[4]="FOUR";
  M[5]="FIVE";
  M[6]="SIX";
  M[7]="SEVEN";
  M[8]="EIGHT";
  M[9]="NINE";
  for(run=1;run<=runs;run++){
    string found="";
    char buf[100000];
    scanf("%s",buf); string s=buf;
    vi tel(26,0);
    for(int i=0;i<sz(s);i++)tel[s[i]-'A']++;
    
    int fnu,dnu; char cnu;
    
    cnu='Z'; fnu=tel[cnu-'A']; dnu=0;    found+=string(fnu,dnu+'0'); for(int j=0;j<sz(M[dnu]);j++) tel[M[dnu][j]-'A']-=fnu;
    cnu='W'; fnu=tel[cnu-'A']; dnu=2;    found+=string(fnu,dnu+'0'); for(int j=0;j<sz(M[dnu]);j++) tel[M[dnu][j]-'A']-=fnu;
    cnu='U'; fnu=tel[cnu-'A']; dnu=4;    found+=string(fnu,dnu+'0'); for(int j=0;j<sz(M[dnu]);j++) tel[M[dnu][j]-'A']-=fnu;
    cnu='X'; fnu=tel[cnu-'A']; dnu=6;    found+=string(fnu,dnu+'0'); for(int j=0;j<sz(M[dnu]);j++) tel[M[dnu][j]-'A']-=fnu;
    cnu='G'; fnu=tel[cnu-'A']; dnu=8;    found+=string(fnu,dnu+'0'); for(int j=0;j<sz(M[dnu]);j++) tel[M[dnu][j]-'A']-=fnu;
    cnu='F'; fnu=tel[cnu-'A']; dnu=5;    found+=string(fnu,dnu+'0'); for(int j=0;j<sz(M[dnu]);j++) tel[M[dnu][j]-'A']-=fnu;
    cnu='V'; fnu=tel[cnu-'A']; dnu=7;    found+=string(fnu,dnu+'0'); for(int j=0;j<sz(M[dnu]);j++) tel[M[dnu][j]-'A']-=fnu;
    cnu='H'; fnu=tel[cnu-'A']; dnu=3;    found+=string(fnu,dnu+'0'); for(int j=0;j<sz(M[dnu]);j++) tel[M[dnu][j]-'A']-=fnu;
    cnu='O'; fnu=tel[cnu-'A']; dnu=1;    found+=string(fnu,dnu+'0'); for(int j=0;j<sz(M[dnu]);j++) tel[M[dnu][j]-'A']-=fnu;
    cnu='E'; fnu=tel[cnu-'A']; dnu=9;    found+=string(fnu,dnu+'0'); for(int j=0;j<sz(M[dnu]);j++) tel[M[dnu][j]-'A']-=fnu;
    if(tel!=vi(26,0)) printf("ouch!\n");
    
    sort(found.begin(),found.end());
    printf("Case #%d: %s\n",run,found.c_str());
  }
}

