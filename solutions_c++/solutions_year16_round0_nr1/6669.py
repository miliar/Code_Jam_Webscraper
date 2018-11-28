#include<iostream>
#include<cstdio>
using namespace std;
int arr[10];
void split(long long n)
{
  long long j=n;
  while(j)
  {
    int k= j%10;
    arr[k]=1;
    j/=10;
  }
}
bool check()
{
  for(int i=0;i<10;i++)
  {
    if(arr[i]==0)
      return false;
  }
  return true;
}
int main()
{
  long long T,n,i,j,k,l,m;
  ios::sync_with_stdio(false);
  // freopen("in.txt","r",stdin);
  // freopen("out.txt","w",stdout);
  cin>>T;
  for(l=0;l<T;l++)
  {
    cin>>n;
    if(n==0)
      cout<<"Case #"<<(l+1)<<": "<<"INSOMNIA"<<endl;
    else
    {
      j=n;
      k=2;
      for(i=0;i<10;i++) arr[i]=0;
      split(n);
      bool done =check();
      if(done)
        cout<<"Case #"<<(l+1)<<": "<<n<<endl;
      else
      {
        for(m=2;;m++)
        {
          n=j*m;
          split(n);
          done=check();
          if(done)
            break;
        }
        cout<<"Case #"<<(l+1)<<": "<<n<<endl;
      }
    }
  }
}
