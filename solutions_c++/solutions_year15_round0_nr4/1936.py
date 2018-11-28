#include<iostream>
using namespace std;
int main()
{
	int T,X,R,C;
	cin>>T;
	for(int i=0;i<T;i++)
	{
		cin>>X>>R>>C;
		int is_solve=0;
		int tmp;
		if(R>C)
		{
			tmp=R;
			R=C;
			C=tmp;
		}	//R<=C
		switch(X)
		{
			case 1:
				is_solve=1;
				break;
			case 2:
				if(R%2==1)
				{
					if(C%2==0) is_solve=1;
				}
				else is_solve=1;
			
				break;
			case 3:

				if(R==2)
				{
					if(C==3) is_solve=1;
				}
				else if(R==3) is_solve=1;


				break;

			case 4:
				if(R==3)
				{
					if(C==4) is_solve=1;
				}
				else
					if(R==4) is_solve=1;

			break;
		}
		cout<<"Case #"<<i+1<<": ";
		if(is_solve)
			cout<<"GABRIEL\n";
		else cout<<"RICHARD\n";
	}
	return 0;
}