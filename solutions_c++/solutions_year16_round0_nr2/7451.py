#include <vector>
#include <list>
#include <string.h>
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
#define ll long long

using namespace std;

int main() {
 freopen("B-large.in", "r", stdin);
 freopen("B-large.out", "w", stdout);
  int tt;
  scanf("%d", &tt);
  for (int qq=1;qq<=tt;qq++) {
    printf("Case #%d: ", qq);
    char s[150];
	int cnt = 0 ;
    scanf("%s",&s);
    int k = strlen(s);
    for(int i = k - 1 ; i >= 0 ; i--){
    	if(s[i] == '-'){
    		if(s[0] != '-'){
    			int j = 0 ;
    			cnt++;
    		    while(j < i && s[j+1] == '+')  j++ ,s[j] = '-';
    			while( j < i && s[j+1] == '-')  j++ ;
    			if(j == i) {
    				for(int px = 1 ; px <= j ;px++){
    					s[px] = '+';
					}
					cnt++;
					break;
			    }
			}
    		  int a1 = 0 , b1 = i;
    		  while(a1 <= b1){
                char tmp = s[a1];
    			if(s[b1] == '-') s[a1] = '+';
    			else             s[a1] = '-';
    			if(tmp == '+')   s[b1] = '-';
    			else             s[b1] = '+';
    			a1++ ,b1--;
			 }
    		 cnt++;
		}
		//cout<<s<<endl;
	}
	printf("%d\n",cnt);
  }
  return 0;
}
