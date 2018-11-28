#include<stdio.h>
#include<iostream>
#include<cstring>
using namespace std;
void fillArr(int *arr,int tempNum);
bool checkIfDone(int *arr);
int main(void)
{
	
	freopen("input.in","r",stdin);
	freopen("output.out","w",stdout);
	int testCases;
	cin >> testCases;
	int arr[10]={0,0,0,0,0,0,0,0,0,0};
	int firstNum;
	int totalCalculated=0;
	bool isDone=true;
	for(int i=0;i<testCases;i++)
	{
		isDone=true;
		cin >> firstNum;
		int tempNum,a,b;
		if(firstNum==0) cout << "Case #"<<(i+1)<<": INSOMNIA"<<endl;
		else 
		{
			tempNum=firstNum;
			memset(arr,true,sizeof(arr));
			a=1;
			while (isDone)
			{
				fillArr(arr,tempNum);
				if( checkIfDone(arr) ) 
				{				
					cout << "Case #"<<(i+1)<<": "<<tempNum<<endl;
					break;
				}
				tempNum=firstNum*++a;
			}
		}
	}
	return 0;
}

void fillArr(int *arr,int tempNum)
{
	int x = tempNum;
	int rem;
	while(x !=0 )
	{
		rem = x%10;
		x=x/10;
		arr[rem]=1;
	}
}

bool checkIfDone(int *arr)
{
	for(int i=0;i<10;i++)
	{
		if (arr[i]!=1) return false;
	}
	return true;
}


