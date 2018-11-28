#include <iostream>
#include <string>
using namespace std;


int main() {
	
	int caseNum, num;
	cin>>caseNum;
	for(int i = 0; i<caseNum  ;i++)
	{
		cin>>num;
		if(num == 0) {
			cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
		}
		else {
			int counter = 10, arr[11], lastNumber = 0;
			for(int j = 0 ; j< 10; j++) {
				arr[j] = 1;
			}
			for(int j = num; counter>0 ;j+=num) {
				for(int k = j; k> 0 ; k/=10) {
					int digit = k%10;
					if(arr[digit] == 1) {
						arr[digit]--;
						counter--;
					}
				}
				if(counter==0) {
					lastNumber = j;
				}
				
			}
			if(counter <= 0) {
				cout<<"Case #"<<i+1<<": "<<lastNumber<<endl;
			}
		}
	}
	// your code goes here
	return 0;
}