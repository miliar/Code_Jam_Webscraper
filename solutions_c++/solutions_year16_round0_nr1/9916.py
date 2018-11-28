#include <iostream>
#include <queue>
#include <list>
#include <vector>


using namespace std;
long long int findAns(int num);

int main()
{
	int testcase = 0;
	cin >> testcase;
	int i;
	long long int arr[100];
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
		else if ( ans[i] < 0)
		{
			cout << "Case #" << i+1 << ": INSOMNIA" << endl;

		}
 	}
 }
 long long int findAns(int num)
 {

 	int digi[10], i;
 	int modulo;
 	bool ans = false; 
 	int cpy;
 	int count = 0;
 	int numcpy = num;
 	for(i=0; i<10; i++)
 	{	
 		digi[i] = 0;

 	}
 	if(num == 0)
 	{
 		return -2;
 	}
 	while(ans == false)
 	{
 		ans = true;
 		cpy = num;
 		while(num  > 0)
 		{
 			modulo = num%10;
 			num = num/10;
 			digi[modulo] = 1;
 		}
 		num = cpy + numcpy;
 		for(i=0; i<10; i++)
 		{
 			if(digi[i] == 0)
 			{
 				ans = false; 
 				break;
 			}		
 		}
 		count ++;
 	}
 	return num - numcpy;
 }