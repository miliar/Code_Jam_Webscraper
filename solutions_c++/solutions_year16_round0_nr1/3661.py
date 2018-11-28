#include <iostream>
#include <sstream>
using namespace std;

int main(){
	int test_cases;
	cin >> test_cases;
	int temp = test_cases;
	while(test_cases--){
		string result;
		long int n;
		int check[10] = {0};
		int count = 0;
		cin >> n;
		long int original_n = n;
		if(n!=0){
			int stop = 0;
			for (long int i=1;stop==0;i++)
			{
				n = original_n*i;
				long int temp1 = n;
				for(;temp1;){
					int remaindr = temp1%10;
					temp1 = temp1/10;

					if(check[remaindr] == 0){
						count++;
						check[remaindr]++;
					}
					if(count==10)
						stop = 1;
				}
			}

			stringstream ss;
			ss << n;
			ss >> result;

		}
		else if( n==0 )
			result = "INSOMNIA";

		cout << "Case #" << temp-test_cases << ": " << result << endl;

	}

	return 0;
}