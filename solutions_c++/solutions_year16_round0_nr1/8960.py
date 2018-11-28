#include<iostream>
#include<algorithm>
#include<sstream>
#include<stdio.h>
using namespace std;
int main()
{
    int arr[10];
    long long int i,t,temp,len,flag,n,l,temp1,k;
    string str;
    freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    k=1;
    while(k<=t)
    {
        cin>>str;
        n=atoi(str.c_str());
            for(i=0;i<10;i++)
            arr[i]=-1;

        if(n==0)
          cout<<"Case #"<<k<<": INSOMNIA"<<endl;
        else{
            l=1;
        while(1)
        {
            flag=0;
        len=str.size();
        for(i=0;i<len;i++)
        {
            temp=((int)str[i]-48);
            arr[temp]=temp;
           // cout<<"temp="<<temp;
        }
        //cout<<"hello";
        for(i=0;i<10;i++)
        { //cout<<"arr[i]="<<arr[i];
            if(arr[i]==-1)
            {
                flag=1;
                break;
            }


        }
       // cout<<"flag="<<flag;
        if(flag==0)
        {   n=atoi(str.c_str());
            cout<<"Case #"<<k<<": "<<n<<endl;
            break;
        }

        temp1=(l+1)*n;
        //cout<<"temp1="<<temp1;
        stringstream ss;
        ss << temp1;
        str=ss.str();
        l++;
        }
        }
        k++;


    }

    return 0;

}
