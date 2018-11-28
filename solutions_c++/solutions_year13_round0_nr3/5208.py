#include <iostream>
#include <fstream>

using namespace std;

bool isPalindrome(long long int data);

int main(){
	ifstream input;
	ofstream output;
	input.open("C-small-attempt3.in");
	output.open("output.txt");

	int test_num;
	input>>test_num;

	for(int qwer=0; qwer<test_num; qwer++){
		long long int a, b, data;
		int count=0;
		input>>a>>b;
		for(long long int loop=1; loop<10000000; loop++){
			if(isPalindrome(loop)){
				data = loop*loop;
				if(a<=data && data<=b){
					if(isPalindrome(data)){
						cout<<data<<endl;
						count++;
					}
				}
				else if(data > b)
					break;
			}
		}
		output<<"Case #"<<qwer+1<<": "<<count<<endl;
	}

	input.close();

	return 0;
}

bool isPalindrome(long long int data){
	long long int temp = data;
	long long int result = 0;

	while(temp != 0)
	{
		result = result*10 + temp%10;
		temp /= 10;
	}

	if(data == result)
		return true;
	else
		return false;
}