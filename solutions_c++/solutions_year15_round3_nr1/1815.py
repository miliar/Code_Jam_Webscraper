#include <bits/stdc++.h>

using namespace std;

#define lld long long 

int main()
{

	lld T;
	cin >> T;
	lld	t = T;

	/*while(t--){

		lld R,C,W,solution;

		cin >> R >> C >> W;

		lld comb = R*((C-W)+1);

		solution = max(comb, W);

		
	}

	/*
		xxxx {c - w} + 1
		xxxx
		xxxx
	
	*/


	while(t--){


		lld R,C,w,solution = 0;


		cin >> R >> C >> w;
/*
		xxxx
		 0
*/
		lld num = (w-1)>0?w:1;
		lld i = num;
		//cout << num << endl;
		for( i ; i < C; i+=num){
			//cout << i;

			solution++;


		}

		solution+=num;

		printf("Case #%lld: %lld\n", T - t, solution);


	}


	return 0;
}