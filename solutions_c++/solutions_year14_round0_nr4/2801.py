#include<iostream>
#include<cstdio>
using namespace std;

#include<algorithm>
#include<vector>
#include<cmath>
#include<limits.h>
#include<queue>


typedef long long ll;
typedef vector<int> vi;
typedef vi::iterator vit;
typedef pair<int,int> pii;
typedef vector<float>::iterator fit;

#define sz(c) (int)( (c).size() 
#define _for(i,a,b) for( int i = a ; i< b; ++i )
#define OR ||
#define AND &&
#define mp make_pair
#define all(c) (c).begin(),(c).end()
//---------------------------

int main()
{
	int t,num;
	cin>>t;
	vector<float> nami,ken,_nami,_ken;
	
	_for(z,1,t+1)
	{
		cout<<"Case #"<<z<<": ";
		cin>>num;
		
		nami.resize(num);
		ken.resize(num);
		
		_for(i,0,num)
		cin>>nami[i];
		sort( all(nami) ) ;
		_nami = nami;
		
		_for(i,0,num)
		cin>>ken[i];
		sort( all(ken) ) ;
		_ken = ken;
		
		int ans1= 0,ans2=0;
		//------------------------------------------
		//       CALCULATING NORMAL
		fit _n=_nami.begin(),_k=_ken.begin();
		
		while( _n != _nami.end() )
		{
			if( *(_k) > *(_n) ) 
			{
				ans1++;
				_nami.erase(_n);
				_ken.erase(_k);
			}
			
			else
			{
				_nami.erase(_nami.end()-1);
				_ken.erase( _k);
			}
		}
	
		//------------------------------------------
		//    CALCULATING DECIETFULL WAR
		
		fit n=nami.begin(),k=ken.begin();
		
		while( n != nami.end() )
		{
			if( *n > *k ) 
			{
				ans2++;
				nami.erase(n);
				ken.erase(k);
			}
			
			else
			{
				nami.erase(n);
				ken.erase( ken.end()-1 );
			}
		}
		cout<<ans2<<" "<<(num - ans1) <<endl;
	}
	
	return 0 ;
}
