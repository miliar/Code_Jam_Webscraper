#include <bits/stdc++.h>
using namespace std;
int main() {

//freopen("input.txt","r",stdin);
//freopen("output.txt","w",stdout);

	int t;
	map<int,bool>m;
	cin>>t;
	for(int k=1,i;k<=t;k++)
	{

	    cin>>i;
	    cout<<"Case #"<<k<<": ";

	    if(!i)
	    {
	        cout<<"INSOMNIA"<<endl;
	        continue;
	    }

	    m.clear();
	    int j=1;
	    while(true)
	    {
	        int x=i*j;

            while(x!=0)
            {
                int r=x%10;
                m[r]=true;
                x/=10;
            }

	        if(m.size()==10)
	        {
	            cout<<i*j<<endl;
	            break;
	        }

	        j++;
	    }

	}
	return 0;
}
