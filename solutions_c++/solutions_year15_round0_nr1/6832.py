/*
 * A.cpp
 *
 *  Created on: Apr 11, 2015
 *      Author: aki
 */

#include<cstdio>


int main(){
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);


	int T;
	scanf("%d",&T);
	T++;
	for(int t =1;t<T;t++){
		int trenutno=0, brojac=0;
		int k;
		scanf("\n%d ",&k);
		k++;
		int niz[k];
		for(int i=0;i<k;i++){
			scanf("%1d",(niz+i));
		}

		for(int i=1;i<k;i++){
			trenutno+=niz[i-1];
			if(trenutno<i){
				brojac+=(i-trenutno);
				trenutno=i;
			}

		}

		printf("Case #%d: %d\n", t, brojac);
		//scanf("\n");
	}

}


