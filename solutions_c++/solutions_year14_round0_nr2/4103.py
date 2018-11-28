#include<stdio.h>
#include<string>
#include<memory.h>
#include<math.h>
#include<iostream>
#include<istream>
#include<vector>
#include<algorithm>
#include<iomanip> 
#define fi(a,b) for( i = a; i < b ; i++ )
#define fj(a,b) for( j = a; j < b ; j++ )
#define fk(a,b) for( k = a; k < b ; k++ )

using namespace std;

typedef vector<int> vi;
typedef vector<char> vc;
typedef vector<double> vd;
//char a[26];
int ri()
	{ int a; 
	  scanf( "%d", &a ); 
	  return a; 
	}
int compare (const void * a, const void * b)
{
  return ( *(int*)b - *(int*)a );
}

int main()
{
	freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
	vd T;
	int i=0, j, t=0;
	long float time = 0.0,c,f,x,r;
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		time = 0;
		scanf("%lf",&c);
		scanf("%lf",&f);
		scanf("%lf",&x);
		r=2;
		while((x-c)/r > x/(r+f))
		{
			{
				time = time + c/r;
				r = r + f;
			}
		}
		time = time + x/r;
		printf("Case #%d: %.7lf\n",i+1,time);
		//cout <<setprecision(20);
		//cout<<time;
	}
}