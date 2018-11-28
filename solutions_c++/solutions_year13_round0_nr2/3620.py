#include<fcntl.h>
#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>
#include <errno.h>
#include <stdlib.h>
#include <math.h>
#include <netdb.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>

#define loopab(a,b,c) for( a = ( b ); a < ( c ); ++ a )
#define loopn(a,b) loopab( a, 0, ( b ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define mms(a,b) memset( a, b, sizeof( a ) )

using namespace std;

template <class T> void out( T a, T b ) { bool first = true; for( T i = a; i != b; ++ i ) { if( !first ) printf( " " ); first = false; cout << * i; } printf( "\n" ); }
template <class T> void outl( T a, T b ) { for( T i = a; i != b; ++ i ) { cout << * i << "\n"; } }
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;

int garden[100][100],m,n;

bool isrow(int i,int j)
{
	int k;
	loopn(k,m)
	{
		if(garden[i][k]>garden[i][j])
			return false;
	}
	return true;
}

bool iscol(int i,int j)
{
	int k;
	loopn(k,n)
	{
		if(garden[k][j]>garden[i][j])
			return false;
	}
	return true;
}


void solve(void)
{
	int i,j;
	scanf("%d %d\n",&n,&m);
	loopn(i,n)
	{
		loopn(j,m)
		{
			scanf("%d",&garden[i][j]);
			//printf("%d",garden[i][j]);
		}
		//printf("\n");
	}
	loopn(i,n)
	{
		loopn(j,m)
		{
			if(garden[i][j]<100)
			{
				if(isrow(i,j))
				{
					continue;
				}
				else if(iscol(i,j))
				{
					continue;	
				}
				else
				{
					printf("NO\n");
					return;
				}
			}
		}
	}
	printf("YES\n");
	return;
	
}

int main(int argc, char *argv[])
{
        unsigned long int i,j,t;
       	int fdi = open("input.txt",O_RDONLY);
        int fdo = creat("output.txt",0644);
        close(1);
        dup(fdo);
        close(0);
        dup(fdi);
        close(fdo);
        close(fdi);
	scanf("%ld\n",&t);
	for(j=0;j<t;j++)
        {
		printf("Case #%ld: ",j+1);
		solve();
        }
return 0;
}
