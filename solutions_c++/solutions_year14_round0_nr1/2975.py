#include<iostream>
using namespace std;

#include<algorithm>
#include<vector>
#include<cmath>
#include<limits.h>

typedef long long ll;
typedef vector<int> vi;
typedef vi::iterator vit;

#define sz(c) (int)( (c).size() ) 
#define MAX 4
#define count _count

int mat1[MAX][MAX];
int ans1;

int mat2[MAX][MAX];
int ans2;

int main()
{
	int t ;
	cin>>t;
	
	for( int z = 1; z <= t; ++z)
	{
		cout<<"Case #"<<z<<": ";


		cin>>ans1;
		ans1--;
		
		for( int i = 0; i<MAX;++i)
			for( int j = 0; j<MAX; ++j)
			cin>>mat1[i][j];
			

		cin>>ans2;
		ans2--;
		
		for( int i = 0; i<MAX;++i)
			for( int j = 0; j<MAX; ++j)
			cin>>mat2[i][j];
			
		int count = 0 ;
		int ans = 0;
		
		for( int i = 0; i<MAX;++i)
		{
			for( int j = 0; j<MAX; ++j)
			{
				if( mat1[ans1][i] == mat2[ans2][j] )
				{
					count++;
					ans = mat1[ans1][i];
					break;
				}
			}
		}	
			
		if( count == 1 )
		cout<<ans<<endl;
		
		else if(count == 0 ) 
		cout<<"Volunteer cheated!"<<endl;
		
		else
		cout<<"Bad magician!"<<endl;	
	}
	
	return 0 ; 
}
