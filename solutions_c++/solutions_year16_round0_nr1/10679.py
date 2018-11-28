#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
     freopen("A-large.in","r",stdin);
   freopen("New Text Document.txt","w",stdout);
int t;
cin>>t;
for(int i=1;i<=t;i++)
{


    long long n;
    cin>>n;
    cout<<"Case #"<<i<<": ";
    if(n==0)
        cout<<"INSOMNIA"<<endl;
    else
        {
            string res="";
              long long temp=n;
              int k=2;
            while(res.size()<10)
            {

                   while(n>0)
                {
                if(!(res.find(n%10+48)!=res.npos))
                    res+=(n%10+48);
                n/=10;

                }
                if(res.size()==10)
                {
                    n=temp*(k-1); break;
                }
                n=temp*k , k++;
            }
            cout<<n<<endl;


        }



}
    return 0;
}
