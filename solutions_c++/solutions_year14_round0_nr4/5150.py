#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>

using namespace std;

int n;

double naomi [1024], ken [1024];

void solve( int test_case)
{
	int i, j, ans=0, l;

	scanf("%d", &n);

	for(i=0; i<n; i++)
		scanf("%lf", &naomi[i]);

	for(i=0; i<n; i++)
		scanf("%lf", &ken[i]);

	sort(naomi, naomi + n);
	sort(ken, ken + n);

	/*for(i=0; i<n; i++)
		if(naomi [i] > ken [1]){
			
		}*/

	for(i=0; i<n; i++){
		l=0;
		for(j=0; j<n-i; j++)
			if(naomi [i+j] < ken [j]) l=1;

		if(l == 0){
			ans=n-i;
			break;
		}
	}
	
	int br= 0;

	for(i=0; i<n; i++){
		for(j=0; j<n; j++){
			if(naomi [i] < ken [j]){
				ken[j] = -1;
				br++;
				break;
			}
		}
	}
	
	printf("Case #%d: %d %d\n", test_case, ans, n-br);
}

int main()
{
	int i, t;

	scanf("%d", &t); 

	for(i=1; i<=t; i++)
		solve(i);

	return 0;
}
