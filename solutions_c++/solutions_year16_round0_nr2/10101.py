#include <iostream>
#include <cstring>
using namespace std;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	long long int t,i,count = 0;
	char a[101];
	cin >> t;
	for (i = 0; i < t; i++)
	{
		count = 0;
		cin >> a;
		long long int p = strlen(a);
		for (long long int j = 0; j < p; ++j){
			if (j==0)
			{
			if (a[j] == '-')
			{
				while(a[j]=='-')
				{
					j++;
				}
				j--;
				count++;
			}
			}
			else if(a[j] == '-')
			{	
				while(a[j]=='-')
				{
					j++;
				}
				j--;
				count = count + 2;
			}
		
}
	cout << "Case #"<<i+1<<": "<<count<< endl;
}
}

