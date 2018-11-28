
#include <string.h>
#include <iostream>
#include <math.h>

using namespace std;

int is_square(int n){
	int root =round(sqrt(n));
	
	if (n<0)
		return 0;
	return n == root*root;
}

int is_fair(int n){
	int tmp = n;
	int sum =0, rem = 0;
	while( n!=0){
		rem = n%10;
		n = n/10;
		sum = sum*10 + rem;
	}
	if (sum == tmp){
		return 1;
	}else{
		return 0;
	}
}

int is_fair_and_square(int n){
	if(is_square(n)){
		int root = round(sqrt(n));
		if(is_fair(root)){
			return 1;
		}else{
			return 0;
		}
	}else{
		return 0;
	}
}


int main(){
	unsigned int n_cases = 0, l=0, u=0, c=0, r=0;
	int i;
	char* str;
	string tmp;
	int n_bytes = 100;
	cin>>n_cases;
	getline(cin, tmp);

	for (i = 1; i <= n_cases; i++){
		cin >>l>>u;
		r = 0;
		c  = l;
		while(c != u){
			if(is_fair_and_square(c) && is_fair(c)){
				r++;
				
			}
			c++;
		}
		if(is_fair_and_square(c) && is_fair(c)){
				r++;
		}
		cout<<"Case #"<<i<<": "<<r<<endl;
	}



	return 0;
}








