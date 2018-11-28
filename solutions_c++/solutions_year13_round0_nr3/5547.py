#include<iostream>
#include<cmath>
#include<cstdio>
using namespace std;
bool isPalindrome(long long int a){
	long long int b;
	long long int s = 0;
	b = a;
	int x;
	while(a > 0){
		x=a%10;
		a=a/10;
		s=s*10+x;
	}
	if(s == b)
		return true;
	else
		return false;
}
int main(){
	
	long long int A,B,i,m = 0,t,test,z,cnt;
	scanf("%d",&test);
	long long int a[100] = {0};
	for(i=1;i<=10000000;i++){
		if(isPalindrome(i) == true){
			z = i * i;
			if(isPalindrome(z) == true){
				a[m]=z;
				m++;
			}
		}
	}
	for(i=1;i<=test;i++){
		cnt = 0;
		scanf("%lld %lld",&A,&B);
		for(t=0;;t++){
			if(a[t] >= A && a[t] <= B)
				cnt++;
			if(a[t]>B)
				break;
		}
		cout << "Case #" << i << ": " << cnt << endl;
	}
	return 0;
}
	

