#include<cstdio>
#include <iostream>
#include <cstring>
#include <iomanip>
using namespace std;

int count = 0;
int** output;
int size, remaining;
double* naomi;
double* ken;

int naomiPoint;
int kenPoint;
bool roundEnd;
	

void war()
{
	int i, j;
	double swap;
	double naomiTemp[size], kenTemp[size];
	roundEnd = false;
	naomiPoint = 0;
	kenPoint = 0;
	
	for(i=0;i<size;i++)
	{
		naomiTemp[i] = naomi[i];
		kenTemp[i] = ken[i];
	}
	      
	for(i=0;i<size-1;i++)
		for(j=i+1;j<size;j++)
		{
			if(naomiTemp[i] > naomiTemp[j])
			{
				swap = naomiTemp[i];
				naomiTemp[i] = naomiTemp[j];
				naomiTemp[j] = swap;
			}
			if(kenTemp[i] > kenTemp[j])
			{
				swap = kenTemp[i];
				kenTemp[i] = kenTemp[j];
				kenTemp[j] = swap;
			}
		}
	  
	for(i=0;i<size;i++)
	{
		for(j=0;j<size;j++)
		{
			if(kenTemp[j] != 0.0)
			{
				if(naomiTemp[i] < kenTemp[j])
				{
					naomiTemp[i] = 0.0;
					kenTemp[j] = 0.0;
					kenPoint++;
					roundEnd = true;
					break;
				}			  
			}
		}
		if(!roundEnd)
		{
			naomiTemp[i] = 0.0;
			kenTemp[i] = 0.0;
			naomiPoint++;		
		}
		roundEnd = false;	
	}
	
	//cout << naomiPoint << endl;
	output[count][0] = naomiPoint;
}

void deceitfulWar()
{
	int i, j, deceive = 0, k=0;
	double swap;
	double naomiTemp[size], kenTemp[size];
	roundEnd = false;
	naomiPoint = 0;
	kenPoint = 0;
	
	for(i=0;i<size;i++)
	{
		naomiTemp[i] = naomi[i];
		kenTemp[i] = ken[i];
	}
	      
	for(i=0;i<size-1;i++)
		for(j=i+1;j<size;j++)
		{
			if(naomiTemp[i] < naomiTemp[j])
			{
				swap = naomiTemp[i];
				naomiTemp[i] = naomiTemp[j];
				naomiTemp[j] = swap;
			}
			if(kenTemp[i]  > kenTemp[j])
			{
				swap = kenTemp[i];
				kenTemp[i] = kenTemp[j];
				kenTemp[j] = swap;
			}
		}
	  
	  
	for(i=0;i<size;i++)
		cout << naomiTemp[i] << "   " << kenTemp[i] << endl;
	for(i=size-1;i>=0;i--)
	{
		for(j=0;j<size;j++)
		{
			if(kenTemp[j] != 0.0)
				if(naomiTemp[i] > kenTemp[j])
				{
					deceive++;
					break;
				}
		}
		cout << deceive << endl;
		if(deceive > 0)
		{
			naomiTemp[i] = 0.0;
			kenTemp[j] = 0.0;
			naomiPoint++;	
		}
		else
		{
			naomiTemp[i] = 0.0;
			kenTemp[j] = 0.0;
			kenPoint++;
		  
		}
		deceive = 0;
		k++;
	}
	k  = 0;
	output[count][1] = naomiPoint;
}

int main(){
	int t;
	int temp;
	int i, j,k=0;
		
	cin >> t;
	temp = t;
	output = new int*[t];
	for(i=0;i<t;i++)
		output[i] = new int[2];
	while(t--)
	{
		cin >> size;
		
		remaining = size;
		naomi = new double[size];
		ken = new double[size];
		for(i=0;i<size;i++)
		{
			cin >> fixed >> setprecision(5) >> naomi[i];
		}
		for(i=0;i<size;i++)
		{
			cin >> fixed >> setprecision(5) >> ken[i];
		}		
		war();
		deceitfulWar();
		count++;
	}
	
	k = 0;
	while(temp--)
	{
		cout << "Case #" << k+1 << ": " << output[k][1] << " " << output[k][0] << endl;
		k++;
	}

	
	return 0;
}
