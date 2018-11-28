#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{
    long int t,c,len,i,count;
    string str;
    freopen("B-large.in","r",stdin);
    freopen("output1.txt","w",stdout);
    cin>>t;
    c=1;
    while(c<=t)
    {
        cin>>str;
        count=0;
        len=str.size();
        for(i=0;i<len-1;i++)
        {
            if(str[i]!=str[i+1])
            count+=1;
        }
        //cout<<str[len];
        if(str[len-1]=='-')
        count+=1;
        cout<<"Case #"<<c<<": "<<count<<endl;
        c++;
    }
    return 0;

}
