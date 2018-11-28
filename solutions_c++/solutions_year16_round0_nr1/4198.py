#include <iostream>
#include <cstdlib>
#include <set>

using namespace std;

int main()
{
	freopen("A-large.in","r",stdin);
 	freopen("A-large.out","w",stdout);
    long long T,N,a,i,c=1;
    cin>>T;
    set<int>S;
    while(T--)
    {
    	cin>>N;
    	if(N==0)cout<<"Case #"<<c<<": "<<"INSOMNIA"<<endl;
    	else
		{
    	for(i=N;;i+=N)
    	{
    		a=i;
    		do
    		{
    			S.insert(a%10);
    			a/=10;	
			}
			while(a);
			if(S.size()==10) break;
		}
		cout<<"Case #"<<c<<": "<<i<<endl;
		}
		S.clear();
		c++;
	}
}
