#include <iostream>
using namespace std;


int main()
{
  int T;
  cin>>T;
  string buf;
  char prev;
  int res;
  for(int t=0;t<T;t++)
  {
    cin>>buf;
    prev='+';res=0;
    for(int i=buf.length()-1;i>=0;i--)
    {
      if(buf[i]!=prev)
      {
	res++;
	prev=buf[i];
      }
    }
    cout<<"Case #"<<t+1<<": "<<res<<endl;
  }
}