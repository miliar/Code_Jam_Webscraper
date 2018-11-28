#include <stdio.h>
#include <set>
#include <iostream>

using namespace std;

int main(){

int T;
scanf("%d\n",&T);
int n=0;

while(n++<T){

int L;
scanf("%d\n",&L);

set<int> num;

for(int i=1; i<=4; i++){
	for(int j=0; j<4; j++){
		int a;
		scanf("%d",&a);

		if(i==L)
			num.insert(a);	
	}
}

scanf("%d\n",&L);

set<int> num2;

for(int i=1; i<=4; i++){
	for(int j=0; j<4; j++){
		int a;
		scanf("%d",&a);

		if(i==L){
			if(num.count(a))
				num2.insert(a);
		}
	}
}
 
set<int>::iterator k = num2.begin();

	if(num2.size()==0)
		printf("Case #%d: Volunteer cheated!\n",n);
	else if(num2.size()==1){
		printf("Case #%d: ",n);
		cout << *k << endl;}
	else
		printf("Case #%d: Bad magician!\n",n);

}


return 0;
}
