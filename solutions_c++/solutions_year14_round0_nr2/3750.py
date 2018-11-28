#include <iostream>
#include <stdio.h>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <vector>
#include <queue>
using namespace std;

typedef vector<int> voi;
typedef set<int> soi;
typedef vector<voi> vooi;
typedef pair<int, int> pii;

#define FOR(i, a, b) for(i=(a); i < (b); ++i)
#define REPEAT(i, n) FOR(i, 0, n)

#define	 EPS 1E-10

int main(){
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	//ios_base::sync_with_stdio(false);
	
	int T;
	scanf("%d", &T);
	double C,F,X;
//	scanf("%F %F %F", &C, &F, &X);


	int i,j,k;
	
	double cookies_count = 0;
	double producity = 0;
	double time = 0;
	double newest = 0;
	for (k=1; k<= T; ++k){
		cin >> C >> F >> X;
		printf("Case #%d: ", k);

		producity = 2;
		cookies_count = 0;
		time = 0;
		
		//while (cookies_count < X){

			//while ((X / producity ) > +X / (producity + F))){
			while (true){
				newest =  C / (producity );
				//if (fabs((X / producity ) - (newest + (X / (producity + F)))) < EPS){
				if ((X / producity ) > (newest + (X / (producity + F)))){
					time += newest;
					producity +=F;
				}
				else{
					time += X / (producity ); 
					break;
				}
			}
			

			printf("%7.7f\n", time);
			//cout << time << endl;

		//}
		//while 




	}
	
	return 0;
}
