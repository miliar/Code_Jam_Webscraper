#include<iostream>
#include<stdio.h>

#define MAX 10
using namespace std;
int main()
{
   // int flag = 0;
    int T;

    cin>>T;
    for(int j=1;j<=T;)
    {   long long N,count=0;
        int Hash_Arr[MAX]={0};
        int flag = 0;
        cin>>N;
        if(N==0)
            {
                cout<<"Case #"<<j<<": INSOMNIA"<<"\n";
                j++;
                continue;

            }
        int n1 = N;
        for(int i=1;;i++)
        {
                N =n1;
                N=i*N;


                    int temp=N,r;
                    while(temp>0)
                    {
                        r=temp%10;
                        temp=temp/10;
                        if(Hash_Arr[r]!=1)
                        {
                            Hash_Arr[r]=1;
                            count++;
                        }
                        if(count==10)
                        {
                            cout<<"Case #"<<j<<": "<<N<<"\n";
                            flag++;
                            break;

                        }


                     }
                     if(flag==1)
                        break;
         }


            j++;

    }
    return 0;
}
