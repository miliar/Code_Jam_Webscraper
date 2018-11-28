#include<cstdlib>
#include<iostream>
using namespace std;
int main()
{
    long long T, r, s;
    cin>>T;
    for(int i=0; i<T; i++)
    {
            cin>>r;
            cin>>s;
            long long  j=1;
            long n=0;
            while(s>=0)
            {
                 long k=(r+j)*(r+j)-(r+j-1)*(r+j-1);      
                 s=s-k;
                 j+=2;
                 if(s>=0)
                 n++;
            }
            char sol[30];
            sprintf(sol,"Case #%d: %d", i+1, n);
            cout<<sol<<endl;
    }
    return 0;
}
