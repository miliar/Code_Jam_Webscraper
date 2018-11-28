#include <iostream>
#include <cstdio>		//for scanf and printf
#include <cstring>		//for memset
#include <vector>
#include <climits>
using namespace std;

//  #define MAX 1001
// 	#define SMALL
	#define LARGE


void printArray(int array[], int size){
	for (int i = 0; i < size; ++i)
	{
		cout<<array[i];
	}
	cout<<endl;
}

int main(){
	#ifdef SMALL
		freopen("B-small-attempt0.in","rt",stdin);
		freopen("B-small.out","wt",stdout);
	#endif
	#ifdef LARGE
		freopen("B-large.in","rt",stdin);
		freopen("B-large.out","wt",stdout);
	#endif


	int cases;

	scanf("%d\n", &cases);
	for (int i = 0; i < cases; ++i)
	{
		int numDishes;
		vector<int> pancakes;		//process time requirement
		scanf("%d\n", &numDishes);		//num of processes
		int themax = 0;
		for (int j = 0; j < numDishes; ++j)
		{
			int pc;
			cin>>pc;
			pancakes.push_back(pc);
			if(pancakes[j] > themax){
				themax = pancakes[j];
			}
		}
		int ans = INT_MAX;
		
		for (int j = 1; j <= themax; ++j)
		{
			int exectime = 0; 
			for (int k = 0; k < numDishes; ++k)
			{
				if(j < pancakes[k]){
					int current_depth = pancakes[k] / j + (pancakes[k] % j ? 1 : 0);
					exectime = exectime + (current_depth - 1);
				}
			}
			if(ans > (exectime + j))
				ans = exectime + j;
		}


		printf("Case #%d: %d\n",i+1, ans);
		
	}
	return 0;
}
