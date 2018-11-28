#include<iostream>
#include <string>
#include <cstdio>



using namespace std;

int main()
{

	freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);


	int T;
	cin>>T;

	for ( int i=1; i<=T; i++)
	{
		int X,R,C;
		cin>> X>>R>>C;
		if (X==1) cout<<"Case #"<<i<<": GABRIEL"<<endl;
		else if ( X==2)
		{
			if ( (R*C)%2==0) cout<< "Case #"<<i<<": GABRIEL"<<endl;
			else cout<<"Case #"<<i<<": RICHARD"<<endl;
		}

		else if ( X==3)
		{
			if ( R*C ==3 ) cout<<"Case #"<<i<<": RICHARD"<<endl;
		  else if ( (R*C)%3==0) cout<< "Case #"<<i<<": GABRIEL"<<endl;
			else cout<<"Case #"<<i<<": RICHARD"<<endl;

		}


		else if (X==4)
		{
			if ( R*C <4) cout<<"Case #"<<i<<": RICHARD"<<endl;
			else if ( R*C == 4 ) cout<<"Case #"<<i<<": RICHARD"<<endl;
			else if ( R*C == 6 ) cout<<"Case #"<<i<<": RICHARD"<<endl;
			else if ( R*C == 8 ) cout<<"Case #"<<i<<": RICHARD"<<endl;
			else if ( R*C == 9 ) cout<<"Case #"<<i<<": RICHARD"<<endl;
			else if ( R*C == 12 ) cout<<"Case #"<<i<<": GABRIEL"<<endl;
			else if ( R*C == 16 ) cout<<"Case #"<<i<<": GABRIEL"<<endl;

		}
		

	}
	
	return 0;
}