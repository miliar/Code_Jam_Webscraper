#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#include <set>
#include <stack>




using namespace std;


bool test(int number){

	 int n = number;
	 int reverse = 0;
	 int dig;
	 while (number > 0)
	 {
	      dig = number % 10;
	      reverse = reverse * 10 + dig;
	      number = number / 10;
	 }

	if(n == reverse)
		return true;

	else
		return false;



}



int main(){

	freopen("C1.in","r",stdin);
	freopen("C.out","w",stdout);

	int cases;
	scanf("%d",&cases);
	bool visited[1001];
	bool ok[1001];
	memset(visited,false,sizeof(visited));
	memset(ok,false,sizeof(ok));

	for(int i=1;i<=cases;i++){



		int start;
		int end;
		scanf("%d %d",&start,&end);

		int count=0;
		for(int j=start ; j<=end;j++){
			bool flag1=false,flag2=false,flag3=false;


			if(visited[j]){
				count+=ok[j];
			}

			else{
			visited[j]=true;
			int k = (int)  sqrt( j  );

			if(k * k == j)
				flag1=true;

			if(test(k))
				flag2=true;

			if(test(j))
				flag3=true;


			 if(flag1 && flag2 && flag3){
				 ok[j]=true;
 				 count++;
			 }

			}

		}


		printf("Case #%d: %d\n",i,count);


	}







}
