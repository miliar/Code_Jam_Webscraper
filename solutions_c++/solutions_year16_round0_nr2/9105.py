#include <iostream>
#include <string>
using namespace std;

int calculate(){
	string input;
	cin >> input;
	char temp = input[0];
	int i=0, ans = 0;
	while (i<input.size()){
		if (input[i]==temp){
			i++;
			continue;
		}
		else{
			temp = input[i];
			ans++;
			i++;
		}
	}

if((input[0]=='-'&& ans%2==0)||(input[0]=='+'&& ans%2==1))
	ans++;

	return ans;
}



int main () {
	int test, ans, i;
	cin >> test;

	for (i=0; i<test; i++){
		
		ans = calculate();
		cout <<"Case #"<<i+1<<": "<<ans<<endl; 
	}
}