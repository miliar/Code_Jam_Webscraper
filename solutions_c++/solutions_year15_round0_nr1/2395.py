#include <iostream>
#include <cstdio>		//for scanf and printf
#include <cstring>		//for memset
#include <vector>

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
		freopen("A-small-attempt0.in","rt",stdin);
		freopen("A-small.out","wt",stdout);
	#endif
	#ifdef LARGE
		freopen("A-large.in","rt",stdin);
		freopen("A-large.out","wt",stdout);
	#endif


	int cases;

	scanf("%d\n", &cases);
	for (int i = 0; i < cases; ++i)
	{	
		int mShy;
		cin>>mShy;
		int shyCount[mShy+1];
		string shyCountString;
		cin>>shyCountString;
		for (int j = 0; j < mShy+1; ++j)
		{	
			shyCount[j] = shyCountString[j] - '0';
		}
		int standPeople = 0;
		int ans = 0;
		for (int j = 0; j < mShy+1; ++j)
		{
		    if(shyCount[j] != 0 && standPeople < j){
				ans += (j - standPeople);		    	
				standPeople = j;
			}
			standPeople += shyCount[j]; 	
		}
		printf("Case #%d: %d\n",i+1, ans);

	}
	return 0;
}
