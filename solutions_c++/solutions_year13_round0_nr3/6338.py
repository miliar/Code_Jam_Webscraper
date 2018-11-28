#include <iostream>
#include <cstdio>
using namespace std;

int a[5]={1,4,9,121,484};

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int sum;
    int n;
    cin >>n;
    for(int k=1; k<=n; ++k){
        sum=0;
        int first,last;
        cin>>first>>last;
        for(int i=0; i<5; ++i){
            if(first<=a[i] && a[i]<=last)
                sum++;
        }
        cout<<"Case #"<<k<<": "<<sum<<endl;

    }

}
