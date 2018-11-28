using namespace std;
#include <iostream>
#include <cmath>
int palindrome(int number){
	int rev = 0, d;
	int abc = number;
	while(number > 0){
		d = number%10;
		rev = (10*rev)+d;
		number = number/10;
	}
	if(rev == abc){
		return 1;
	} else {
		return 0;
	}
}

int main(){
	int n, start[1000], end[1000], i, j;
	int count[1000], fair, square;
	cin>>n;
	for(i = 0; i<n; i++){
		cin>>start[i]>>end[i];
		count[i] = 0;
	}
	for(i = 0; i<n ;i++){
		for(j = start[i]; j<=end[i]; j++){
			fair = palindrome(j);
			if(floor(sqrt(j)) == sqrt(j)){
				square = palindrome(sqrt(j));
				if(fair && square){
					count[i]++;
				}
			}
		}
	}
	for(i = 0; i<n; i++){
		cout<<"Case #"<<i+1<<": "<<count[i]<<endl;
	}
	return 0;
}
