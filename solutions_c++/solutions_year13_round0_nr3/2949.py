#include <iostream>
#include <cstdio>
using namespace std;
int t;

int palindrome(int x){
 	int a=x;
 	int b=0;
 	while(a) {
 		b*=10;
 	 	b+=a%10;
 	 	a/=10;
 	}
 	return (x==b);
}

int square(int x){
 	int i;
 	for(i=1;i*i<x;i++);
 	if(i*i==x) return palindrome(i);
 	return 0;
}

int main(){
 	freopen("c_input","rt",stdin);
 	freopen("c_output","wt",stdout);
 	cin>>t;
 	for(int i=1;i<=t;i++) {
 	 	int a,b;
 	 	cin>>a>>b;
 	 	int y=0;
 	 	for(int x=a;x<=b;x++) {
 	 		if(square(x)&&palindrome(x)) {
// 	 			cout<<x<<endl;
 	 			y++;
 	 		}
 	 	}
 	 	printf("Case #%d: %d\n",i,y);
 	}
 	return 0;
}