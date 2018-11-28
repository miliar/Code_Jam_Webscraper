#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#define ll long long int

#include <algorithm>
#include <vector>
#include <utility>

using namespace std;


bool myfunc(const vector<long> &vec1, const vector<long> &vec2){
     int i=0;
     while(i<vec1.size()){
         if(vec1[i]<vec2[i]){
             return true;
         }
         else if(vec1[i]>vec2[i]){
             return false;
         }
         i++;
     }
     return true;
}


int main(){
	int t,use,i,j,k,n,temp,p,q,a[52][52],len,new1[52];
	scanf("%d",&t);
	for(i=1;i<=t;i++){
		scanf("%d",&n);
		use = (2*n) -1;
		int b[2502];
		for(j=0;j< 2502;j++) b[j]=0;
		while(use--){
			for(j=0;j<n;j++){
				scanf("%d",&temp);
				b[temp]++;
			}
		}
		k=0;
		for(j=1,k=0;j< 2502;j++){
			if(b[j]==0) continue;
			if(b[j]%2 !=0){
				new1[k] = j;
				k++;
			}
		}
		//printf("\n");
		//continue;
		sort(new1,new1+n);
		printf("Case #%d: ",i);
		for(j=0;j< n;j++){
			printf("%d ",new1[j]);
		}
		printf("\n");
		//ffree(b);
	}
	return 0;
} 