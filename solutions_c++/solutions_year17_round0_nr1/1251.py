/*
 *	Task: A. Oversized Pancake Flipper
 *	Lang: C/C++11
 *	Author: comtalyst
 *	Site: Google Code Jam 2017 Qualification Round
 *	Last Update: 8/4/2017
 */

#include <bits/stdc++.h>
//#pragma GCC optimize ("O3")
using namespace std;

/* Note
Learned :  
*/	

#define x first
#define y second
#define umap unordered_map
#define pqueue priority_queue
#define mset multiset
#define mp make_pair

char str[1005];

main(){
	int t,i,j,n,m,k,res,tt=0;
	freopen("A-l-in.txt","r",stdin);
	freopen("A-l-out.txt","w",stdout);	
	
	scanf("%d",&t);
	while(t--){
		res = 0;
		scanf("%s %d",str+1,&k);
		n = strlen(str+1);
		for(i = 1; i <= n-k+1; i++){
			if(str[i] == '-'){
				res++;
				for(j = 0; j < k; j++){
					if(str[i+j] == '+'){
						str[i+j] = '-';
					}
					else{
						str[i+j] = '+';
					}
				}
			}
		}
		for(; i <= n; i++){
			if(str[i] == '-'){
				res = -1;
				break;
			}
		}
		if(res != -1){
			printf("Case #%d: %d\n",++tt,res);
		}
		else{
			{
			printf("Case #%d: IMPOSSIBLE\n",++tt);
		}
		}
	}
	
	return 0;	
}


















