/*
 * Qb.cpp
 *
 *  Created on: Apr 10, 2016
 *      Author: suparsh14
 */

/*
 *logic:first flip contiguous '+' or '-' to make similar to next contiguous '-' or '+'. repeat this procedure until each become '+'.
 */
#include<bits/stdc++.h>

using namespace std;

char str[110];

int main(){

	int tc;
	scanf("%d",&tc);

	for(int i=1;i<=tc;i++){
		scanf("%s",str);
		int len=0,cnt=0;

		while(str[len+1]){
			if(str[len]!=str[len+1])cnt++;
			len++;
		}

		if(str[len]=='-')cnt++;

		printf("Case #%d: %d\n",i,cnt);


	}



	return 0;
}


