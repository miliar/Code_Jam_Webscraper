#include <cstdio>
#include <numeric>
#include <iostream>
#include <vector>
#include <set>
#include <cstring>
#include <string>
#include <map>
#include <cmath>
#include <ctime>
#include <algorithm>
#include <bitset>
#include <queue>
#include <sstream>
#include <deque>

using namespace std;

static char s[1002];
static char finals[2004];

int main() {
  int i , T, len, j, mark, start;
  char c;
  cin >> T;
  for (i = 0; i < T; i++) {
     memset(s, '\0', sizeof(s));
	 memset(finals, '\0', sizeof(finals));
	 cin >> s;
	 len = strlen(s);
	 start = mark = 1001;
	 for (j = 0; j < len; j++) {
       c = s[j];
	   if (j == 0) {
		   finals[mark] = c;
	   } else if (c >= finals[start]) {
           start--;
		   finals[start] = c; 
	   } else {
          mark++;
          finals[mark] = c;
	   }
	 }
     cout << "Case #"<<i+1<<": "<<&finals[start]<<"\n";
  }
  return 0;
}