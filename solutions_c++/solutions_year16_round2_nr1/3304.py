#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <vector>
using namespace std;

string findNumber(string input){
	// int zero, one, two, three, four, five, six, seven, eight, nine;
	int zero =0;
	int one = 0;
	int two = 0;
	int three =0;
	int four =0;
	int five = 0;
	int six =0;
	int seven =0;
	int eight =0;
	int nine =0;

	for (int i=0;i<input.length();i++){
		// switch (input[i]){
		// 	case 'Z': zero++;
		// 				break;

		// 	case 'W':two++;
		// 				break;

		// 	case 'G':eight++;
		// 				break;

		// 	case 'X': six++;
		// 				break;

		// 	case 'U':	four++;
		// 				break;
		// 	case 'H' : three++;	//three-eight;
		// 				break;
		// 	case 'F': five++;  //five-four;
		// 				break;
		// 	case 'S': seven++; //seven-six;
		// 				break;
		// 	case 'I': nine++; //nine-six-five-eight;
		// 				break;
		// 	case 'N': one++; //one -seven-2*nine
		// 				break;


			
		// }
		if (input[i]=='Z'){
			zero++;
		}
		else if(input[i]=='W'){
			two++;
		}
		else if(input[i]=='G'){
			eight++;
		}
		else if(input[i]=='X'){
			six++;
		}
		else if(input[i]=='U'){
			four++;
		}
		else if(input[i]=='H'){
			three++;
		}
		else if(input[i]=='F'){
			five++;
		}
		else if(input[i]=='S'){
			seven++;
		}
		else if(input[i]=='I'){
			nine++;
		}
		else if(input[i]=='N'){
			one++;
		}

	}
	three = three-eight;
	five = five-four;
	seven = seven-six;
	nine = nine-six-five-eight;
	one = one -seven -(2*nine);
	string result = " ";
	// cout << "yahan\n";
	// cout << zero << endl;
	for (int i = 0; i < zero; ++i)
	{
		result = result+"0";
		// cout << "zero"<< endl;
	}
	for (int i = 0; i < one; ++i)
	{
		/* code */
		result = result+"1";
	}
	for (int i = 0; i < two; ++i)
	{
		/* code */
		result = result+"2";
	}
	for (int i = 0; i < three; ++i)
	{
		/* code */
		result = result+"3";
	}
	for (int i = 0; i < four; ++i)
	{
		/* code */
		result = result+"4";
	}
	for (int i = 0; i < five; ++i)
	{
		/* code */
		result = result+"5";
	}
	for (int i = 0; i < six; ++i)
	{
		/* code */
		result = result+"6";
	}
	for (int i = 0; i < seven; ++i)
	{
		/* code */
		result = result+"7";
	}
	for (int i = 0; i < eight; ++i)
	{
		/* code */
		result = result+"8";
	}
	for (int i = 0; i < nine; ++i)
	{
		/* code */
		result = result+"9";
	}


	// cout<< "wahan\n";
	string final = "";
	for (int i=1;i<result.length();i++){
		final = final + result[i];
	}
	return final;
	}
	


int main(){
	FILE* in = freopen("A-large.in", "r", stdin);
	FILE* out = freopen("A-large.out", "w", stdout);
	string a;
	int tries;
	cin >>tries;
	for (int i=0;i<tries;i++){
	cin >> a;

	cout << "Case #" << i+1 << ": " << findNumber(a) << endl;
	}
}