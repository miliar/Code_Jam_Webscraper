#include<iostream>
using namespace std;

int main()
{
  int i,j,t,s,count,p;
  string a;
  cin>>t;

  for(i=0; i<t; i++)
  {
    count=0;
    p=0;
    cin>>s;
    cin>>a;

    for(j=0; a[j]!='\0'; j++)
    {
      if(p<j && a[j]!=48)
      {
        count=count+(j-p);
        p=p+count;
      }
      p=p+(a[j]-48);
    }
    cout<<"Case #"<<i+1<<": "<<count<<endl;
  }
  return 0;
}
