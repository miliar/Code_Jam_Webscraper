#include <iostream>
#include <fstream>
#include <iomanip>
#include <vector>
#include <algorithm>

using namespace std;

int finished(int* a)
{
	for (int i=0; i<10; i++)
		if (a[i]==0) return 0;
	return 1;
}

int main()
{
	ifstream myfile;
	//myfile.open("testA.txt");
	myfile.open("A-large.in");

	int T;
	myfile >> T;
	
	for (int t=0; t<T; t++)
	{
		int N;
        myfile >> N;

		int digits[10]={0};
		int p = 1;
		if (N==0)
		{
		cout << "Case #" << t+1 << ": " << "INSOMNIA" <<"\n";
		}
		else
		{
	    while(!finished(digits))
		{
			int num=p*N;
			while (num!=0)
			{
		
			digits[num%10]=1;
			num=num/10;
			
			}
			p++;
		}



		
		cout << "Case #" << t+1 << ": " << (p-1)*N <<"\n";
		}
	} 
	
	myfile.close();
	return 0;	
}

