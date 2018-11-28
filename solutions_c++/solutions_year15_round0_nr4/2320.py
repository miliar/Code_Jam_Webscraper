#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main()
{
	ios::sync_with_stdio(0);
	int z; cin>>z; for(int x=0; x<z; x++)
	{
		int X,R,C; cin>>X>>R>>C;

		bool B;

		if(X==1)
			B=true;

		if(X==2)
		{
			if(R*C % 2 == 0)
				B=true;
			else
				B=false;
		}

		if(X==3)
		{
			B=false;

			if(R> C)
				swap(R,C);
			if(R == 2 && C== 3)
				B=true;
			if(R==3 && C==3)
				B=true;
			if(R==3 && C==4)
				B=true;
		}

		if(X==4)
		{
			B=false;
			if(R> C)
				swap(R,C);

			if(R==3 && C==4)
				B=true;
			if(R==4 && C==4)
				B=true;
		}

		if(B)
			cout<<"Case #"<<x+1<<": "<<"GABRIEL"<<endl;
		else
			cout<<"Case #"<<x+1<<": "<<"RICHARD"<<endl;

	}

	return 0;
}