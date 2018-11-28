#include<cstdio>
#include <iostream>
#include <cstring>
#include <string>
#include <math.h>
#define GETBYTE(x,N) ((x >> (8*N)) & 0xff)
using namespace std;

int count = 0;
	
int* output;
int A, B, K;
string bA, bB;
int  sum;

void lottery()
{
}

string DecimalToBinary(int dec)
{
	  if ( dec == 0 ) return "0";
	  if ( dec == 1 ) return "1";

	  if ( dec % 2 == 0 )
	      return DecimalToBinary(dec / 2) + "0";
	  else
	      return DecimalToBinary(dec / 2) + "1";
}

void addition(string b1, string b2)
{
	sum = 0;
	int carry = 0;
	int i;
	int j = 0;
	//cout << b1 << "        " << b2 << endl;
	for(i=b1.size()-1;i>=0;i--)
	{
		if(b1.at(i) == '1' && b2.at(i) == '1')
		{
			sum = sum + pow(2, j);
		}
		j++;
	}
}
int main(){
	int t;
	int temp;
	int p = 0;
	cin >> t;
	temp = t;
	//a = new char[t]
	output = new int[t];
	while(t--)
	{
		//draw()
		cin >> A >> B >> K;
		//cout << bA << "            " << bB << endl;
		for(int i=0;i<A;i++)
			for(int j=0;j<B;j++)
			{		
				
				bA = DecimalToBinary(i);
				bB = DecimalToBinary(j);
				//cout << i << "            " << j << endl;
				while(bA.size() != bB.size())
				{
					if(bA.size() > bB.size())
					{
						for(int k=0;k<bA.size() - bB.size();k++)
						{
							bB = "0" + bB;
						}
					}
					else if(bA.size() < bB.size())		  
					{
						for(int l=0;l<bB.size() - bA.size();l++)
						{
							bA = "0" + bA;
						}
					}
				}
				addition(bA, bB);	
				//cout << "Here" << endl;
				//cout << bA << "              " << bB << "               " << sum << endl;
				if(sum < K)
				{
					count++;
				}
			}
		//cout << count << endl;
		output[p++] = count;
		count = 0;
	}
	
	int q = 0;
	while(temp--)
	{
		cout << "Case #" << q+1 << ": " << output[q] << endl;
		q++;
	}
	

	
	return 0;
}
