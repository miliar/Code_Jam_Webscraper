#include <iostream>
#include<fstream>
#include <stdio.h>
#include<math.h>
#include<cmath>

using namespace std;


int main()
{
     freopen ("A-large.in","r",stdin);
    freopen ("A-large.out","w",stdout);
    int t;
    cin>>t;
    for(int j=0; j<t; j++)
    {
        bool arr[10]= {false};
        int numberOfTrue =0 ;
        long long int n;
        cin >> n;
        long long  int result =1;
        for(int i=1; i<100; i++)
        {
            result = n*i;

            while (result > 0)
            {
                int digit = result%10;
                result /= 10;
                //print digit
                if(!arr[digit])
                {
                    arr[digit] = true;
                    numberOfTrue++;
                }

            }
            if(numberOfTrue == 10)
            {
                cout<<"Case #"<<j+1<<": "<<n*i<<endl;
                break;

            }
        }
        if(numberOfTrue < 10)
        {
            cout<<"Case #"<<j+1<<": INSOMNIA"<<endl;
        }
    }

    return 0;
}
