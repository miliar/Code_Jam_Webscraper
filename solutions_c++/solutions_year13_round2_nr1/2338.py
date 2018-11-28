#include <stdlib.h>
#include <stdio.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <math.h>
#include <sstream>

using namespace std;

int n, a, b,c ,d,x,y,M;
long long N,k,l;
#define _CRT_SECURE_NO_WARNINGS
#define For(i,a,b) for (int i(a),_b(b); i < _b; ++i)


int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}


int main() {
	ifstream myfile;
	myfile.open("input.txt");
	ofstream myfile2;
	myfile2.open("output.txt");
	
	myfile >> N;
	
	for (long long u = 0; u < N; u++) {

		myfile >> a>>b;
		
		int *arr = new int[b];

		For(i,0,b)
			myfile >> arr[i];
		qsort (arr, b, sizeof(int), compare);
		int num=0;
		For(i,0,b){
			if(arr[i]<a)
				a+= arr[i];
			//bool mark=true;
			else{
				int t;
				int count=0;
				for(double j=i;j<b;j++)
				{
					t=pow(2,j-i);
					int p=j;
					if((2*t*a-2*t-1)<=arr[i])
					{
						count++;
					}
					else 
						break;
				}

				if(count==b-i)
				{
					num+= b-i;
					break;
				}
				a += a-1;
				num++;
				i--;
				
			}
			if(a==1)
			{
				num=b;
				break;
			}
		}
		
		myfile2<<"Case #"<<u+1<<": "<<num<<endl;
		//cout<<"Case #"<<u+1<<": "<<num<<endl;
		
	}
	system("pause");
}