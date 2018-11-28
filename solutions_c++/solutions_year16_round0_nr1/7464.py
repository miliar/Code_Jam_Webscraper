#include <iostream>

#include <set>

using namespace std;


int main()

{

    int t;

    cin>>t;

    for(int i=0;i<t;i++)

    {

    	long n;

    	cin>>n;

    	cout<<"Case #"<<i+1<<": ";

    	if(n==0) cout<<"INSOMNIA\n";

    	else

    	{

    		set<int> s;

    		long k=1,o;

    		while(s.size()<10)

    		{

    			long p=k*n;

    			o=p;

    			while(p>0)

    			{

    				s.insert(p%10);

    				p/=10;

    			}

    			k++;

    		}

    		cout<<o<<endl;

    	}

    }

    return 0;

}
