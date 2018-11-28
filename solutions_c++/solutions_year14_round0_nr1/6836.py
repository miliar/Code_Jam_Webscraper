#include <stdio.h>
#include <stdlib.h>
#include <set>
using namespace std;

int main(){
	int t;scanf("%d",&t);
	for(int i=1;i<=t;i++){
		set<int> myset;
		int a,x;scanf("%d",&a);
		int num;
		for(int j=1;j<=4;j++){
			for(int k=1;k<=4;k++){
				scanf("%d",&num);
				if(j==a){
					if(myset.find(num)!=myset.end()){x=num;}
					myset.insert(num);
				}
			}
		}
		scanf("%d",&a);
		for(int j=1;j<=4;j++){
			for(int k=1;k<=4;k++){
				scanf("%d",&num);
				if(j==a){
					if(myset.find(num)!=myset.end()){x=num;}
					myset.insert(num);
				}
			}
		}
		if(myset.size()==8)	{
			printf("Case #%d: Volunteer cheated!\n",i);
		}
		else if(myset.size()<=6){
			printf("Case #%d: Bad magician!\n",i);
		}
		else{
			printf("Case #%d: %d\n",i,x);
		}
	}
}
