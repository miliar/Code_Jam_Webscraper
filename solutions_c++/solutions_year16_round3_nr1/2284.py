#include<iostream>
#include<string.h>
#include<vector>
#include<algorithm>
using namespace std;



int main()
{
long long i,j,k,l,h,m,n,o,t,c,s;
char w1[25],w2[25];
cin>>t;
for(o=1;o<=t;o++)
{
    int arr[26]={0};
   cin>>n;
cout<<"Case #"<<o<<": ";
c=0;
for(i=0;i<n;i++)
{
    cin>>j;
    arr[i]+=j;
    c+=j;
}
n=c;
while(n>0)
{
    if(n==1)
    {
        for(i=0;i<26;i++)
        {
            if(arr[i]!=0)
            {
                char d='A'+i;
                cout<<d<<" ";
                n--;
                break;
            }
        }
    }
    if(n==0)
        break;
        for(i=0;i<26;i++)
        {
            if(arr[i]>=2)
            {
                j=n-2;
                arr[i]-=2;
                int flag=1;
                for(k=0;k<26;k++)
                {
                    if(arr[k]>j/2)
                    {
                        flag=0;
                        break;
                    }
                }
                if(flag)
                {
                    char d='A'+i;
                cout<<d<<d<<" ";
                n-=2;
                goto hi;
                }
                else
                    arr[i]+=2;
            }
        }

        for(i=0;i<26;i++)
        {
            if(arr[i]>=1)
            {
                arr[i]-=1;

                for(j=i+1;j<26;j++)
                {
                    if(arr[j]>0)
                    {
                        arr[j]-=1;
                        int flag=1;
                for(k=0;k<26;k++)
                {
                    if(arr[k]>(n-2)/2)
                    {
                        flag=0;
                        break;
                    }
                }
                if(flag)
                {

                    char d='A'+i;
                    char b='A'+j;
                cout<<d<<b<<" ";
                n-=2;
                goto hi;
                }
                else
                    arr[j]+=1;


                    }
                }
                arr[i]+=1;
            }
        }
        for(i=0;i<26;i++)
        {
            if(arr[i]!=0)
            {
                arr[i]-=1;


            int flag=1;
                for(k=0;k<26;k++)
                {
                    if(arr[k]>(n-1)/2)
                    {
                        flag=0;
                        break;
                    }
                }
                if(flag)
                {

                    char d='A'+i;
                cout<<d<<" ";
                n-=1;
                goto hi;
                }
                else
                    arr[i]+=1;
            }


        }


  hi:
      ;
}


cout<<endl;
}



}
