#include <stdio.h>
#include <iostream>
#include <math.h>
#include <vector>
#include <utility>
#include <algorithm>
#include <string>
#include <set>

using namespace std;

int main() {
    freopen("input.txt", "r",stdin);
    freopen("output.txt", "w",stdout);
    int n,k=1;
    scanf("%d",&n);
    while(n--){
		vector<int> arr;
		int c,aux=0,cont=0;
		int a;
		scanf("%d",&a);
		a--;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(i==a){
				scanf("%d",&c);
				arr.push_back(c);
				}else
				scanf("%d",&c);
				}			
			}
		scanf("%d",&a);
		a--;
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				if(i==a){
				scanf("%d",&c);
				for(int z=0;z<(int)arr.size();z++){
					if(arr[z]==c){
						aux=c;
						cont++;
						}
					}
				}else
				scanf("%d",&c);
				}			
			}
			if(cont==1)
		printf("Case #%d: %d\n",k,aux);
		else if(cont!=0)
		printf("Case #%d: Bad magician!\n",k);
		else
		printf("Case #%d: Volunteer cheated!\n",k);		
		k++;
	}
   
} 
