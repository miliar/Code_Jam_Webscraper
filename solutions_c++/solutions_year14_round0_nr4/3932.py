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
typedef vector<float> vf;

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
	vf A,B,A1,B1;
	int i=0, j, t=0, n, dec_count=0, war_count=0,test;
	long float temp;
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		A.clear();
		B.clear();
		A1.clear();
		B1.clear();
		dec_count=0;
		war_count=0;

		scanf("%d",&n);
		for(j=0;j<n;j++) 
			{
				scanf("%lf",&temp);
				A.push_back(temp);
				A1.push_back(temp);
		}
		for(j=0;j<n;j++) 
			{
				scanf("%lf",&temp);
				B.push_back(temp);
				B1.push_back(temp);
		}
		sort(A.begin(),A.end());
		sort(B.begin(),B.end());
		sort(A1.begin(),A1.end());
		sort(B1.begin(),B1.end());
		
		while(!A.empty())
		{
		if(A[0] > B[0])
		{
			dec_count++;
			B.erase(B.begin());
			A.erase(A.begin());
		}
		else{
			if(B.size()==1)
			{ B.erase(B.begin()); A.erase(A.begin());}
			else
				{ B.pop_back(); 
				A.erase(A.begin());
			}
		}
		}
/**********************************************************/
		while(!A1.empty())
		{
			test = 0;
			for(j=0;j<B1.size();j++)
			{
				if(A1[0] < B1[j])
				{ 
					A1.erase(A1.begin());
					B1.erase(B1.begin()+j);
					test=1;
					break;
				}
			}
			if(test==0)
			{			
			war_count = A1.size();	
			A1.clear();
			}
		}

		printf("Case #%d: %d %d\n",i+1,dec_count,war_count);
		//cout <<setprecision(20);
		//cout<<time;
	}
}