/*
 * qa.cpp
 *
 *  Created on: Apr 30, 2016
 *      Author: suparsh14
 */


#include<bits/stdc++.h>

using namespace std;


int main(){

	int tc;
	scanf("%d",&tc);


	for(int i=1;i<=tc;i++){
		char str[2010];
		int dig[10],a[26];
		scanf("%s",str);


		memset(a,0,sizeof(a));
		memset(dig,0,sizeof(dig));
		int t=0;

		while(str[t]!=0){

			a[str[t]-'A']++;
			t++;
		}

		dig[0]=a['Z'-'A'];
		dig[2]=a['W'-'A'];
		dig[4]=a['U'-'A'];
		dig[6]=a['X'-'A'];
		dig[8]=a['G'-'A'];
		dig[3]=a['H'-'A']-dig[8];
		dig[5]=a['F'-'A']-dig[4];
		dig[7]=a['V'-'A']-dig[5];
		dig[1]=a['O'-'A']-dig[4]-dig[2]-dig[0];
		dig[9]=a['I'-'A']-dig[6]-dig[5]-dig[8];

		printf("Case #%d: ",i);

		for(int k=0;k<=9;k++)
		{
			for(int j=1;j<=dig[k];j++){
				printf("%d",k);
			}
		}
		printf("\n");






	}


	return 0;
}

