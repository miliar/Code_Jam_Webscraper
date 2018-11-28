#include<iostream>
#include<cstring>
#include<cmath>
using namespace std;
bool arr[1002];
void solve()
{
	memset( arr, 0, sizeof(arr) );
	int s,j;
	int arrr[7];
	bool check;
	for ( int i=1 ; i<1000 ; i++ )
	{
		s=i;
		j=0;
		while ( s!=0 )
		{
			arrr[j++]=s%10;
			s/=10;
		}
		check=true;
		for ( int k=0 ; k<=j/2 ; k++ )
			if ( arrr[k]!=arrr[j-k-1] )
				check=false;
		if ( check )
		{
			s=i*i;
			j=0;
			while ( s!=0 )
			{
				arrr[j++]=s%10;
				s/=10;
			}
			check=true;
			for ( int k=0 ; k<=j/2 ; k++ )
				if ( arrr[k]!=arrr[j-k-1] )
					check=false;
			if ( check )
			{
				if ( i*i>1000 )
					break;
				else
					arr[i*i]=true;
			}
		}
	}

}
int main()
{
	//freopen ( "input.in" , "r" , stdin );
	//freopen ( "output.out" , "w" , stdout );
	solve();
	int A,B,ans,t;
	cin>>t;
	for ( int i=0 ; i<t ; i++ )
	{
		cin>>A>>B;
		ans=0;
		for ( int j=A ; j<=B ; j++ )
			if ( arr[j] )
				ans++;
		cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
}