#include<bits/stdc++.h>
using namespace std;

int main()
{
	freopen("D-small-attempt0 (1).in","r",stdin);
freopen("output_3.txt","w",stdout);
	int test,cnt=1;
	cin >> test;
	while(test--) {


		int domino,row,column;

		cin >> domino >> row >> column;

		printf("Case #%d: ",cnt++);

		if(domino == 1)
		{
			printf("GABRIEL\n");
		}
		else if(domino == 2)
		{
			if((row*column) & 1 ) printf("RICHARD\n");
			else puts("GABRIEL");
		}
		else if(domino == 3)
		{
			if((row == 3 || column == 3) && (row*column) != 3)printf("GABRIEL\n");
			else printf("RICHARD\n");
		}
		else{
			if((row == 3 && column == 4) || (row == 4 && column ==3) || (row == 4 && column == 4)) printf("GABRIEL\n");
			else printf("RICHARD\n");
		}
	}
}
