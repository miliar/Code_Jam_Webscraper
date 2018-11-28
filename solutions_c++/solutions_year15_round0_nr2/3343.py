#include <iostream>
#include <stdio.h>
#include <set>
#include <stdlib.h>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	freopen("B-small-attempt0.in-2.txt","r",stdin);
	freopen("Boutput.out","w",stdout);
	int t,d;
	scanf("%d",&t);
	for(int r=1; r<t+1; ++r){
		scanf("%d",&d);
		int max=-1,cost,mincost=99999999,x;
		vector<int> vec;
		for(int h=0; h<d; ++h){
			scanf("%d",&x);
			vec.push_back(x);
			if(max<vec[h]) max=vec[h];
		}
		for(int i=1; i<max+1; ++i){
			cost=0;
			for(int j=0; j<d; ++j){
				//printf("vec[j]: %d   i: %d\n",vec[j],i);
				//printf("%d\n",((vec[j]/i) + (vec[j]%i > 0 ? 1 : 0)));
				//printf("%d - %d >? %d\n", vec[j], i, i);
				if(vec[j]>i) cost+=(((vec[j]-i)/i) + ((vec[j]-i)%i > 0 ? 1 : 0));
			}
			cost+=i;
			//printf("Cost: %d\n",cost);
			if(mincost>cost) mincost=cost;
		}
		printf("Case #%d: %d\n",r,mincost);
	}
	return 0;
}
	
					
			
