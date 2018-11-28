#include <iostream>  
#include <fstream> 
using namespace std; 
int digits[10];
int Rob(int n, int index);
int main() 
{
	fstream f;
	f.open("Input.in");
	int n,t;
	f >> t;
	for (int i = 0; i < t; i++)
	{
		for (int j = 0; j < 10; j++)
		digits[j]=0;
		f >> n;
		Rob(n,i);
	}
	f.close();
	system("pause");
	
}

int Rob(int n, int index)
{
	ofstream f("output.txt", ios_base::app);
	//fstream f;
	//f.open("output.txt");
	int real_n = n;
	int i=1,x=1;
	int perev=0;
	if (n == 0)
	{

		f << "Case #" << index + 1 << ": INSOMNIA\n";
	}
	else
	{
		while (perev==0)
		{
			n = real_n*i;
			i++;
			while (n != 0)
			{
				digits[n % (10)] = 1;
				n = (int) (n / (10));
			}
			x = 1;
			perev = 1;
			for (int j = 0; j < 10; j++)
				if (digits[j]==0) perev=0;
		}
		f << "Case #" << index + 1 << ": " << real_n*(i - 1) << endl;
	}
	f.close();
	return 0;
}