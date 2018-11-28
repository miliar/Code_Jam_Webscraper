#include <iostream>
#include <cstdio>		//for scanf and printf
#include <cstring>		//for memset
#include <vector>
#include <climits>
using namespace std;

//  #define MAX 1001
 	#define SMALL
//	#define LARGE


void printArray(int array[], int size){
	for (int i = 0; i < size; ++i)
	{
		cout<<array[i];
	}
	cout<<endl;
}

int main(){
	#ifdef SMALL
		freopen("D-small-attempt0.in","rt",stdin);
		freopen("D-small.out","wt",stdout);
	#endif
	#ifdef LARGE
		freopen("D-large.in","rt",stdin);
		freopen("D-large.out","wt",stdout);
	#endif


	int cases;

	cin>>cases;
	for (int i = 0; i < cases; ++i)
	{						
		int x, r, c; 
		cin>>x>>r>>c;
		int winner = 1;	//Ritchard the problem maker
		if((r*c)%x == 0){
			if(r >= (x-1) && c >= (x-1))
				winner = 0;
		}
		if(winner == 0)
			printf("Case #%d: GABRIEL\n",i+1);
		else
			printf("Case #%d: RICHARD\n",i+1);
		
	}
	return 0;
}
