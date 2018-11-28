#include<iostream>
using namespace std;
int main()
{
    int t,c=0;
    cin>>t;
    while(c++<t)
    {
        int smax;
        cin>>smax;
        char a[smax+2];
        cin>>a;
        int n=smax+2,f=0,noOfPeople=0;
        for(int i=0;i<n-1;i++)
        {
            if(i>noOfPeople&&(a[i]-48)!=0)
            {
                f+=(i-noOfPeople);
                noOfPeople+=(i-noOfPeople);
            }
            noOfPeople+=(a[i]-48);
        }
        
        cout<<"Case #"<<c<<": "<<f<<endl;    
    }
    return 0;
}
