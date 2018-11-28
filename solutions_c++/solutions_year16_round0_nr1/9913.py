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
main() {
  freopen("in", "r", stdin);
  freopen("out", "w", stdout);
  int tt;
  int i,j,no,temp,temp1,rem,array[10],flag=1;
  scanf("%d", &tt);
  
  for (int qq=1;qq<=tt;qq++) {
    printf("Case #%d: ", qq);
	scanf("%d",&no);
	if(no == 0){
		printf("INSOMNIA\n");
		continue;
	}
	for(i=0;i<10;i++)
	  array[i] = -1;
	while(1){
		i=1;
		while(1){
			temp = no * i;
			temp1= temp;
			while(temp1>0){
				rem = temp1 % 10;
				temp1 = temp1/10;
				if(array[rem]<0)
					array[rem] = 1;
				
			}
			for(j=0;j<10 && array[j]!=-1;j++);
			if(j==10){
				flag=0;
				break;
			}
			++i;
			//printf("for i=%d,temp=%d",i,temp);
		}
		if(flag==0)
			break;
		for(i=0;i<10 && array[i]!=-1;i++);
			if(i==10)
				break;
	}
	printf("%d\n",temp);
}
}