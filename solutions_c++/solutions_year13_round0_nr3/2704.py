#define _USE_MATH_DEFINES
#define INF 0x3f3f3f3f
#include <cstdio>
#include <iostream>
#include <sstream>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <queue>
#include <stack>
#include <limits>
#include <map>
#include <string>
#include <cstring>
#include <set>
#include <deque>
#include <bitset>
#include <list>
#include <cctype>
#include <utility>
 
using namespace std;
 
typedef long long ll;
typedef pair <int,int> P;
typedef pair <int,P > PP;
 
const int tx[] = {0,1,0,-1};
const int ty[] = {-1,0,1,0};

bool isPalindrome(const char buf[101]){
  for(int lhs=0,rhs=strlen(buf)-1;lhs <= rhs; lhs++,rhs--){
    if(buf[lhs] != buf[rhs]) return false;
  }

  return true;
}

int ComputeSquare(int num){
  for(int i=1;i*i<=num;i++){
    if(num == i*i) return i;
  }

  return -1;
}

int main(){
  int H,W;
  int T;
  while(~scanf("%d",&T)){
    for(int test_num = 0; test_num < T; test_num++){
      int first,last;
      scanf("%d %d",&first,&last);

      int count = 0;
      for(int i=first;i<=last;i++){
	char buf[101];
	memset(buf,'\0',sizeof(buf));
	sprintf(buf,"%d",i);
	if(!isPalindrome(buf)) continue;

	int square = ComputeSquare(i);
	if(square == -1) continue;

	memset(buf,'\0',sizeof(buf));
	sprintf(buf,"%d",square);
	if(!isPalindrome(buf)) continue;
	
	count++;
      }

      printf("Case #%d: %d\n",test_num+1,count);
    }
  }
}
