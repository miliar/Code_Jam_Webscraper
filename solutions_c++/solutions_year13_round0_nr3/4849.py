#include<iostream>
#include<algorithm>
#include<cmath>
#include<cstdio>



using namespace std;


long long int palin(long long int num){
	long long int r,num1,dig,rev=0;
	
	num1 = num;
	
	while(num > 0){
		dig = num % 10;
      	rev = rev * 10 + dig;
      	num = num / 10;
	}
	if(rev == num1){
		return 1;
	}
	else{
		return 0;
	}
}


int main()
{
	long long int a,i,count,b,c,j,a3,a1,a2;
	freopen ("myfile.txt","w",stdout);
	cin >> a;
	for(j=0;j<a;j++){
		count = 0;
		cin >> b >> c;
		a1 = sqrt(b);
		a2 = sqrt(c);
		
		for(i=a1;i<=a2;i++){
			a3 = i * i;
			if(a3 >= b && a3 <= c){
				if(palin(i) == 1 && palin(a3) == 1){
					count++;
				}
			}
		}
			cout << "Case #"<<(j+1) << ": "<<count <<endl;
	}
	return 0;
}
