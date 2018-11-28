#include <iostream>
#include <stdio.h>
#include <string>
#include <string.h>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <climits>
#include <cmath>
#include <sstream>
#include <iomanip>
using namespace std;

int main(int argc, char const *argv[])
{
	int tc;
	scanf("%d",&tc);
	getchar();
	char arr[4][5];
	int arr_bool[4][4];
	for (int t = 1; t <= tc; ++t){
		for (int i = 0; i < 4; ++i){
			scanf("%s",&arr[i]);
		}

		bool incomplete=0;
		for (int i = 0; i < 4; ++i){
			for (int j = 0; j < 4; ++j){
				if (arr[i][j]=='X')
					arr_bool[i][j]=1;
				else if (arr[i][j]=='O')
					arr_bool[i][j]=-1;
				else if (arr[i][j]=='.'){
					arr_bool[i][j]=0;
					incomplete=1;
				} 
				else if (arr[i][j]=='T')
					arr_bool[i][j]=0;
			}
		}

		int sum=0;
		bool T=0;
		int state=0; //0 for draw //1 for X //2 for O 
		
		/////////Horizontal
		for (int i = 0; i < 4; ++i){
			sum=0;
			T=0;
			for (int j = 0; j < 4; ++j){
				sum+=arr_bool[i][j];
				if (arr[i][j]=='T')
					T=1;
			}

			if (sum==4 || (sum==3 && T==1)){
				state=1;
				goto x;
			}
			if (sum==-4 || (sum==-3 && T==1)){
				state=2;
				goto x;
			}
		}

		/////////Vertical
		for (int i = 0; i < 4; ++i){
			sum=0;
			T=0;
			for (int j = 0; j < 4; ++j){
				sum+=arr_bool[j][i];
				if (arr[j][i]=='T')
					T=1;
			}

			if (sum==4 || (sum==3 && T==1)){
				state=1;
				goto x;
			}
			if (sum==-4 || (sum==-3 && T==1)){
				state=2;
				goto x;
			}
		}


		//Top-down Diagnol
		sum=0;
		T=0;
		for (int j = 0; j < 4; ++j){
			sum+=arr_bool[j][j];
			if (arr[j][j]=='T')
				T=1;
		}

		if (sum==4 || (sum==3 && T==1)){
			state=1;
			goto x;
		}
		if (sum==-4 || (sum==-3 && T==1)){
			state=2;
			goto x;
		}
		//Bottom-up diagnol
		sum=0;
		T=0;
		for (int j = 0; j < 4; ++j){
			sum+=arr_bool[j][3-j];
			if (arr[j][3-j]=='T')
				T=1;
		}

		if (sum==4 || (sum==3 && T==1)){
			state=1;
			goto x;
		}
		if (sum==-4 || (sum==-3 && T==1)){
			state=2;
			goto x;
		}
		
		x:
		if (state==1){
			printf("Case #%d: X won\n",t);
		}
		else if (state==2){
			printf("Case #%d: O won\n",t);
		}
		else if (state==0 && incomplete){
			printf("Case #%d: Game has not completed\n",t);
		}
		else
			printf("Case #%d: Draw\n",t); 
	}

	return 0;
}
