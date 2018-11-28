#include <bits/stdc++.h>
using namespace std;
int main() {

//freopen("input.txt","r",stdin);
//freopen("output.txt","w",stdout);
	int t;
	map<int,int>m;
	scanf("%d",&t);

	for(int k=1,i;k<=t;k++)
	{
	    scanf("%d",&i);
	    cout<<"Case #"<<k<<": ";

	    if(!i)
	    {
	        cout<<"INSOMNIA"<<endl;
	        continue;
	    }

	    m.clear();
	    int j=1;

      do
	    {
	        int x=i*j;

            while(x)
            {
                int rm=x%10;
                m[rm]=1;
                x/=10;
            }

	        if(m.size()==10)
	        {
	            cout<<i*j<<endl;
	            break;
	        }
          j++;
	    }while(1);

	}
	return 0;
}
