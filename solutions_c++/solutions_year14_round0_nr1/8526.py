//In the name of GOd

#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>
using namespace std;
int a[5][5],b[5][5];
//vector <string> ll;
ifstream fin("1.txt");
ofstream fout("A-small-arrempt3.out");
int main()
{
  //#define cin fin
  //#define cout fout
  int t;
  cin>>t;
  for(int i=1;i<=t;i++)
    {
      int ans1,ans2;
      cin>>ans1;
      for(int j=1;j<=4;j++)
	cin>>a[1][j]>>a[2][j]>>a[3][j]>>a[4][j];
      cin>>ans2;
      for(int j=1;j<=4;j++)
	cin>>b[1][j]>>b[2][j]>>b[3][j]>>b[4][j];
      int rans=-10,n=0;
      for(int j=1;j<=4;j++)
	for(int pp=1;pp<=4;pp++)
	if(a[j][ans1]==b[pp][ans2])
	  {
	    n++;
	    rans=a[j][ans1];
	  }
      if(n>1)
	{
	  cout<<"Case #"<<i<<": "<<"Bad magician!"<<endl;
	  continue;
	}
      else if(n==1)
	cout<<"Case #"<<i<<": "<<rans<<endl;
      else if(n==0)
	cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
    }
  return 0;
}
