#include <iostream>  
#include <fstream> 
using namespace std; 
int Rob(char n[101], int index);
int main() 
{
	fstream f;
	f.open("Input.in");
	int t;
	f >> t;
	char rad[101];
	for (int i = 0; i < t; i++)
	{
		f >> rad;
		Rob(rad,i);
	}
	f.close();
	system("pause");
	
}

int Rob(char n[101], int index)
{
	int sum,x=1;
	ofstream f("output.txt", ios_base::app);
	if (n[0]=='-')
	{
		sum = 1;
		x = 0;
	}
	else sum = 0;
	for (int j = 0; j < strlen(n); j++)
	{
		if (n[j] == '+') x=1;
		else if (x==1)
		{
			x = 0;
			sum += 2;
		}

	}
	f << "Case #" << index + 1 <<": " << sum << endl;
	f.close();
	return 0;
}