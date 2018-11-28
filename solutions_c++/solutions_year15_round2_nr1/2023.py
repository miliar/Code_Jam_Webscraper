#include <bits/stdc++.h> 

using namespace std ; 

#define MAX 1000001
int arr[MAX] = { } ; 
int get_reverse(int num)
{
	string str = to_string(num) ; 
	reverse(str.begin(), str.end()) ; 
	return stoi(str) ; 

}

int main()
{
	int tc ; 
	int limit = 1 ; 
	arr[1] = 1 ; 
	scanf("%d\n", &tc) ; 
	for(int i=0; i<tc; i++)
	{
		int num ; scanf("%d", &num) ; 
		if(limit < num)
		{
			for(int j=limit+1; j<num+1; j++)
			{
				int rev = get_reverse(j) ; 	
				if(j == get_reverse(rev)) 
				{
					if(arr[rev] != 0)
					{
						arr[j] = min(arr[rev],arr[j-1]) + 1 ; 
					}	
					else 
					{
						arr[j] = arr[j-1] + 1 ;
					}	
				}
				else 
				{
					arr[j] = arr[j-1] + 1 ; 
				}
			}
		}
		printf("Case #%d: %d\n", i+1,arr[num]) ; 
	}
	return 0 ; 
}
