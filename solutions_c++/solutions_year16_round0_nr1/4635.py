#include<iostream>
using namespace std;

int main()
{
    bool volt[10];
    long long i;
    int ff=0;
    int t;
    cin>>t;
    for( ff=1; ff<=t; ff++ )
    {
        cin>>i;
        long long k = i;
        if( i==0 ){ cout<<"Case #"<<ff<<": INSOMNIA\n"; continue; }
        for(int j=0; j<10; j++)
            volt[j] = false;
        bool f=false;
        while(!f)
        {
            long long kk = k;
            while( kk )
            {
       //         cout<<kk<<" ";
                volt[ kk - (kk/10)*10 ] = true;
                kk /= 10;
            }
      //      cout<<endl;
            f=true;
            for(int l=0; l<10; l++)
                if( !volt[l] ) f=false;
            k+=i;
        }
        cout<<"Case #"<<ff<<": "<<k-i<<endl;
    }
}
