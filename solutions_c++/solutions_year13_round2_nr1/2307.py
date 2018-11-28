#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <set>
#include <map>
#include <stdio.h>
using namespace std;

int main()
{
	freopen("Text1.txt","r",stdin);
	freopen("Text.txt","w",stdout);
	int tc;
	cin >> tc;

	for ( int o = 1 ; o <= tc ; o++ )
	{
		long long mote;
		cin >> mote;
		long long n;
		cin >> n;
		vector<int> v(n);
		for ( int i = 0 ; i < n ; i++ )
		{
			cin >> v[i];
		}
		sort(v.begin(),v.end());
		long long sum=0;
		for ( int i = 0 ; i < v.size() ; i++ )
		{
			if ( v[i] >= mote )
			{
				if ( mote+(mote-1) <= v[i] )
				{
					int w = v.size()-i;
					int w2 = mote;
					int co = 0;
					while ( true )
					{
						w2 += (w2-1);
						co++;
						if ( w2 > v[i] || co == v.size()-i )
							break;
					}
					if ( w <= co )
					{
						sum+=w;
						break;
					}
					else
					{
						sum += co;
						mote = w2+v[i];
					}
					
				}
				else
				{
					sum++;
					mote += (mote-1)+v[i];
				}
			}
			else
			{
				mote += v[i];
			}
		}
		cout<<"Case #"<<o<<": ";
		cout<<sum<<endl;
	}
	return 0;
}
