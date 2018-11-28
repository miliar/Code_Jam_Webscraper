#include <iostream>
#include <stdio.h>
using namespace std;
int main(){
	int i, t, T, start, end;
	long long int sq[] = {1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404};
	long long	a, b;
	scanf("%d",&T);
	for(t=1;t<=T;t++){
		cin>>a>>b;
		i=0;
		while(sq[i] < a && i < 21) i++;
		start = i;
		while(i < 21){
			if(sq[i] > b){
				break;
			}
			i++;
		}
		end = i;
		printf("Case #%d: %d\n", t, end-start);
	}
	return 0;
}