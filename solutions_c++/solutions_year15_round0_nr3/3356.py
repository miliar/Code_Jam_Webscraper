# include <stdio.h>
# include <iostream>

using namespace std;

char pre [10003][10003];

char a[8][8] = {
			{0, 1, 2, 3, 4, 5, 6, 7},
			{1, 4, 3, 6, 5, 0, 7, 2},
			{2, 7, 4, 1, 6, 3, 0, 5},
			{3, 2, 5, 4, 7, 6, 1, 0},
			{4, 5, 6, 7, 0, 1, 2, 3},
			{5, 0, 7, 2, 1, 4, 3, 6},
			{6, 3, 0, 5, 2, 7, 4, 1},
			{7, 6, 1, 0, 3, 2, 5, 4}
};

int main(){
    freopen("input.txt", "r" , stdin );
    freopen("output.txt", "w" , stdout );
	int t;
	scanf("%d",&t);
	for( int kr = 1; kr <= t; kr++ ){
		printf("Case #%d: ",kr);
		int l, x;
		string s;
		cin>>l>>x>>s;
		for( int i = 0; i < l; i++ ){
			if( s[i] == 'i' )s[i] = 1;
			else if( s[i] == 'j')s[i] = 2;
			else s[i] = 3;
		}
		string y;
		for( int i = 0; i < x; i++ )
			y = y + s;
		for( int i = 0; i < y.size(); i++){
			int l = 0;
			for( int j = i; j < y.size(); j++ ){
				l = a[l][y[j]];
				pre[i][j] = l;
			}
		}
		int flag = 0;
		for( int i = 0; i < y.size(); i++ ){
			for ( int j = i + 1; j < y.size(); j++ ){
				if ( (pre[0][i] == 1) && (pre[i+1][j] == 2) && (pre[j+1][y.size() -1] == 3)){
					flag = 1;
					break;
				}
			}
			if( flag == 1)
				break;
		}
		if(flag){
			printf("YES\n");
		}
		else
			printf("NO\n");
	}
	return 0;
}
