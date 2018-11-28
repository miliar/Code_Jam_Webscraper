#include<iostream>
using namespace std;

int main()
{
  int ia,ja,ta,sa,count,pa;
  string a;
  cin>>ta;

  for(ia=0; ia<ta; ia++)
  {
    count=0;
    pa=0;
    cin>>sa;
    cin>>a;

    for(ja=0; a[ja]!='\0'; ja++)
    {
      if(pa<ja && a[ja]!=48)
      {
        count=count+(ja-pa);
        pa=pa+count;
      }
      pa=pa+(a[ja]-48);
    }
    cout<<"Case #"<<ia+1<<": "<<count<<endl;
  }
  return 0;
}
