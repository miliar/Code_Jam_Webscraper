#include <iostream>
#include<algorithm>
#include<stdio.h>

using namespace std;

int main()
{
    int t, a[26],n,s=0,i,j=0;
    cin>>t;

    while(j<t)
    {
        j++;
        cin>>n;
        s=0;
        for(i=0;i<n;i++)
        {
            cin>>a[i];
            s+=a[i];
        }
        cout<<"Case #"<<j<<": ";
        if(n==2)
        {
            s=s/2;
            for(i=0;i<s;i++)
                cout<<"AB ";
        }
        else
        {
          int k;
          
          while(s>2)
          {
          	k= distance(a, max_element(a,a+n));
          	s--;
          a[k]--;
          printf("%c ",k+65);
          }
          k= distance(a, max_element(a,a+n));
          printf("%c",k+65);
          a[k]--;
          k= distance(a, max_element(a,a+n));
          printf("%c",k+65);
          //cout<<endl;
        }
        cout<<endl;
    }
    return 0;
}
