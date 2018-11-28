#include <iostream>
#include <algorithm>
using namespace std;
int main()
{
    int t,i,j,k,max1,n,time;
    freopen("output.txt", "w" , stdout);
	freopen("input.txt", "r" ,stdin);
    cin>>t;
    for(k=1;k<=t;k++)
	{
        cin>>n;
        int p[n+1];
        max1 = 0;
        for(i=0;i<n;i++)
        {
            cin>>p[i];
            max1 = max(max1,p[i]);
        }
        int mns = max1;
        time = 0;

        for(i=1 ; i <= max1; i++)
		{
            time=i;
            for(j=0;j<n;j++)
			{
                if(p[j]>i)
				{
                    if( p[j]%i == 0 )
					{
                        time += (p[j]/i -1);
                    }
                    else
					{
                        time += (p[j]/i);
                    }
                }
            }
            mns=min(mns,time);
        }
        cout<<"Case #"<<k<<": "<<mns<<endl;
    }
    return 0;
}


