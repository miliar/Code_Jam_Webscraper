#include<iostream>
using namespace std;
int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++){
    int a,b,k,c=0;
    cin>>a>>b>>k;
    for(int l=0;l<a;l++)
        for(int m=0;m<b;m++)
    {
        if((l&m)<k)
            c++;
    }
    cout<<"Case #"<<i+1<<": "<<c<<endl;
    }
    return 0
}
