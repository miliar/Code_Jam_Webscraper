#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

int i,j,k,l,A,B,m,n,t;
string s[4];
int a[10000000];

int palindrome(long long x){
	int a[15],n=0,i;
	if (x%10 == 0) return 0; 
	while (x>0){
		a[n]=x%10;
		x/=10;
		n++;	
	}
	int d = 1;
	for (i=0;i<n/2;i++){
		if (a[i]!=a[n-1-i]) {d=0;break;}
	}
	if (d) return 1; else return 0;
}

int main(){
	freopen("output.txt","w",stdout);
	for (i=1;i<10000000;i++){
		a[i] = a[i-1];
		if (palindrome(i) && palindrome(i*i)){
			a[i]++;
			//cout<<i<<"\n";		
		}
	}
	cin>>t;
	for (i=1;i<=t;i++){
		cin>>A>>B;
		cout<<"Case #"<<i<<": "<<a[(int)sqrt(B+0.1)]-a[(int)sqrt(A-0.1)]<<"\n";
	}
	return 0;
}
