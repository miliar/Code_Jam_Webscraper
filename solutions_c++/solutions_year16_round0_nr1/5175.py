#include<cstdio>
#include<iostream>
#include<fstream>
#include<string>
#include<fstream>
using namespace std;

void func(int *a, int &n, int &sum)
{
    int k=n;
    while(k)
    {  if(!a[k%10])
         {a[k%10]++;
          sum++;
         }
        k/=10;
    }
    /*cout<<n<<endl;
    for(int i=0;i<10;i++)cout<<a[i]<<' ';
    cout<<endl;*/
}

int main()
{
    int t;
    fstream fout;
    fout.open("out1.txt",ios::out);
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        int n;
        cin>>n;
        int f=0;
        int ans=n;
        int a[10];
        for(int i=0;i<10;i++)a[i]=0;


        int sum=0;
        if(n!=0)
         { f=1;
           int j=1;
           do
           {   ans=j*n;
               func(a,ans,sum);
               j++;
           }
           while(sum!=10);

         }
        if(f==0)
        {
            fout<<"Case #"<<i<<": INSOMNIA\n";
        }
        else
            fout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}
