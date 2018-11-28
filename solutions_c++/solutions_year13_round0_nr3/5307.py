/************************************************************************
* Problem ID: 
*************************************************************************
*  Rahul Kushwaha
*************************************************************************
* Additional Information [Bookname , Links, etc.]
*
*************************************************************************/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <utility>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <ctime>
#include <string.h>

#define FOR(X) for(int i=0; i<(X);i++)
#define FOR_R(X) for( int i= (X);i>0;i--)
#define MAX(X,Y) (X) > (Y) ? (X) : (Y)
#define MIN(X,Y) (X) < (Y) ? (X) : (Y)
#define SWAP_XOR(X,Y) (X)=(X)^(Y);(Y)=(X)^(Y);X=(X)^(Y);
#define SWAP(X,Y) { int temp = (X); (X)= (Y); (Y) = temp;}

typedef long long LL;
typedef long double LD;

using namespace std;
int NumDigits(int x)  
{  
	x = abs(x);  
	return (x < 10 ? 1 :   
		(x < 100 ? 2 :   
		(x < 1000 ? 3 :   
		(x < 10000 ? 4 :   
		(x < 100000 ? 5 :   
		(x < 1000000 ? 6 :   
		(x < 10000000 ? 7 :  
		(x < 100000000 ? 8 :  
		(x < 1000000000 ? 9 :  
		10)))))))));  
}
bool isPalindrome(int num)
{
	int reverse = 0;
	int counter = NumDigits(num) - 1;
	int num_ = num;
	while(num_  > 0)
	{
		reverse += ( num_ % 10 ) * pow(10, counter);
		num_ /= 10;
		counter --;
	}
	return num == reverse;
}
bool elements[1001] = {0};
void GenerateFairAndSquare()
{
	for(int i = 1; i < 32; i++ )
	{
		int num = i * i;
		if( isPalindrome(i) && isPalindrome(num))
		{
			elements[ num]  = true;
		}
	}
}

int main()
{
	//freopen("Input.txt", "r", stdin);
	//freopen("Output.txt", "w", stdout);
	int testCases;
	scanf("%d",&testCases);
	GenerateFairAndSquare();
	FOR(testCases)
	{
		int A,B;
		scanf("%d%d", &A, &B);
		int result  =0;
		for(int j = A; j <= B ; j++)
		{
			if(elements[j])
			{
				result++;
			}
		}
		cout<<"Case #"<<i + 1<<": " << result<<endl;
	}						   
	//fclose(stdin);
	//fclose(stdout);
	return 0; 
}