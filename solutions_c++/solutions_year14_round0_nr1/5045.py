#include<cstdio>
#include <iostream>
#include <cstring>
using namespace std;

int count = 0;
	
int** l;
int firstAnswer = 0;
int secondAnswer = 0;
int *f;
int *s;
int* output;

void readCards(int d)
{
	int n;
	if(d == 0)
	{
		for(n = 0;n<4;n++)
		{
			f[n] = l[firstAnswer-1][n];
		}
	}
	else
	{
		for(n = 0;n<4;n++)
		{
			s[n] = l[secondAnswer-1][n];
		}
		  
	}
}

void getAnswer(int k)
{
	int m, o;
	bool multiple = false;
	bool gotAnswer = false;
	for(m=0;m<4;m++)
	{
		for(o=0;o<4;o++)
		{
			if(f[m] == s[o])
			{
				if(!multiple)
				{
					output[k] = f[m];
					multiple = true;
					gotAnswer = true;
				}
				else
				{
					output[k] = 20;
				}
			}
		  
		}
	}
	if(output[k] == 0)
		output[k] = 30;
}

int main(){
	int t;
	int temp;
	int i, j,k=0;
	l = new int*[4];
	f = new int[4];
	s = new int[4];
	for(int i=0;i<4;i++)
		l[i] = new int [4];
	cin >> t;
	temp = t;
	output = new int[temp];
	//a = new char[t];
	while(t--)
	{
		//draw()
		cin >> firstAnswer;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin >> l[i][j] ;
			}
		}
		readCards(0);
		cin >> secondAnswer;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin >> l[i][j] ;
			}
		}
		readCards(1);
		getAnswer(k++);
	}
	
	k = 0;
	while(temp--)
	{
		if(output[k] == 20)
			cout << "Case #" << k+1 << ": Bad magician!" << endl;
		else if (output[k] == 30)
			cout << "Case #" << k+1 << ": Volunteer cheated!" << endl; 
		else cout << "Case #" << k+1 << ": " << output[k] << endl; 
		
		k++;
	}

	
	return 0;
}
