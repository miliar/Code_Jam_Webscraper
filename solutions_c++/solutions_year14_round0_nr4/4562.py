#include <cstdio>
#include <iostream>
#include <algorithm>
using namespace std;

#define S(n)	scanf("%d",&n)
#define SF(n)	scanf("%lf",&n)
#define EPS 1e-6
#define OO 1e9

bool rev(const double &a , const double &b){return a > b;}

int main(){
	freopen("in.in" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);

	int TC , cc = 0 ;
	int n , war , dwar;
	double c1[1001] , c2[1001] ;
	
	S(TC);
	while(TC--){
		war = dwar = 0;
		S(n);
		for (int i = 0; i < n; i++)	SF(c1[i]);
		for (int i = 0; i < n; i++)	SF(c2[i]);
		sort(c1 , c1+n);
		sort(c2 , c2+n);
		for (int i = 0 , j = 0; i < n; i++){
			if(c2[i] > c1[j]){
				war++;
				j++;
			}
		}
		war = n - war;
		for (int i = 0 , j = 0; i < n; i++){
			if(c1[i] > c2[j]){
				dwar++;
				j++;
			}
		}
		//reverse(c2 , c2+n);
		//for (int i = 0; i < n; i++){
		//	if(c1[i] > c2[i])
		//		dwar++;
		//}


		printf("Case #%d: %d %d\n" , ++cc , dwar , war);
	}
	return 0;
}