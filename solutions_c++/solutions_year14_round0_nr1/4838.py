#include <iostream>


using namespace std;
int jadval1[4][4],jadval2[4][4];
int a,b;
int adad;
void getin()
{
  cin>>a;
  a--;
  for(int i=0;i<4;i++)
    for(int j=0;j<4;j++)
      cin>>jadval1[i][j];

  cin>>b;
  b--;
  for(int i=0;i<4;i++)
    for(int j=0;j<4;j++)
      cin>>jadval2[i][j];
}

int tedad()
{
  int t=0;
  for(int i=0;i<4;i++)
    for(int j=0;j<4;j++)
      if(jadval1[a][i]==jadval2[b][j])
	{
	  t++;
	  adad=jadval1[a][i];
	  // cerr<<adad<<endl;
	}
  return t;
}

int main()
{
  int t;cin>>t;
  for(int i=1;i<=t;i++)
    {
      getin();
      int tmp = tedad();
      if(tmp==0)
	cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
      else
	{
	  if(tmp==1)
	    cout<<"Case #"<<i<<": "<<adad<<endl;
	  else
	    cout<<"Case #"<<i<<": Bad magician!"<<endl;
	}
    }
  return 0;
}
