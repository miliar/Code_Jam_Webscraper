#include <iostream>
#include<math.h>
using namespace std;

long long reverse(long long n)
{
	long long b = 0;
	long long a;
	while(n>0){
		a = n%10;
		b = b * 10 + a;
		n = n/10;
	}
	return b;
}

long long IsPalindrone(long long n)
{
	long long a = reverse(n);
	if(a == n){
	//	cout<<"found "<<a;
		return 1;
	}
	else{
		return 0;
	}
}

int main()
{
	long long n;
	cin >> n;
//	cout<<"reverse = "<<reverse(n);
	long long count=0;
	long long i,a,b,c,j;
	for(i=0;i<n;i++){
		cin >> a >> b;
		count=0;
		c = sqrt(a);
		if( c*c != a ){
			a = c + 1;
		}
		else{
			a = c;
		}
		b = sqrt(b);
		for(j=a;j<=b;j++){
			if(IsPalindrone(j)&&IsPalindrone(j*j)){
				count++;
			//	cout<< "num = "<<j;
			}
		}
		cout<<"Case #"<<i+1<<": "<<count<<"\n";
	}
}
