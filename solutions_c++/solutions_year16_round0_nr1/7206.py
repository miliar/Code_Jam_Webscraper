#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(){

	int t;
	cin >> t;
	long long n;
	for(int i=0;i<t;i++){
		cin >> n;
		long long current = n;
		vector<int> numbers;
		if(n == 0){
			cout << "Case #" << i+1 <<": INSOMNIA" << endl;
		}
		else {
			while(true){			
				long long temp = current;
				while(temp > 0){
					int rem = temp % 10;
					temp = temp / 10;
					if (find(numbers.begin(), numbers.end(), rem) == numbers.end())
						numbers.push_back(rem);

					
				}	
				if(numbers.size() == 10){
					cout << "Case #" << i+1 <<": " << current <<endl;
					break;	
				}
				else
					current += n;
			}
		}	
	} 
	return 0;
}
