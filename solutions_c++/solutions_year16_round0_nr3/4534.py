#include <iostream>
#include <bits/stdc++.h>
using namespace std;
typedef unsigned long long int ull;
int cnt=0,N,j,arr[30];
long long int res[20];
ofstream ot;
ull ans[11];
int prime(ull n,int ind)
{
    int flag=0;
    for(ull i=2;i<sqrt(n);i++)//till sqrt
    {
        if(n%i==0)
        {   //cout<<i<<"\n";
            res[ind]=i;
            flag=1;
            break;
        }
    }
    if(flag==1)
        return 0;
    else
        {//cout<<"val"<<n<<endl;
            return 1;

        }
}
void print()
{

    int i;
   
   for(i=0;i<N;i++)
        {cout<<arr[i];
            ot<<arr[i];
         }   
    //cout<<" ";
    ot<<" ";
   for(i=2;i<=10;i++)
        {cout<<res[i]<<" ";
           ot<<res[i]<<" "; 
        }
        ot<<"\n";
        cnt++;
    if(cnt==j)
    {
     exit(0);
    }
}
void comp(int arr[])
{
    unsigned long long int temp=0;
    int flg=0;
    for(int i=2;i<=10;i++)
    {
        //flg=0;
        temp=0;
        for(int j=N-1;j>=0;j--)
        {
           temp=temp+(arr[j]*pow(i,(N-j-1)));
        }
        ans[i]=temp;
        //cout<<"chk"<<i<<'\t'<<temp<<endl;
        int tp=prime(ans[i],i);
        if(tp)
        {
            flg=1;
            break;
        }
    }
    if(flg==1)
        return;
    else
        print();

}
void func(int n)
{
    if(n<=0)
    {
        int temp2=arr[0]&&arr[N-1];
        //cout<<"jhflh\n";
        if(temp2)
            comp(arr);
        else
            return;
    }
    else
    {
        arr[n-1]=0;
        func(n-1);
        arr[n-1]=1;
        func(n-1);
    }
}
int main()
{
    ifstream ob;
    ob.open("file.txt");
    
    ot.open("file2.txt");

    int n;
    int k,T;
    //cin>>T;
    ob>>T;
    //cin>>N>>j;
    ob>>N>>j;
    cout<<"Case #1:\n";
    ot<<"Case #1:\n";
    func(N);

}
