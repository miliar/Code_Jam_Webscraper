#include <iostream>
#include <fstream>
#include <stdio.h>
using namespace std;

long long p[45] = {39, 1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321,
 4008004, 100020001, 102030201, 104060401, 121242121, 123454321,
 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121,
 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001,
 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121,
 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004};

int main(){
    int N, cases = 0;
	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.out","w",stdout);
	scanf("%d", &N);
	while(N--){
	    long long x, y;
	   	int ax = -1, ay = -1;
	    cases++;
		scanf("%I64d%I64d", &x, &y);
		for(int i=1; i<=p[0]; i++)
			if(p[i] >= x){
				ax = i;
				break;
			}
		for(int i=1; i<=p[0]; i++)
			if(p[i] <= y) ay = i;
			else break;
		printf("Case #%d: %d\n", cases, max(0, ay-ax+1));
	}
    return 0;
}
