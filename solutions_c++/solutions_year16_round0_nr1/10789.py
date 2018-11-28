#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output.out","w",stdout);
    int t,l=1;
    cin>>t;
    while(t--)
    {
        long int n,c;
        int a[10]={0},j=1,cnt=0;
        cin>>n;
        c=n;
        while(j<=100)
        {
          n=c*j;  cnt=0;       
          while(n>0)
          {
            int i=n%10;
            a[i]++;
            n=n/10;
          }
          for(int i=0;i<10;i++)
             if(a[i]==0)
               cnt=1;
          if(cnt==0)
          {  cout<<"Case #"<<l<<": "<<c*j<<endl; break; }
          j++;
        }
        if(cnt==1)
        cout<<"Case #"<<l<<": INSOMNIA"<<endl;
        l++;
    }
    return 0;
}

