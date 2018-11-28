#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,i;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        int  number[10]={0};
        long long int n;
        int j,l;
        cin>>n;
        l=0;j=0;
        if(n==0)
        {
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
            continue;
        }
        int arr[10000]={0},arr2[10000]={0};
        while(n)
        {
            l++;
            arr[j]=n%10;
            arr2[j++]=arr[j];
            n=n/10;
        }

      int count=0,num,k,flag=0,carry,len1=l-1,len2=l-1;
        for(j=1;j;j++)
        {   len1=len2;
            carry=0;
            for(k=0;carry!=0||k<=l-1;k++)
            {
                    num=arr[k]*j+carry;
                    carry=num/10;
                    arr2[k]=num%10;
                        if(k>len1)
                            len2++;

                    if(number[arr2[k]]==0)
                    {
                        number[arr2[k]]++;
                        count++;
                    }
                    if(count==10)
                        flag=1;


            }

            if(flag)
                break;
        }
          int m;
            cout<<"Case #"<<i<<": ";
            for(m=len2;m>=0;m--)
                cout<<arr2[m];
            cout<<endl;

    }
}
