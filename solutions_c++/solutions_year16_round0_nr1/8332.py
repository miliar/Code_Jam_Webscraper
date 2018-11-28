#include <iostream>
#include<cstdio>
#include<cstdlib>

using namespace std;
int arr[10];
void init();
int check();
void split(int n);

int main()
{
    freopen("input_file.in","r",stdin);
    freopen("output_file_large.out","w",stdout);

  long long int t,i,j,n;
   int cnt=1;
   cin>>t;



   while(t--)
   {
     cin>>n;
     if(n==0)
     {
      cout<<"Case #"<<cnt<<": INSOMNIA"<<endl;
     }else{

     init();
   long long  int p=1,tn;
     while(!check())
     {
         tn=n*p;
    //     cout<<"I*N:"<<p<<"*"<<n<<":"<<n<<endl;
         split(tn);
         p++;
     }

    cout<<"Case #"<<cnt<<": "<<tn<<endl;
     }


     cnt++;
   // cout<<arr[8]<<endl;

   } //eowhile



    return 0;
}


void init()
{
    for(int i=0;i<10;i++)
        arr[i]=0;
    //arr[]={0};
}

int check()
{
    int i,flag=1;
    for(i=0;i<10;i++)
    {
        if(arr[i]==0)
        {
           flag=0;
           return 0;
        }

    }

    return 1;
}


void split(int n)
{
    int i,t;

    while(n)
    {
        t=n%10;
        arr[t]=arr[t]++;
        n=n/10;
    }

/*for(i=0;i<10;i++)
{
    cout<<" "<<arr[i];
}*/

}
