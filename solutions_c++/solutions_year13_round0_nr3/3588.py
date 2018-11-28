#include<iostream>
using namespace std;

main()
{
    int t, k, low, high, count, i;
    int a[]={1,4,9,121,484};
    cin>>t;

    for(k=0; k<t; k++)
    {
                 count=0;
                 cin>>low>>high;

                 for(i=0;i<5;i++)
                 if(a[i]>=low && a[i]<=high)
                 {
                     count++;
                 }

                 cout<<"Case #"<<k+1<<": "<<count<<"\n";
    }
}
