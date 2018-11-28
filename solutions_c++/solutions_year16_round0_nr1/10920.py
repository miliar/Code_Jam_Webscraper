#include<iostream>
using namespace std;
int A[10],tot,N;
void reset()
{
  for(int i=0;i<10;i++)
  A[i]=0;
  tot=10;
}
int checkdig(int n)
{
  int r,m=n;
  while(n>0)
  {
    r=n%10;
    if(A[r]==0)
    {
      A[r]=1;
      tot--;
    }
    n=n/10;
  }
  if(tot==0)
    return m;
  else
  return checkdig(N+m);
}
int main(int argc, char const *argv[]) {
  /* code */
  int i,A[10],t,m;
  cin>>t;
  for(i=1;i<=t;i++)
  {
    cin>>N;
    if(N==0)
    {
      cout<<"Case #"<<i<<": INSOMNIA\n";
      continue;
    }
    reset();
    m=checkdig(N);
    cout<<"Case #"<<i<<": "<<m<<endl;
  }
  return 0;
}
