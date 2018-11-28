#include <stdio.h>
#include<iostream>
#include<set>
#include<algorithm>
#include <limits>
#include<math.h>
#include<ctype.h>
#include<string.h>
#include<vector>
#include <iomanip>
#include <locale>
#include <sstream>
using namespace std;
int main()
{
   freopen("A-large.in","r", stdin);
    freopen ("A-large.out","w",stdout);

    int t;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        int arr[]={1,1,1,1,1,1,1,1,1,1};
        int n,counter=1;
        cin>>n;

        bool found=true;
        while(found&&n!=0)
        {
            int x;
            x=n*counter;
            while(x!=0)
            {
                arr[x%10]=0;
                x/=10;
            }
            bool no=false;
            for(int j=0;j<10;j++)
            {
                if(arr[j]==1)
                 no=true;
            }
            if(no)
                no=false;
            else
                found=false;

                counter++;
        }
        if(n==0)
        {
            cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;

        }
        else
          cout<<"Case #"<<i<<": "<<n*(counter-1)<<endl;
    }

    return 0;
}
