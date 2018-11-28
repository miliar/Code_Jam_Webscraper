#include <iostream>
#include <vector>
using namespace std;

int calculate(vector<int> &seen, long long n){
	int counter = 0;
	while(n>0){
		long long tmp = n%10;
		if(seen[tmp] == 0){
			seen[tmp]++;
			counter++;
		}
		n /= 10;
	}
	return counter;
}

int main(){
	//freopen("in1.in", "r", stdin);
	//freopen("myout.out", "w", stdout);
	int T;
	cin >> T;
	
	for(int i = 1; i <= T; ++i){
		vector<int> seen(10,0);
		long long n;
		cin >> n;
		int counter = 0;
		
		long long tmp = n;
		if(n == 0 || tmp < 0){
			cout << "Case #" << i << ": INSOMNIA" <<endl;
	    }
		else{
			for(int j = 1; ; ++j){
				tmp = j * n;
				if(tmp < 0){
					cout << "Case #" << i << ": INSOMNIA" <<endl;
				    break;
				}
				counter += calculate(seen, tmp); 
			    if(counter >= 10){
			    	cout << "Case #" << i << ": " << tmp <<endl;
				    break;
				}
			}
		}
		
	}
	return 0;
}
