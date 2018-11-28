#include <stdio.h>
#include <iostream>
#include <stdlib.h>
using namespace std;
int ProcessInput();
int main()
{

int testcases, i;

cin >> testcases;

//cout <<"Number of testcases:" << testcases << endl;
for(i=0; i < testcases; i++) {
	cout<<"Case #"<<i + 1<<": ";
	ProcessInput();
}

return 0;
}

int ProcessInput()
{
	int r1, r2;
	int a[4][4], b[4][4];
	int i, j, count, matched_value;

	cin >> r1;
	for(i=0; i < 4; i ++) 
		for(j=0; j < 4; j++)
			cin >> a[i][j];
	cin >> r2;
	for(i=0; i < 4; i ++)
		for(j= 0; j <4; j++)
			cin >> b[i][j];

	count = 0;
	for(i=0; i < 4; i++)
		for(j = 0; j < 4; j++) 
			if(a[r1-1][i] == b[r2-1][j]) {
				count ++;
				matched_value = a[r1-1][i];
			}						
	if(count == 0)
		//return -1; // User cheated
		cout <<"Volunteer cheated!"<<endl;
	if(count > 1)
		//return -2 // 
		cout <<"Bad magician!"<<endl;
	if(count== 1)
		cout<<matched_value<<endl;

	return 0;
}
