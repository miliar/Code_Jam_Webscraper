#include<stdio.h>
#include<iostream>
using namespace std;
int main() {
    int T=0;
	int sMax=0;
	int count = 0;
	int people_needed =0;
	char sLevels[10];
	int val;
	cin>>T;
	
	for(int i = 1; i <= T ; i++)
	{

        scanf("%d %s",&sMax,sLevels);

		people_needed = 0;
		count=0;
		for(int j = 0; j <= sMax ;j++)
		{
			val = sLevels[j] - '0';
			if(count < j)
				{
				people_needed +=  j - count;
				count = j;
				}
				
			count += val;
			
		}
		cout<<"Case #"<<i<<": "<<people_needed<<endl;
		
	}
	
	
	
    return 0;
}