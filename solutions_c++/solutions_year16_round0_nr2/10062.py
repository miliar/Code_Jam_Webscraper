#include <iostream>
#include <queue>
#include <list>
#include <vector>
#include <string>
#include <string.h>


using namespace std;
 long long int findAns(char stack[100]);
 char *flip(char *stack, int n);

int main()
{
	int testcase = 0;
	cin >> testcase;
	int i;
	char arr[100][100];
	int ans[100];
	for (i=0; i< testcase; i++)
	{
		cin >> arr[i];
		ans[i] = findAns(arr[i]);
 	}
    for (i=0; i< testcase; i++)
	{

		if(ans[i] >= 0) 
		{
			cout << "Case #" << i+1 << ": " << ans[i] << endl;
		}
 	}
 }
long long int findAns(char *stack)
{
 	bool flag = false;
 	int i;
 	int count = 0;
 	char copy[100];
 	int plus_count = 0; 
 	int len = strlen(stack);
 	while(len > 0)
 	{
 		
 		for(i = 0; i < strlen(stack); i++)
 		{
 			if(stack[i] == '+')
 			{
 				plus_count++;
 			}
 			else
 			{
 				break;
 			}
 		}
 		if(plus_count > 0 && plus_count != strlen(stack))
 		{
 			stack = flip(stack, plus_count);
 			count ++;
 		}
 		for(i = strlen(stack) - 1; i>=0; i-- )
 		{
 			if(stack[i] == '-')
 			{
 				stack = flip(stack, i+1);
 				count ++;
 				break;
 			}
 		}
 		for(i = strlen(stack) - 1; i>=0; i-- )
 		{
 			if(stack[i] == '-')
 			{
 				break;
 			}
 		}
 		len = i + 1;
 		plus_count = 0;


 	}
 	return count;
}

char *flip(char *stack, int n)
{
	char temp;
	int i;
	for(i = 0; i < n; i++)
 	{
 		if(stack[i] == '-')
 		{
 			stack[i] = '+';

 		}
 		else if(stack[i] == '+')
 		{
 			stack[i] = '-';
 		}
 	}
 	for(i = 0; i< n/2; i++)
 	{
 		temp = stack[i];
 		stack[i] = stack[n -1 - i];
 		stack[n - 1 - i] = temp;
 	}

 	return stack;

}
