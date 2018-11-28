#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
#include<vector>
using namespace std;

int C,n;
double a[1000],b[1000];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&C);
	for(int tc=1;tc<=C;tc++){
		printf("Case #%d: ",tc);
		scanf("%d",&n);
		for(int i=0;i<n;i++)scanf("%lf",a+i);
		for(int i=0;i<n;i++)scanf("%lf",b+i);
		sort(a,a+n);
		sort(b,b+n);
		int a1=0,b1=0,a2=n-1,b2=n-1;
		int A=0,B=0;
		while(a1<=a2){
			if(a[a2]>b[b2]){
				A++;
				a2--;
				b2--;
			}
			else{
				a1++;
				b2--;
			}
		}
		a1=0,b1=0,a2=n-1,b2=n-1;
		while(b1<=b2){
			if(a[a2]>b[b2]){
				B++;
				a2--;
				b1++;
			}
			else{
				a2--;
				b2--;
			}
		}
		printf("%d %d\n",A,B);
	}
	return 0;
}