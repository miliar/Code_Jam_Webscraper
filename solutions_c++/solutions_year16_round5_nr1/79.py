#define BUFSIZE 1000000
char buf[BUFSIZE];
int Tests, cnum;
// #define USEWIN
#define MANYTESTS 1
// #define LINEBYLINE

// Eryx's new template for I/O contests, May 3, 2015

#include <algorithm>
#include <string>
#include <stdio.h>
using namespace std;

#define Size(x) (int(x.size()))

string getLine() {
  string s;
  while(!feof(stdin)) {
    char c = fgetc(stdin);
    if(c <= 0) continue;
    if(c == 13) continue;
    if(c == 10) return s;
    s += c;
    }
  return s;
  }

int scanerr;

int getNum() {
#ifdef LINEBYLINE
  string s = getLine();
  return atoi(s.c_str());
#else
  int i;
  scanerr = scanf("%d", &i);
  return i;
#endif
  }

string getStr() {
#ifdef LINEBYLINE
  return getStr();
#else
  scanerr = scanf("%s", buf);
  return buf;
#endif
  }

#line 10 "work.cpp"

/// ----


//Eryx

// !FDI

char stk[500000];
  
void solveCase() {
  int res = 0;
  
  string S = getStr();
  
  int qstk = 1;
  stk[0] = 'X';
  
  int score = 0;
  
  for(char c: S) 
    if(c == stk[qstk-1]) qstk--, score += 10;
    else stk[qstk++] = c;
  
  while(qstk>1) { qstk -= 2; score += 5; }
  
  printf("Case #%d: %d\n", cnum, score);
  }

#define P 1000000007

int main() {

  if(!MANYTESTS) Tests = 1;
  else Tests = getNum();
  
  for(cnum=1; cnum<=Tests; cnum++)
    solveCase();
    
  // finish
  return 0;
  }

// This solution includes hidden routines to solve test cases in separate
// processes in order to make it faster. I will update them to run on a
// cluster if I get one ;)
