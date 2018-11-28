#include<iostream>
#include<algorithm>
#include<sstream>
#include<stdio.h>
using namespace std;
int main()
{

    long long int i,t,temp,len,max,k,j,l;
    char current;
    string str;
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    k=1;
    while(k<=t)
    {
        cin>>str;
    len=str.size();
    char arr[2*len];
    arr[len]=str[0];
    for(i=0;i<2*len;i++)
    {
        arr[i]='0';
    }
    arr[len-1]=str[0];
    current=str[0];
    j=len-1;
    l=len-1;
    for(int i=1;i<len;i++)
    {
        if(str[i]>=current)
        {
            j--;
            arr[j]=str[i];
            current=arr[j];
           // cout<<"current="<<current;

        }
        else
        {
            l++;
            arr[l]=str[i];
            //cout<<"else="<<arr[l];
        }

    }
    cout<<"Case #"<<k<<": ";
    for(i=0;i<2*len;i++)
    {
        if(arr[i]=='0')
        continue;
        cout<<arr[i];
    }
    cout<<endl;
    k++;
    }

    return 0;
}
