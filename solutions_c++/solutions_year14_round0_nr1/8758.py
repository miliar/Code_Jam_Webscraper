#include<iostream>

using namespace std;

int A[5][5];
int B[5][5];

int check(int r1,int r2)
{
  int t=-1,temp;
  for(int i=1;i<5;i++)
  {
    temp=A[r1][i];
      for(int j=1;j<5;j++)
      {
	if(B[r2][j]== temp)
	{
	  if(t==-1)t=temp;
	  else return 17;
	}
      }
  }
  return t;	
}


int main()
{
  int n,a1,a2;
  cin>>n;
  for(int k=1;k<=n;k++)
  {
    cin>>a1;
    for(int i=1;i<5;i++)
      for(int j=1;j<5;j++)
	  cin>>A[i][j];
      
    cin>>a2;  
      
    for(int i=1;i<5;i++)
      for(int j=1;j<5;j++)
	  cin>>B[i][j];  
      
    int res=check(a1,a2);
    cout<<"Case #"<<k<<": ";
    
    if(res==-1) cout<<"Volunteer cheated!\n";
    else if(res==17) cout<<"Bad magician!"<<endl;
    else cout<<res<<endl;
  }
    
  
}