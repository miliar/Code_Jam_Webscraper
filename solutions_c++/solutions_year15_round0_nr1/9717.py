#include <iostream>

using namespace std;

int main()
{
  int n;
  int k;
  char a;
  int b;
  int osoby;
  int wstalo;
  cin>>n;
  for(int i=0;i<n;i++)
  {
    osoby=0;
    wstalo=0;
    cin>>k;
    for(int j=0;j<=k;j++)
    {
      cin>>a;
      b=a-48;
      if(j>wstalo&&b!=0){
        osoby+=j-wstalo;
        wstalo+=osoby;
        }
      wstalo+=b;
    }
    cout<<"Case #"<<i+1<<": "<<osoby<<'\n';
  }

  return 0;
}