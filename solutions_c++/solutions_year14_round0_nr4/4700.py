#include <iostream>
#include <algorithm>


using namespace std;

const int MAXn=1000+17;
int n;
float first[MAXn];
float second[MAXn];


int usual()
{
  int s=0;
  int flag1 = n-1;
  int flag2 = 0;
  for(int i=n-1;i>=0;i--)
    {
      if(first[i]>second[flag1])
	{
	  flag2++;
	  s++;
	}
      else
	flag1--;
    }
  return s;
}


int unfair()
{

  int s=0;
  int flag2 = 0;
  for(int i=0;i<n;i++)
    {
      if(first[i]>second[flag2])
	{
	  flag2++;
	  s++;
	}
    }
  return s;
}

int main()
{
  int t;
  cin>>t;
  for(int i=1;i<=t;i++)
    {
      cin>>n;
      for(int j=0;j<n;j++)
	cin>>first[j];
      for(int j=0;j<n;j++)
	cin>>second[j];
      sort(first,first+n);
      sort(second,second+n);
      int p1=usual();
      int p2=unfair();
      cout<<"Case #"<<i<<": "<<p2<<" "<<p1<<endl;
    }
  return 0;
}
