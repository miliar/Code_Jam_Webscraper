#include <iostream>
using namespace std;
int A[4][4],B[4][4],v=1,x=0,b=0,r1,r2;;
void inp();
void rst();
void wrk();
int main() 
{
	int t,i;
	cin>>t;
	for(i=1;i<=t;i++)
	{
		rst();
		inp();
		wrk();
		cout<<"Case #"<<i<<": ";
		if(v==1)
		{
			cout<<"Volunteer cheated!";
		}
		else if(b==1)
		{
			cout<<"Bad magician!";
		}
		else
		{
			cout<<x;
		}
		cout<<endl;
	}
	return 0;
}

void rst()
{
	v = 1;
	b = 0;
	x = 0;
}

void inp()
{
	int i,j;
	cin>>r1;
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			cin>>A[i][j];
		}
	}
	cin>>r2;
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			cin>>B[i][j];
		}
	}
	r1 -= 1;
	r2 -= 1;
}

void wrk()
{
	int i,j;
	for(i=0;i<4;i++)
	{
		for(j=0;j<4;j++)
		{
			if(v==1 && (A[r1][i] == B[r2][j]))
			{
				v = 0;
				x = A[r1][i];
			}
			else if(v==0 && A[r1][i] == B[r2][j])
			{
				b = 1;
				break;
			}
		}
		if(b==1)
		{
			break;
		}
	}
}