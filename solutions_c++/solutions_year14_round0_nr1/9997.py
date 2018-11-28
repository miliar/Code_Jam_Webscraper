# include<fstream>

using namespace std;

ifstream cin("a.in");
ofstream cout("a.out");

int main()
{
	int n;
	cin>>n;
	
	for(int qi=1;qi<=n;qi++)
	{
		int a[5][5],b[5][5];
		
		int m,x,y,sum=0,nu;
	
		cin>>x;
		for(int j=1;j<=4;j++)
		    for(int k=1;k<=4;k++)	
				  cin>>a[j][k];
		cin>>y;
		for(int q=1;q<=4;q++)
			for(int h=1;h<=4;h++)
			     cin>>b[q][h];
		for(int ai=1;ai<=4;ai++)
		{
		    for(int aj=1;aj<=4;aj++)
		    {
				   if(a[x][ai]==b[y][aj])
					{
					     sum++;
						  if(sum==1)
						    nu=a[x][ai];
					}
			 }
		}
		if(sum==1)
		 cout<<"Case #"<<qi<<": "<<nu<<endl;
		else if(sum==0)
		 cout<<"Case #"<<qi<<": "<<"Volunteer cheated!"<<endl;
		else if(sum>=2)
		 cout<<"Case #"<<qi<<": "<<"Bad magician!"<<endl;
		 
	}
	return 0;
}
