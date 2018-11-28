#include<iostream>
#include<string.h>
using namespace std;
//header file from :  http://askubuntu.com/questions/481807/how-to-install-g-in-ubuntu-14-04
int main(int argc, char *argv[])
{
    int T;
	cin>>T;
	string input;
	int counter = 0;
	int i,j = 0;
	for ( i = 1; i <= T; i++) {
		cin>>input;
		int counter = 0;		
		for (j = 0; j < input.length()-1; j++) {
			char y = input[j];
			char y1 =  input[j+1];
			if(y == '-' && y1 == '+')
				counter++;
			if(y == '+' && y1 == '-')
				counter++;
		}
		if(counter == 0 && input[j] == '+')
		{cout<<"Case #"<<i<<": 0"<<endl;
		continue;
		}
		if(input[j] == '-')
			++counter;
		cout<<"Case #"<<i<<": "<<counter<<endl;			
	}

    return 0;
}
