#include<iostream>
#include<vector>
#include<map>
#include<iterator>
#include<algorithm>
#include<utility>
#include<numeric>
#include<cstdlib>


using namespace std;

long long z,tc,an[100];


int main()
{
	cin >> tc;

	for(z=0;z<tc;z++)
	{

	    long long a,b,k,i,j,x;
		long long ans=0;

		cin >> a >> b >> k;


		for(i=0;i<a;i++)
        {

            for(j=0;j<b;j++)
            {
                //cout << endl << "i : j : i&j "<< i <<" : "<< j<<" : "<< (i&j) << " ans :" << ans <<endl;

                if((i&j) < k)
                {

                    ans++;
                }

            }
        }

        an[z] = ans;

	}

	for(z=0;z<tc;z++)
    {

        cout<<"Case #"<<z+1<<": "<<an[z]<<endl;
    }

	return 0;
}
