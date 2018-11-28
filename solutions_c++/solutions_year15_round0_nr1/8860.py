#include<iostream>
#include<fstream>

using namespace std;

int main()
{
	int t;
	ifstream fin;
	ofstream fout;
	fin.open("input.txt");
	fout.open("output.txt");
	fin>>t;
	int temp;
	temp=t;
	while(t--)
	{
		int n;
		int sum=0;
		fin>>n;
		int arr[n] , cum[n];
		char inp;
		int i=0;
		while(i<=n)
		{
			fin>>inp;
			arr[i] = int(inp-48);
			i++;
		}
		cum[0] = arr[0];
		for(int i = 1; i<=n ;i++)
		{
			if(cum[i-1] >= i)
			{
				cum[i] = cum[i-1]+ arr[i];
			}
			else
			{
				sum+= i - cum[i-1];
				cum[i-1] = i;
				cum[i] = cum[i-1]+ arr[i];
			}
			
		}
		fout<<"Case #"<<temp-t<<": "<<sum<<"\n";
		
	}
	return 0;
}




