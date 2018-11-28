#include <vector>
#include <string.h>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
main() {
 freopen("in", "r", stdin);
 freopen("out", "w", stdout);
  int tt,i,j;
  char str[100];
  scanf("%d", &tt);
  
  for (int qq=1;qq<=tt;qq++) {
    printf("Case #%d: ", qq);
	scanf("%s",&str);
	int count = 0;
	for(i=0;i<strlen(str)-1;i++){
		if(str[i] != str[i+1]){
			++count;
			for(j=0;j<=i;j++){
				//printf("%c",str[i+1]);
				str[j] = str[i+1];
		}}
	}
	if(str[0]=='-')
		//printf("hey");
		++count;
	printf("%d\n",count);
	}
}