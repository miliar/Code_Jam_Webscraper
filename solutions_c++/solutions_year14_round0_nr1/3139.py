#include<cstring>
#include<cstdio>
#include<iostream>

using namespace std;

const int mn = 20;
const int mm = 4;

int Test;
int a[mn][mn];
bool bo[mn];
int x;

void check()
{
	int ans = -1;
	for ( int j = 0; j < 4; ++j ) if ( bo[a[x - 1][j]] )
	{
		if ( ans != -1 ) 
		{
			cout << "Bad magician!" << endl;
			return;
		}
		if ( ans == -1 ) ans = a[x - 1][j];
	}
	if ( ans == -1 ) 
		cout << "Volunteer cheated!" << endl;
	else 
		cout << ans << endl;
}

int main()
{
	freopen("A-small-attempt1.in","r",stdin);
	freopen("A-small-attempt1.out","w",stdout);
	cin >> Test;
	for ( int Testi = 0; Testi < Test; ++Testi )
	{
		memset( bo, 0, sizeof bo );
		cin >> x ;
		for ( int i = 0; i < 4; ++i )
			for ( int j = 0; j < 4; ++j ) cin >> a[i][j];
		for ( int j = 0; j < 4; ++j ) bo[a[x - 1][j]]=true;
		cin >> x ;
		for ( int i = 0; i < 4; ++i )
			for ( int j = 0; j < 4; ++j ) cin >> a[i][j];
		cout << "Case #" << Testi+1 << ": " ;
		check();
	}
}