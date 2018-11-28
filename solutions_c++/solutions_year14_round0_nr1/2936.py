#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
    /* Enter your code here. Read input from STDIN. Print output to STDOUT */   
int t,first,second;
int prob[4],prob2[4];
int grid[4][4];
cin>>t;
int total=t;
while(t-- && t<=100){
int i=0,j=0;
cin>>first;
for(i=0;i<4;i++)
	for(j=0;j<4;j++)
		cin>>grid[i][j];

for(j=0;j<4;j++)
prob[j] = grid[first-1][j];

for(i=0;i<4;i++)
	for(int j=0;j<4;j++)
		grid[i][j]=0;

cin>>second;
for(i=0;i<4;i++)
	for(j=0;j<4;j++)
		cin>>grid[i][j];

for(j=0;j<4;j++)
prob2[j] = grid[second-1][j];

int common[4],count=0;
for(i=0;i<4;i++)
	for(j=0;j<4;j++)
		{
		if(prob[i] == prob2[j])
			{
				common[count] = prob[i];
				count++;
			} 
		}		
cout << "Case #" << total-t << ": ";
if (count > 1)
cout << "Bad magician!" << endl;
else if (count == 1)
cout << common[0] << endl;
else if(count == 0)
cout << "Volunteer Cheated!" <<endl;


}
    return 0;
}
