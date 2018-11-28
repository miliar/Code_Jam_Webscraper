#include <iostream>
#include <stdio.h>

using namespace std;


int main ()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);

	int T;
	cin>>T;
	char arr[4][4],brr[4][4],numofchars;

	for (int i=0;i<T;i++)
	{
		int flags=0,numofchars=0;
//		numofchars++;

		for (int a=0;a<4;a++)
			for (int b=0;b<4;b++)
			{
				cin >> arr[a][b];
				brr[a][b]=arr[a][b];

				if (arr[a][b]=='T')
					arr[a][b]='X';

				if (brr[a][b]=='T')
					brr[a][b]='O';

				if (arr[a][b]!='.')
					numofchars++;			
			}
///
		for (int a=0;a<4;a++)
		{
			if (arr[a][0]==arr[a][1] && arr[a][2]==arr[a][1] && arr[a][2]==arr[a][3] && arr[a][0]=='X'&&flags==0)
			{	cout<< "Case #"<<i+1<<": X won"<<'\n';	flags=1;}
		}		

		for (int a=0;a<4;a++)
		{
			if (arr[0][a]==arr[1][a] && arr[2][a]==arr[1][a] && arr[2][a]==arr[3][a] && arr[0][a]=='X'&&flags==0)
			{	cout<< "Case #"<<i+1<<": X won"<<'\n';	flags=1;}
		}		

		if (arr[0][3]==arr[1][2] && arr[2][1]==arr[1][2] && arr[2][1]==arr[3][0] && arr[3][0]=='X'&&flags==0)
		{		cout<< "Case #"<<i+1<<": X won"<<'\n';	flags=1;}

		if (arr[0][0]==arr[1][1] && arr[2][2]==arr[1][1] && arr[2][2]==arr[3][3] && arr[0][0]=='X'&&flags==0)
		{	cout<< "Case #"<<i+1<<": X won"<<'\n';		flags=1;}

///
		for (int a=0;a<4;a++)
		{
			if (brr[a][0]==brr[a][1] && brr[a][2]==brr[a][1] && brr[a][2]==brr[a][3] && brr[a][0]=='O'&&flags==0)
			{	cout<< "Case #"<<i+1<<": O won"<<'\n';	flags=1;}
		}		

		for (int a=0;a<4;a++)
		{
			if (brr[0][a]==brr[1][a] && brr[2][a]==brr[1][a] && brr[2][a]==brr[3][a] && brr[0][a]=='O'&&flags==0)
			{	cout<< "Case #"<<i+1<<": O won"<<'\n';	flags=1;}
		}		

		if (brr[0][3]==brr[1][2] && brr[2][1]==brr[1][2] && brr[2][1]==brr[3][0] && brr[3][0]=='O'&&flags==0)
		{	cout<< "Case #"<<i+1<<": O won"<<'\n';	flags=1;}

		if (brr[0][0]==brr[1][1] && brr[2][2]==brr[1][1] && brr[2][2]==brr[3][3] && brr[0][0]=='O'&&flags==0)
		{	cout<< "Case #"<<i+1<<": O won"<<'\n';	flags=1;}


/*for (int h=0;h<4;h++)
{
	for (int g=0;g<4;g++)
		cout<<arr[h][g];
	cout<<'\n';
}*/

		if (flags==0&&numofchars<16)
			cout<<"Case #"<<i+1<<": Game has not completed"<<'\n';
		if (flags==0&&numofchars==16)
			cout<<"Case #"<<i+1<<": Draw"<<'\n';				

	}


	return 0;
}
