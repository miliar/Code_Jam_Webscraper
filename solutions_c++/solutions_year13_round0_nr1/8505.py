#include <iostream>
using namespace std;

int main()
{
	int t;
	int i,j, xr[4],or[4],xc[4],oc[4],d;
	bool ist;
	char a[5][5];
	int d1=0,d2=0;
	cin>>t;
	

	for(int l=0; l<t; ++l)
	{
		d=0;
		ist=false;
		d1=d2=0;

		for(i=0; i<4; ++i)
		{
			xr[i]=xc[i]=oc[i]=or[i]=0;
		}

		for(i=0; i<4; ++i)
		{
			for(j=0; j<4; ++j)
			{
				cin>>a[i][j];
				if(a[i][j]=='X')
				{
					++xr[i];
					++xc[j];
				}
				if(a[i][j]=='O')
				{
					++or[i];
					++oc[j];
				}
				if(a[i][j]=='T')
				{
					ist=true;
					++or[i];
					++oc[j];
				    ++xr[i];
					++xc[j];
				}
				
				if(a[i][j]=='.')
					++d;
			}
		}

		cout<<"Case #"<<l+1<<": ";
		bool over=false;
		for(i=0; i<4; ++i)
		{
			if(xr[i]==4 || xc[i]==4)			
			{
				cout<<"X won"<<endl;
				over=true;
				continue;
			}

			if(or[i]==4 || oc[i]==4)			
			{
				cout<<"O won"<<endl;
				over=true;
				continue;
			}
		}

		if( (a[0][0]=='O' || a[0][0]=='T') && (a[1][1]=='O' || a[1][1]=='T') && (a[2][2]=='O' || a[2][2]=='T') && (a[3][3]=='O' || a[3][3]=='T') && !over ) 
		{
			cout<<"O won"<<endl;
			over=true;
		}

		if( (a[0][0]=='X' || a[0][0]=='T') && (a[1][1]=='X' || a[1][1]=='T') && (a[2][2]=='X' || a[2][2]=='T') && (a[3][3]=='X' || a[3][3]=='T') && !over ) 
		{
			cout<<"X won"<<endl;
			over=true;
		}

		if( (a[0][3]=='O' || a[0][3]=='T') && (a[1][2]=='O' || a[1][2]=='T') && (a[2][1]=='O' || a[2][1]=='T') && (a[3][0]=='O' || a[3][0]=='T') && !over) 
		{
			cout<<"O won"<<endl;
			over=true;
		}

		if( (a[0][3]=='X' || a[0][3]=='T') && (a[1][2]=='X' || a[1][2]=='T') && (a[2][1]=='X' || a[2][1]=='T') && (a[3][0]=='X' || a[3][0]=='T') && !over) 
		{
			cout<<"X won"<<endl;
			over=true;
		}

		if(!over)
		{
			if(d==0)
				cout<<"Draw"<<endl;

			else
				cout<<"Game has not completed"<<endl;
		}



	}

	return 0;
}