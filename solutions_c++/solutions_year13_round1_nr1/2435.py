#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <queue>
#include <set>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>
#include <sstream>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(false);
	
	
	freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
	
	long long n;
	
	cin>>n;

	for(int k=1;k<=n;k++)
	{
		long long r, t;
		cin >> r >> t;
		 
		int ans = 0;
		
		while(true)
		{
			 int b = ( r + 1 ) * ( r + 1 );
			 int w = r * r;
			 int need = b - w;
			  
			 if( t < need )
			 break;
			  
			 r+= 2;
			 t -= need;
			 ans++;
			}
			
		cout<<"Case #"<<k<<": "<<ans<<endl;
	}
	
    return 0;
}

