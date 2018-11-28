#include <vector>
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

int main() {
  freopen("a.txt", "r", stdin);
  freopen("new.out", "w", stdout);
  int tt,sy,i;
  char str[1000];
  
  scanf("%d", &tt);
  for (int qq=1;qq<=tt;qq++) {
    printf("Case #%d: ", qq);
    int sum=0,res=0;
    scanf("%d",&sy);
    scanf("%s",str);
    sum=str[0]-'0';
    
	if (sy==0) printf("%d\n",res);
	else 
	{//if(sum==0) res++;
	for(i=1;i<=sy;i++)
    	{
    	
		if(sum<i&&str[i]-'0'==0){
		res++;
		sum++;
		}
		else if (sum<i&&str[i]-'0'!=0) {
		res++;
		sum+=str[i]-'0'+1;
		}
		else sum+=str[i]-'0';
		}
    printf("%d\n",res);
	}
}
  return 0;
}
