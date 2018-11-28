# include <iostream>

using namespace std;

int main()
{
	long *x,t,j,b[10],p,a[10];
	int y,f;
	cin >> y;
	x = new long[y];
	for (int i=1; i<=y;i++)
	{
		cin >> x[i-1];
	}
	for (int i=0; i<y;i++)
	{
		cout << "Case #" << i+1 <<": ";
		for (int m = 0; m<10; m++)
			b[m] = 0;
		if(x[i]!=0)
		{	
			t = x[i];
			for ( int l=2; 1;l++)
			{
				j=0;
				p = t;
				while(t!=0)
				{
					a[j] = t%10;
					j++;
					t=t/10;
				}
				t = p;
				for (int k=0; k<j; k++)
				{
					b[a[k]] = 1; 
				}
				f = 0;
				for (int k=0; k<10; k++)
				{
					if(b[k]!=1)
						f = 1;
				}
				if (f == 0)
				{
					cout << t <<endl;
					break;
				}
				else
					t = x[i] * l;
					
			}
		}
		else
			cout << "INSOMNIA" <<endl;
	}
	return 0;
}
