/*
ID: abunida1
PROG: ride
LANG: C++
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <string>
#include <map>
#include <math.h>
#include <stack>
#include <bitset>
#include <list>
#include <limits.h>

using namespace std;


#define ii pair<int,int>
#define iii pair<int,ii>
#define INF 1000000000
typedef long long int ll;
typedef unsigned long long int ull;
typedef vector <int> vi;
typedef vector <ii> vii;


int main (){

	freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);
	//freopen("friday.in","r",stdin);	freopen("friday.out","w",stdout);
	
	int t_kasus;
	int kasus=1;
	scanf("%d",&t_kasus);
	
	map <int,int> m;
	map <int,int> ::iterator it;
	
	while(t_kasus--){
		printf("Case #%d: ",kasus);
		kasus++;
		
		int guess;
		int angka;
		scanf("%d",&guess);
		
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				
				scanf("%d",&angka);
				
				if(i==guess)m[angka]++;
			}
		}
		
		scanf("%d",&guess);
		
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				
				scanf("%d",&angka);
				
				if(i==guess)m[angka]++;
			}
		}
		
		// for(it=m.begin();it!=m.end();it++){
			// printf("%d ",it->first);
		// }printf("\n");
		
		if(m.size()==7){
			for(it=m.begin();it!=m.end();it++){
				if(it->second==2)printf("%d\n",it->first);
			}
		}
		else if(m.size()==8){//cheat
			printf("Volunteer cheated!\n");
		}
		else {//bad
			printf("Bad magician!\n");
		}
		
		
		m.clear();
	}

	
	return 0;
}
















