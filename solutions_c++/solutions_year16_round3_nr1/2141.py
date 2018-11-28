#include<iostream>
using namespace std;

int main()
{
    int i, j, t, casen, n;
    int p[27];

    cin>>t;

    for( casen=1; casen<=t; ++casen )
    {
        cout<<"Case #"<<casen<<": ";
        cin>>n;
        int max1, max2, max3, sum=0;
        int max1it, max2it, max3it;
        for(i=0; i<n; ++i)
        {
            cin>>p[i];
            sum += p[i];
        }

        if( n==2 )
        {
            while( p[0]>p[1] ){ --p[0]; cout<<"A "; }
            while( p[0]<p[1] ){ --p[1]; cout<<"B "; }
            while( p[0]>0   ){ --p[0]; cout<<"AB "; }
            cout<<endl;
            continue;
        }

        while( sum )
        {
  //          cout<<sum;
            max1=max2=max3=0;
            for(i=0; i<n; ++i)
            {
                if( p[i]>max1 ){ max3=max2; max2=max1; max1=p[i]; max3it=max2it; max2it=max1it; max1it=i; }
                else if( p[i]>max2 ){ max3=max2; max2=p[i]; max3it=max2it; max2it=i; }
                else if( p[i]>max3 ){ max3=p[i]; max3it=i; }
            }

            if( max3 <= (sum-2)/2 && max1-1 <= (sum-2)/2 && max2>0 )
            {
                cout<<char(max1it+'A')<<char(max2it+'A')<<" ";
                sum -= 2;
                --p[ max1it ];
                --p[ max2it ];
            } else{
                cout<<char(max1it+'A')<<" ";
                sum -= 1;
                --p[ max1it ];
            }
        }

        cout<<endl;
    }
}
