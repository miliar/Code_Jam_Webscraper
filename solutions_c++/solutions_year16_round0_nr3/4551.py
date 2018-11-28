#include<cstdio>
#include<iostream>
#include<cmath>

using namespace std; 

double aux;
int value[60];
int T;
int N;
int J;
long long int bases[60];
long long int ct;
long long int myPow[60];
long long int result	[30];
long long int toPrint[30];
long long int total;

void check()
{
	if(total == J)
	{
		return;
	}
	
	for(int k=0 ; k<=8 ; k++)
	{
		bool flag = false;
		for(int it=2 ; it<= sqrt(result[k]) ; it++)
		{
			if(result[k]%(long long int)it == 0)
			{
				toPrint[k] = it;
				flag = true;
				break;
			}
		}
		
		if(!flag)
		{
			return;
		}
	}
	
	for(int k=N-1 ; k>=0 ; k--)
	{
		cout << value[k];
	}
	cout << " "; 
	for(int k=0 ; k<=8 ; k++)
	{
		cout << toPrint[k] << " ";
	}
	total ++;
	cout << endl;
}

void ctrNum(int level, int max,
			long long int pot2, long long int res2,
			long long int pot3, long long int res3, 
			long long int pot4, long long int res4,
			long long int pot5, long long int res5,
			long long int pot6, long long int res6,
			long long int pot7, long long int res7, 
			long long int pot8, long long int res8,
			long long int pot9, long long int res9,
			long long int pot10, long long int res10)
{
	if(total == J)
	{
		return;
	}
	
	if(level > max)
	{	
		result[0] = res2+pot2;
		result[1] = res3+pot3;
		result[2] = res4+pot4;
		result[3] = res5+pot5;
		result[4] = res6+pot6;
		result[5] = res7+pot7;
		result[6] = res8+pot8;
		result[7] = res9+pot9;
		result[8] = res10+pot10;
		check();
		
		//cout << "\n" << endl;
			
		ct ++;
		return;
	}
	
	
	ctrNum(level+1, max, 
		pot2*2, res2,
		pot3*3, res3,
		pot4*4, res4,
		pot5*5, res5,
		pot6*6, res6,
		pot7*7, res7,
		pot8*8, res8,
		pot9*9, res9,
		pot10*10, res10);
	
	value[level] = 1;
	ctrNum(level+1, max, 
		pot2*2, res2+pot2,
		pot3*3, res3+pot3,
		pot4*4, res4+pot4,
		pot5*5, res5+pot5,
		pot6*6, res6+pot6,
		pot7*7, res7+pot7,
		pot8*8, res8+pot8,
		pot9*9, res9+pot9,
		pot10*10, res10+pot10);
	value[level] = 0;
	
}

int main()
{
	for(int k=0 ; k<33 ; k++)
	{
		value[k] = 0;
		bases[k] = 1;
		myPow[k] = 1;
	}
	
	cin >> T;
	
	for(int k=0 ; k<T ; k++)
	{
		cin >> N >> J;
		
		ct = 0;
		value[0] = value[N-1] = 1;
		total = 0;
		
		cout << "Case #" << k+1 << ":" << endl;
		ctrNum(1, N-2, 
				2, 1,
				3, 1,
				4, 1,
				5, 1,
				6, 1,
				7, 1,
				8, 1,
				9, 1,
				10, 1);
		
	}
return 0;
}