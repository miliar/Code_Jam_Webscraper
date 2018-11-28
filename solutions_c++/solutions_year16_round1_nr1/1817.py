#include<iostream>
#include<string.h>
#include<vector>
#include<algorithm>
using namespace std;



int main()
{
long long i,j,k,l,h,m,n,o,t,c,s;
char str[1002];
char arr[5002];
cin>>t;
for(o=1;o<=t;o++)
{
cin>>str;
cout<<"Case #"<<o<<": ";
long long len=strlen(str);
l=2499;
h=2501;
arr[2500]=str[0];
for(i=1;i<len;i++)
{
    if(str[i]>=arr[l+1])
    {
        arr[l]=str[i];
        l--;
    }
    else
        arr[h++]=str[i];
}
for(i=l+1;i<h;i++)
    cout<<arr[i];
cout<<endl;


}



}
