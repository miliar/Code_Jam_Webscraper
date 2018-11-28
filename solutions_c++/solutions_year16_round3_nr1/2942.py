#include<iostream>
using namespace std;

string b = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

bool checksatisfy(int a[], int n)
{
	bool answer = true;
	int sum = 0;
	for(int i = 0; i<n; i++)
	{
		sum = sum + a[i];
	}
	float newsum = sum / 2;
	for(int i = 0; i<n; i++)
	{
		if(a[i] > newsum)
		{
			answer = false;
			break;
		}
	}
	return answer;
}

int main()
{
int t;
cin>>t;
for(int l = 0; l<t; l++)
{
cout<<"Case #"<<l+1<<":"<<" ";
	int n;
	cin>>n;
	int a[n];
	for(int i = 0; i<n; i++)
	{
		cin>>a[i];
	}
	int sum = 0;
	for(int i = 0; i<n; i++)
	{
		sum = sum + a[i];
	}
	for(int i = 0; i<sum; i++)
	{
		for(int j = 0; j<n; j++)
		{
			if(a[j] != 0)
			{
				a[j] = a[j] - 1;
				if(checksatisfy(a,n))
				{
					cout<<b[j]<<" ";
					break;
				}	
				else
				{
					a[j] = a[j] + 1;	
				}
			}
			for(int k = 0; k<n; k++)
			{
				if(a[k] != 0)
				{
					a[j] = a[j] - 1 ;
					a[k] = a[k] - 1 ;
					if(checksatisfy(a,n))
					{
						cout<<b[j]<<b[k]<<" ";
						break;
					}	
					else
					{
						a[j] = a[j] + 1;	
						a[k] = a[k] + 1;
					}
				}
			}
		}
	}
cout<<"\n";
}		
}
