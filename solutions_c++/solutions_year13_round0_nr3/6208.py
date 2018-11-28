// tomek.cpp : Defines the entry point for the console application.
//

#include <iostream> 
#include <cstdio>
#include <ctime>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <string>
#include <map>
#include <set> 
#include <vector>
#include <cstdlib>
#include <queue>
#include <stack>

using namespace std;

int main() 
{ 
    freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int T;
	cin >> T;
	for(int t = 0; t < T; ++t) 
	{
		unsigned int A,B;
		int count=0;
		cin >> A >> B;
		int fas[] = {1,4,9,121,484};
		for(int i= 0; i<=5; i++)
		{
			if((fas[i] >= A) && (fas[i] <= B))
				count++;
		}
		
		printf("Case #%d: ", t + 1);
		cout << count;
		printf("\n");
		}
		
		return 0;

}

	
 

