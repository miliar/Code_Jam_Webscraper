#include<iostream>
#include<string.h>
#include<stdio.h>
using namespace std;

void swapp(int arr[105],int beg,int endd)
{
    int temp[105];int q=0,p;
    for(p=beg;p<=endd;p++)
    {
        temp[p]=!arr[p];
    }
    q=endd;
    p=0;
    while(q>=beg)
    {
        arr[p]=temp[q];
        p++;
        q--;
    }
}

int main()

{
   freopen("Bansl.in","r",stdin);
freopen("boutlar1.txt","w",stdout);
    int t,i,j,num=0;
    cin>>t;

    while(t--)
    {
        num++;
        char str[105];
        cin>>str;
        int cnt=0;
        int arr[105];
        int len=strlen(str);
        for(i=0;i<len;i++)
        {
            if(str[i]=='-')
                arr[i]=0;
            else
                arr[i]=1;
        }
        i=len-1;
        while(i>=0)
        {
            if(arr[i]==0)
            {
                if(arr[0]==0)
                 {
                    cnt++;
                   swapp(arr,0,i);
                 }
                else
                {
                    j=0;
                    while(arr[j]==1 && j<i)
                    {
                        arr[j]=0;
                        j++;
                    }
                    cnt++;
                    swapp(arr,0,i);
                    cnt++;
                }
            }
            else
                i--;
        }
        cout<<"Case #"<<num<<": "<<cnt<<endl;
    }
return 0;
}
