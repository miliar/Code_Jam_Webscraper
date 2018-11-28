#include <iostream>
#include <cstdlib>
#include <set>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#include <map>

using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
 	freopen("A-large.out","w",stdout);
    long long T,N;
    cin>>T;
    for(N=1;N<=T;N++)
    {
    	long long n,a,size=0,j;
    	char i;
    	cin>>n;
    	vector<pair<int,char> >V;
    	for(i='A',j=0;j<n;j++,i++)
    	{
    		cin>>a;
    		V.push_back(make_pair(a,i));
    		size+=a;
		}
    	cout<<"Case #"<<N<<": ";
    	while(size)
    	{	
    		sort(V.rbegin(),V.rend());
    		if(size>3)
    		{
    			if(V[0].first-V[1].first>=2)
    			{
    				cout<<V[0].second<<V[0].second<<' ';
    				V[0].first-=2;
					size-=2;
				}
				else if(V[0].first-V[1].first==1&&size%2==0)
				{
					cout<<V[0].second<<V[1].second<<' ';
    				V[0].first--;
    				V[1].first--;
					size-=2;
				}
				else if(V[0].first-V[1].first==1&&size%2==1)
				{
					cout<<V[0].second<<' ';
    				V[0].first--;
					size--;
				}
				else if(V[0].first-V[1].first==0)
				{
					cout<<V[0].second<<V[1].second<<' ';
    				V[0].first--;
    				V[1].first--;
					size-=2;
				}
			}
    		else if(size==3)
    		{
				cout<<V[0].second<<' ';
				V[0].first--;
				size--;
			}
			else if(size==2)
			{
				if(V[0].first>1)
				{
					cout<<V[0].second<<V[0].second<<endl;
    				V[0].first-=2;
					size-=2;
				}
				else 
				{
					cout<<V[0].second<<V[1].second<<endl;
    				V[0].first--;
    				V[1].first--;
					size-=2;
				}
			}
		}
    	
    	
	}
	return 0;
}
