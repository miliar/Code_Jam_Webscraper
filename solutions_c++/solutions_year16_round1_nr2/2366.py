#include <iostream>
#include<string>
using namespace std;

int main() {
    int t,n,s,k;
    int arr[2510]={0};
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        cin>>n;
        k=0;
        for(int j=0;j<(2*n-1)*n;j++)
        {
            cin>>s;
            arr[s]++;
        }
        cout<<"Case #"<<i<<": ";
        for(int j=0;j<2505;j++)
        {
            if(arr[j]%2==1)
               cout<<j<<" ";
            arr[j]=0;
        }
        cout<<endl;
    }
	return 0;
}