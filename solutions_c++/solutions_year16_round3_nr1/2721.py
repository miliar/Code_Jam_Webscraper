#include<iostream>
using namespace std;
int main()
{
	int t;
	cin >> t;
	for (int i = 0 ;i < t; i++)
	{
		cout << "Case #" << i+1 << ": ";
		int n;
		cin >>n;
		int arr[n];
		for (int j = 0; j < n; j ++)
		{
			cin >> arr[j];
		}
		long int max =  arr[0], a = 0, b = -1, count = 1;
		while(true)
		{
			max = arr[0];
			a = 0; b = -1; count = 1;
			for (int k = 1; k <n; k++)
			{
				if (arr[k] > max)
				{
					max = arr[k];
					a= k;
					b = -1;	
					count = 1; 
				}
				else if (max == arr[k])
				{
					count++;
					if (b == -1)
						b = k;
				}	
			}
			//cout << max << "max " << count << "count "<< endl;
			if (max == 0 ||max == 1)
			{
				if (max == 0)
					break;
				if(max == 1)
				{
					if (count %2 == 0)
					{
						int x = 0;
						for (int u =0; u < n; u++)
						{
							if (arr[u] == 1)
							{
								cout << (char)(u+65);
								x++;
								if (x == 2)
								{
									x = 0;
									cout << " ";
								}
							}
						}
					}
					else
					{
						int x = 0, y = 0;
						for (int u =0; u < n; u++)
						{
							if (arr[u] == 1)
							{
								if (y == 0)
								{
									cout << (char)(u+65) << " ";
									y = 1;
								}
								else
								{
									cout << (char)(u+65);
									x++;
									if (x == 2)
									{
										x = 0;
										cout << " ";
									}
								}
							}
						}
					}
					break;
				}
			}
			else
			{
				if (b == -1)
				{
					arr[a]-=2;
					cout << (char)(a+65) << (char)(a+65) << " ";
				}
				else
				{
					arr[a]-=1;
					arr[b]-=1;
					cout << (char)(a+65) << (char)(b+65) << " ";
				}
			}	
		} 
		cout<<endl;
	}
}
