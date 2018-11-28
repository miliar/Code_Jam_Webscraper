//
//  main.cpp
//  A.Standing Ovation
//
//  Created by Repon Macbook on 4/11/15.
//  Copyright (c) 2015 Repon Macbook. All rights reserved.
//

#include <bits/stdc++.h>
using namespace std;

#define LMT			100


string inpStr;
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int tc ,cs =  0 , SM ;
	scanf("%d",&tc);
	while (tc -- ) {
		scanf("%d",&SM);
		cin >> inpStr;
		
		int audienceClap = inpStr[0] -'0' ;
		int additional = 0;
		for (int i = 1; i <= SM ; i ++ ) {
			int k = inpStr[i] -'0' ;
			if( k == 0 ) continue;
			if(audienceClap >= i  ){
				audienceClap += k;
			}
			else {
				additional += (i - audienceClap );
				audienceClap += additional + k ;
				
			}
		}
		printf("Case #%d: %d\n" , ++cs, additional  );
	}
	return 0;
}
