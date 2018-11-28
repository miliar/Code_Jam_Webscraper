#include <stdio.h>
#include <iostream>

using namespace std;

int main()
{
    int t,i,j,k,l,a[10];
    long int n,c;
    cin >> t;
    
    
    for(i=0; i<t;i++)
    {
        cin >> n;
        c=n;
        
        
        a[0] = 0;
        a[1] = 0;
        a[2] = 0;
        a[3] = 0;
        a[4] = 0;
        a[5] = 0;
        a[6] = 0;
        a[7] = 0;
        a[8] = 0;
        a[9] = 0;

        l=0;
        k=0;
        
        while((l!=10) && k<1000)
        {

            for(; c>0; c/=10)
            {
                j=c%10;

                if(a[j] == 0)
                {
                    //cout<<j << " ";
                    a[j] = 1;
                    l++;
//                    cout<<a[j]<<endl;
                }
            }

            c= n*(k+2);
           // cout<<"k="<<k<<endl;
            k++;

        }
        
        if( k== 1000)
            cout << "Case #" << (i+1) << ": INSOMNIA" << endl;
        else
            cout << "Case #" << (i+1) << ": " << (n*k) << endl;
        
        
    }
}