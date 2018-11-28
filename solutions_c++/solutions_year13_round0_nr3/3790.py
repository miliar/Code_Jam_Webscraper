#include <iostream.h>
#include <fstream.h>

// Code Jam 2013
// Qualification Round
// Problem C. Fair and Square
// For small data sets

bool ispalindrome(int num)
{
	int reverse;
	int temp;
	temp = num;
	
	reverse = 0;
	while ( temp > 0 )
	{
		reverse = reverse * 10;
		reverse = reverse + temp%10;
		temp = temp/10;
	}
	
	if ( reverse == num )
	{
		return true;
	}
	else
	{
		return false;
	}
}

int main(int argc, char *argv[])
{
	int T;
	int t;
	
	int A;
	int a;
	int B;
	int b;
	
	int answer;
	
	ifstream inFile;
	
	//inFile.open("test.in");
	if ( argc < 2 )
	{
		cout << "No input file given!" << endl;
		exit(1);
	}
	inFile.open(argv[1]);
	if ( !inFile )
	{
		cout << "Error opening file!" << endl;
		exit(1);
	}
	
	inFile >> T;
	
	for (t=0;t<T;t++)
	{
		inFile >> A;
		inFile >> B;
		
		answer = 0;
		for (int i=A;i<=B;i++)
		{
			if ( ispalindrome(i) )
			{
				int j = sqrt(i);
				if ( (j*j == i) && ispalindrome (j) )
				{
					answer++;
				}
			}
		}
		
		
		
		cout << "Case #" << t+1 << ": " << answer << endl;
	}
		
		
	
	inFile.close();
	return 0;
}