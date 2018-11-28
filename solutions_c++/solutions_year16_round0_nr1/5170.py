#include<iostream>
#include<string.h>

using namespace std;

 void func(long long n,long long *arr)
{
    while(n>0)
    {
        arr[n%10]=1;
        n=n/10;
    }
}

int main()
{
long long i,j,k,l,m,n,o,t;
cin>>t;

for(o=1;o<=t;o++)
{
cin>>n;
cout<<"Case #"<<o<<": ";
if(n==0)
{
cout<<"INSOMNIA\n";
continue;

}
long long arr[10]={0};
for(i=1;;i++)
{
    func(i*n,arr);
    for(j=0;j<10;j++)
        if(arr[j]==0)
            break;
    if(j==10)
        break;

}
cout<<i*n<<endl;


}



}
