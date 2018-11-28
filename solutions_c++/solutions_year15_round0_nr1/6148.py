#include <iostream>
#include <cmath>
#include <vector>
#include <string>
#include <cstdlib>

using namespace std;

int main()
{
    int T;
	cin>>T;
	//vector <int> S;
	long int Smax, tmp, Sum=0;
	long int count = 0;
	long int result[T];
	string input;
    for(int i=0; i<T; i++)
    {
		cin >> Smax;
		long int S[Smax + 1];
		for(int j=0; j<=Smax; j++)
		{
			S[j] = 0;
		}
		cin>>input;
		//cout << input[0];
		for(int j=0; j<input.length(); j++)
		{
			S[j] = input[j] - 48;
		}
		//sum of previous elements of array is >= its index
		for(int j=1; j<=Smax; j++)
		{
			Sum = Sum + S[j-1];
			//cout<<"hello";
			if(Sum < j && S[j] != 0)
			{
				count = count + (j - Sum);
				Sum = j;
				//cout<<"hello";
			}
		}
		result[i] = count;
		
		count = 0;
		//S.clear();
		input = "";
		Sum = 0;
    }
    
    for(int i=0; i<T; i++)
    {
    	cout<<"Case #"<<i+1<<": "<<result[i]<<endl;
    }
}
