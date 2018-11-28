#include<iostream>
#include<string>
#include<cmath>
#include<algorithm>
#include<iomanip>
#include<map>
#include<stdio.h>
#include<vector>
#include<string.h>
#include<set>
#include<stack>
#include<queue>
#include<sstream>
#include<fstream>
using namespace std;
int a[1000000];
int main()
{
	ifstream cin("A-small-attempt2.in");
	ofstream cout("A-small-attempt2.out");
	int T;
	cin>>T;
	for(int i=0;i<T;i++){
		int counter = 0;
		int N,A;
		cin>>A>>N;

		for (int j = 0; j < N ; j++)
		{
			cin>>a[j];
		}
		sort(a,a+N);
		int problem=-1;
		for (int j = 0; j < N ; j++)
		{
			if(A>a[j])
				A+=a[j];
			else
			{
				problem=j;
				break;
				
			}
		}
		if(problem==-1)
			counter=0;
		else if(A==1)
			counter=N;
		else{
			int removeSolution = N-problem;
			while(problem<N){
				int oldCounter = counter;
				while(A<=a[problem])
				{
					A+=(A-1);
					counter++;
				}
				if(counter>=removeSolution+oldCounter)
				{
					counter=removeSolution+oldCounter;
					break;
				}
				
				while(problem<N&&a[problem]<A)
				{
					A+=a[problem++];
					removeSolution--;
				}
			}
		}
		cout<<"Case #"<<i+1<<": "<<counter<<endl;
	}
	return 0;
}