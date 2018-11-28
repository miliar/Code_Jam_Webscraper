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
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;

void solve(void)
{
	int A,N,M[200],changes=0,save=100;
	int loop1,loop2;
	bool FLAG[200] = {false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false,false};
	
	scanf("%d %d\n",&A,&N);
	vi myvector,myvector1;
	vi::iterator it,it1;
	
	loopn(loop1,N)
	{
		scanf("%d",&M[loop1]);
		it = myvector.end();
		myvector.insert(it,M[loop1]);

	}
		
	sort (myvector.begin(), myvector.end());
	bool movement = false,pass=false,issaved = false;
	again:
	movement = false;
	for (it=myvector.begin(),loop2=0; it!=myvector.end(); ++it,loop2++)
    	{
		if(*it<A && !FLAG[loop2])
		{
			movement = true;
			A+=*it;
			FLAG[loop2] = true;
			//printf("\n%d",*it);
		}
	}
	if(movement)
	{
		goto again;
	}
	else
	{
		pass = false;
		loopn(loop1,N)
		{
			if(FLAG[loop1]==false)
			{
				//if((myvector.at(loop1)))
				pass = true;
				int tmp = (myvector.at(loop1));
				it1 = myvector1.begin();
  				it1 = myvector1.insert ( it1 , tmp );
			}
		}
		if(pass)
		{
		sort (myvector1.begin(), myvector1.end());
		int first = (myvector1.at(0));
		/*if(first<(2*A) && A!=1)
		{
			it1 = myvector.end();
			myvector.insert(it1 , (A-1));
			N++;
			changes++;
			myvector1.clear();
			goto again;
		}
		else
		*/{
			int temp_save = changes;
			for (it=myvector1.begin(); it!=myvector1.end(); ++it)
		   	{
				changes++;
			}
			//printf("\n\nchanges = %d",changes);
			if(changes < save) 
			{
				save = changes;
				//printf("\n\nsave = %d",save);
			}
			else if(changes>=100)
				goto end;
			if(A!=1)
			{
				it1 = myvector.end();
				myvector.insert(it1 , (A-1));
				N++;
				changes = temp_save+1;
				myvector1.clear();
				goto again;
			}
		}
		myvector1.clear();
		}
	}
	end:
	if(changes>save)
		changes = save;
	printf("%d\n",changes);
}

int main(int argc, char *argv[])
{
        ull j,t;
       	scanf("%lld\n",&t);
	loopn(j,t)
        {
		printf("Case #%lld: ",j+1);
		solve();
        }
return 0;
}
