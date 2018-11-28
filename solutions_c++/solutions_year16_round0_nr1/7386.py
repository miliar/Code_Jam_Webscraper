#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    //cout << "Hello world!" << endl;
    long long unsigned t,n,i,j,k,a[10],count,r;
    fstream f,f1;
    f.open("output.txt",ios::out);
    f1.open("input.txt",ios::in);
     //cin>>t;
    f1>>t;
    i=1;
    while(i<=t)
    {

        f1>>n;
        for(j=0;j<10;j++)
            a[j]=0;
        if(n==0)
         //   cout<<"Case #"<<i<<": INSOMNIA\n";
            f<<"Case #"<<i<<": INSOMNIA\n";
        else
        {
            j=1;
            count=0;
            while(count!=10)
            {
             k=n*j;
             while(k!=0)
             {
                 r=k%10;
                 if(a[r]!=1)
                 {
                     count++;
                     a[r]=1;
                 }
                 k=k/10;
             }
              j++;
            }
       // cout<<"Case #"<<i<<": "<<n*(j-1)<<"\n";
        f<<"Case #"<<i<<": "<<n*(j-1)<<"\n";
        }
        i++;
    }
    return 0;
}
