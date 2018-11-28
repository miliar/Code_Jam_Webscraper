#include <iostream>
#include<bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t, i;
	string A;
	int flag1=0;
	int flag2 = 0;
	int flag3 =0;
	scanf("%d",&t);
	int count = 0, l, j;
	for(i=1;i<=t;i++){
		A.clear();
		cin>>A;
		count = 0;
		flag1=flag2=flag3=0;
		l = A.length();
		for(j=0;j<l;){
			flag1 = 0;
			if(A[j]=='-' && j==0){
				while(A[j]!='+' && j<l){
					j++;
				}
				count = count + 1;
			}
			else if(A[j]=='+'){
				while(A[j]!='-' && j<l){
					j++;
				}
				while(A[j]!='+' && j<l){
					j++;
					flag1 = 1;
				}
				if(flag1==1){
					count = count + 2;
				}
			}
		}
		printf("Case #%d: %d\n",i, count);
	}
	return 0;
}