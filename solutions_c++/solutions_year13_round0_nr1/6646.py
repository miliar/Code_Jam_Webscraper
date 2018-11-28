#include<cstdio>
#include<iostream>

using namespace std;

int check_o ( char a[5][5] )
{
	int flag1 = 0;
	int flag2 = 0;
	for ( int i = 0; i < 4; i++ ) {
		if ( a[0][i] == 'O' || a[0][i] == 'T')
			flag1++;
	}
	if ( flag1 == 4 ) 
		return 1;
	flag1 = 0;
	for ( int i = 0; i < 4; i++ ) {
		if ( a[1][i] == 'O' || a[1][i] == 'T')
			flag1++;
	}
	if ( flag1 == 4 ) 
		return 1;
	flag1 = 0;
	for ( int i = 0; i < 4; i++ ) {
		if ( a[2][i] == 'O' || a[2][i] == 'T')
			flag1++;
	}
	if ( flag1 == 4 )
		return 1;
	flag1 = 0;
	for ( int i = 0; i < 4; i++ ) {
		if ( a[3][i] == 'O' || a[3][i] == 'T')
			flag1++;
	}
	if ( flag1 == 4 ) 
		return 1;
	flag1 = 0;

	for ( int i = 0; i < 4; i++ ) {
		if ( a[i][0] == 'O' || a[i][0] == 'T')
			flag1++;
	}
	if ( flag1 == 4 )
		return 1;
	flag1 = 0;
	for ( int i = 0; i < 4; i++ ) {
		if ( a[i][1] == 'O' || a[i][1] == 'T')
			flag1++;
	}
	if ( flag1 == 4 )
		return 1;
	flag1 = 0;
	for ( int i = 0; i < 4; i++ ) {
		if ( a[i][2] == 'O' || a[i][2] == 'T')
			flag1++;
	}
	if ( flag1 == 4 ) 
		return 1;
	flag1 = 0;
	for ( int i = 0; i < 4; i++ ) {
		if ( a[i][3] == 'O' || a[i][3] == 'T')
			flag1++;
	}
	if ( flag1 == 4 ) 
		return 1;
	flag1 = 0;
	for ( int i = 0; i < 4; i++ ) {
		if ( a[i][i] == 'O' || a[i][i] == 'T')
			flag1++;
	}
	if ( flag1 == 4 )
		return 1;
	flag1 = 0;
	for ( int i = 0; i < 4; i++ ) {
		if ( a[3-i][i] == 'O' || a[3-i][i] == 'T' ) 
			flag1++;
	}
	if ( flag1 == 4 )
		return 1;
	return 0;
}


int check_x ( char a[5][5] )
{
	int flag1 = 0;
	int flag2 = 0;
	for ( int i = 0; i < 4; i++ ) {
		if ( a[0][i] == 'X' || a[0][i] == 'T')
			flag1++;
	}
	if ( flag1 == 4 )
		return 1;
	flag1 = 0;
	for ( int i = 0; i < 4; i++ ) {
		if ( a[1][i] == 'X' || a[1][i] == 'T')
			flag1++;
	}
	if ( flag1 == 4 )
		return 1;
	flag1 = 0;
	for ( int i = 0; i < 4; i++ ) {
		if ( a[2][i] == 'X' || a[2][i] == 'T')
			flag1++;
	}
	if ( flag1 == 4 )
		return 1;
	flag1 = 0;
	for ( int i = 0; i < 4; i++ ) {
		if ( a[3][i] == 'X' || a[3][i] == 'T')
			flag1++;
	}
	if ( flag1 == 4 )
		return 1;
	flag1 = 0;

	for ( int i = 0; i < 4; i++ ) {
		if ( a[i][0] == 'X' || a[i][0] == 'T')
			flag1++;
	}
	if ( flag1 == 4 )
		return 1;
	flag1 = 0;
	for ( int i = 0; i < 4; i++ ) {
		if ( a[i][1] == 'X' || a[i][1] == 'T')
			flag1++;
	}
	if ( flag1 == 4 )
		return 1;
	flag1 = 0;
	for ( int i = 0; i < 4; i++ ) {
		if ( a[i][2] == 'X' || a[i][2] == 'T')
			flag1++;
	}
	if ( flag1 == 4 )
		return 1;
	flag1 = 0;
	for ( int i = 0; i < 4; i++ ) {
		if ( a[i][3] == 'X' || a[i][3] == 'T')
			flag1++;
	}
	if ( flag1 == 4 )
		return 1;
	flag1 = 0;
	for ( int i = 0; i < 4; i++ ) {
		if ( a[i][i] == 'X' || a[i][i] == 'T')
			flag1++;
	}
	if ( flag1 == 4 )
		return 1;
	flag1 = 0;
	for ( int i = 0; i < 4; i++ ) {
		if ( a[3-i][i] == 'X' || a[3-i][i] == 'T' )
			flag1++;
	}
	if ( flag1 == 4 )
		return 1;
	return 0;
}

int check_tie ( char a[5][5] )
{
	for ( int i = 0; i < 4; i++ ) {
		for ( int j = 0; j < 4; j++ ) {
			if ( a[i][j] == '.') {
				return 0;
			}
		}
	}
	return 1;
}

int main()
{
	int t;
	int test = 1;
	int p,q,r;
	scanf ("%d",&t);
	while(t--) {
		char a[5][5];
		for ( int i = 0; i < 4; i++ ) {
			scanf("%s", a[i]);
		}
		p = check_o (a);
		if ( p == 1 ) {
			cout << "Case #"<<test<<": O won"<<endl;
		}
		else {
			q = check_x (a);
			if ( q == 1 ) {
				cout << "Case #"<<test<<": X won"<<endl;
			}
			else {
				r = check_tie (a);
				if ( r == 1 ) {
					cout << "Case #"<<test<<": Draw"<<endl;
				}
				else {
					cout << "Case #"<<test<<": Game has not completed"<<endl;
				}
			}
		}
		test++;
	}
	return 0;	
}
