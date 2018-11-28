//**********LOGIC**********
//range - a to b
//find sqrt of a -> Asqrt
//do
//start incrementing from Asqrt
//find square of Asqrt
//if square is more than b, then break
//see if Asqrt is palindrome
//if yes, see if its square is also palindrome
//if yes, then increment counter
//



#include <iostream>
#include <fstream>
#include <cmath>

using namespace std;

bool checkPalindrome(int n)
{
	int rem, sum, temp;
	temp = n;
	sum = 0;
	while(n) {
		rem = n % 10;
		sum = sum*10 + rem;
		n = n / 10;
	}
	if(sum == temp)
		return true;
	else
		return false;
}

int main(int argc, char **argv)
{
	ifstream input("C-small-attempt0.in");
	ofstream output("output3");
	int i, n, a, b, root, square, palcount;
	i = 0;
	input >> n;
	//cin>>n;
	while(++i <= n) {
		input >> a;
		input >> b;
		//cin>>a>>b;
		palcount = 0;
		root = (int)sqrt(a);
		while(1) {
			square = root * root;
			if(square > b)
				break;
			if(square >= a && square <=b)
				if(checkPalindrome(root) && checkPalindrome(square))
					palcount++;
			root++;
		}
		output << "Case #"<<i<<": "<<palcount<<"\n";
		//cout << "Case #"<<i<<": "<<palcount<<"\n";
	}
	output.close();
	input.close();
	return 0;
}

