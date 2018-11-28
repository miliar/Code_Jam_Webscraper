#include <iostream> 
#include <vector> 

using namespace std; 

bool is_square_fair(int n)
	{
	int sqrs[] = {1,4,9,121,484};
	for(int i=0;i<sizeof(sqrs)/sizeof(sqrs[0]);i++)
		{
		if(sqrs[i] == n)
			return true; 
		}
	return false; 
	}

int main() {

	int T; 
	cin >> T; 

	int vals[] = {1,2,3,11,22};
	int sqrs[] = {1,4,9,121,484};
	int size = sizeof(vals)/sizeof(vals[0]); 

	int cache[1001] = {0}; 
	for(int i=1;i<=1000;i++)
		{
		if(is_square_fair(i))
			cache[i] = cache[i-1] + 1; 
		else
			cache[i] = cache[i-1]; 
		}

	for(int i=0;i<T;i++) 
	{ 
		int a, b; 
		cin >> a >> b; 

		int result = cache[b] - cache[a]; 
		if(cache[a-1] != cache[a])
			result += 1; 
		cout << "Case #" << (i+1) << ": " << result << endl; 
	}

	return 0; 
}
