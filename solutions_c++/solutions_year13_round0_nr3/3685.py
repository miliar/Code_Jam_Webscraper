#include<iostream>
#include<math.h>
 using namespace std;
 
bool isInt(double d){
	int k = d;
	return k==d;
} 
 int reverse(int x){
	int y,z=0;
	while(x>0){
		y = x%10;
		x = (x-y)/10;
		z = (z*10)+y;
	}
	return z;
 }
 bool isPalindrome(int n){
	return n == reverse(n);
 }
 
 int main(){
	int c,i,j,a,b,cagla;
	cin>>c;
	for(i=0;i<c;i++){
		cin>>a>>b;
		cagla = 0;
		for(j=a;j<=b;j++){
			if(isInt(sqrt(j))&&isPalindrome(j)&&isPalindrome(sqrt(j)))
				cagla++;
		}
		cout<<"Case #"<<i+1<<": "<<cagla<<endl;
	}
	return 0;
}
 
 