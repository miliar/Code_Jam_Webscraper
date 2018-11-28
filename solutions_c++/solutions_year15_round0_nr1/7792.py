#include<iostream>
#include <stdio.h>
using namespace std;
int main(void) {
	int t;
	int test =1;
	scanf("%d",&t);
	while(t!=0){
	int d;
	string n;
	cin >> d >>n;
	int i,count=0,countreq = 0;
	for(i=0;i<=d;i++){
		int te = n[i];
			te = te - 48;
			if(i > count){
				int temp = i - count;
				countreq = countreq + temp;
				count = te + countreq+ count;
			}
			else{
				count = count + te;
			}
		}
		printf("Case #%d: %d\n",test,countreq);
	test++;
	t--;	
	}
	return 0;
}
