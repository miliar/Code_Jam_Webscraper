#include <fstream>

using namespace std;
ifstream cin("s.in");
ofstream cout("s.out");






int main() 
{
	int a,b,c,f=0,m,u;
	cin>>a;
	for(int i=1;i<=a;i++)
	{
		int d[100][100],r[100][100];
		
		f=0;
		u=i;
		
		cin>>b;
		
		for(int l=1;l<=4;l++)
		{
		    for(int j=1;j<=4;j++)
		    {
			 cin>>d[l][j];
		    }
	    }
	    cin>>c;
	    
		for(int l=1;l<=4;l++)
		{
		    for(int j=1;j<=4;j++)
		    {
			 cin>>r[l][j];
		    }
		}
	    for(int l=1;l<=4;l++)
	    {
		  for(int j=1;j<=4;j++)
		  {
			 if(d[b][l]==r[c][j])
			 {
				 f++;
				 m=r[c][j];
			 }
		  }
		}
		if(f==1)
		{
		  cout<<"Case #"<<i<<": "<<m<<endl;
		}
		else if(f>1)
		{
		  cout<<"Case #"<<i<<": Bad magician!"<<endl;
		}
		else
		{
		  cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
		}
	}
	return 0;
}
