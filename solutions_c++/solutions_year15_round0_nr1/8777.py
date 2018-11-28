#include <iostream>
using namespace std;

int count(int shyness[1000], int S){
	int c = 0;
	for(int s=0;s<=S;++s){
		if(c >= s){
			c+=shyness[s];
			
			if(s == S){
				c *= -1;
			}
		}
	}
	return c;
}

int main(){
	int N;
	cin >> N;
	for(int n=0;n<N;++n){
		cout << "Case #" << n+1 << ": ";
		
		int S;
		cin >> S;
		int shyness[1001];
		string shyness_s;
		cin >> shyness_s;
		
		for(int s=0;s<=S;++s){
			shyness[s] = shyness_s[s] - '0';
		}
		
		int add = 0;
		
		while(true){
			int c = count(shyness, S);
			if(c < 0){
				break;
			}else{
				++add;
				++shyness[0];
			}
		}
		
		cout << add << endl;
	}
}