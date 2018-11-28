#include<iostream>
using namespace std;
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C.in","w",stdout);
    long long int arr[30]={1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 94249, 698896, 1002001,
     1234321, 4008004, 5221225, 6948496, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004,
      404090404, 522808225},a,b,t,c,i,k=1;
    cin>>t;
     cin.ignore();
    do
    {
              cin>>a>>b;
              c=0;
              for(i=0;i<7;i++)
              {
                                     if(arr[i]>=a && arr[i]<=b)
                                          c++;          
                }
                cout<<"Case #"<<k<<": "<<c<<"\n";
    }while(k++!=t);
    return 0;
}
