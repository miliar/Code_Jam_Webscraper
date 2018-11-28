#include<iostream>
using namespace std;
int main()
{
    int a[6]={0,1,4,9,121,484};
    int t,c=0;
    cin>>t;
    while(t--)
    {
              c++;
              int m,n,cnt=0;
              cin>>m>>n;
              for(int i=0;i<6;i++)
              {
                      if(a[i]>=m && a[i]<=n)
                      cnt++;
              }
              cout<<"Case #"<<c<<": "; 
              cout<<cnt<<endl;
    }
   // system("pause");
    return 0;
}
