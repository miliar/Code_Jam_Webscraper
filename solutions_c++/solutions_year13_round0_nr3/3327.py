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

#define loopab(a,b,c) for( a = ( b ); a <= ( c ); ++ a )
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

bool pelindrome(long double num)
{
	long double n, rev = 0;
	int digit,temp = (int) num;
     	n = num;
     	do
     	{
         	digit = temp%10;
         	rev = (rev*10) + digit;
         	temp = temp/10;
     	}while (temp!=0);
	//printf("%Lf,%Lf",n,rev);
     	if (n==rev)
       		return true;
     	else
       		return false;
}

void solve(void)
{
	long double low,high,ans=0,i,sqr;
	long double val_low,val_high;
	scanf("%Lf",&low);
	scanf("%Lf",&high);
	val_low = sqrt(low);
	val_low = ceil(val_low);
	val_high = sqrt(high);
	val_high = ceil(val_high);	
	loopab(i,val_low,val_high)
	{
		if(pelindrome(i))
		{
			sqr = i*i;
			if(pelindrome(sqr) && sqr <= high)
			{
				ans++;
				//printf("\ni=%Lf",i);
			}
		}
	}
	printf("%.0Lf\n",ans);

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
