#include<iostream>
#include<fstream>

using namespace std;

int main()
{
	int arrangement1[5][5];
	int arrangement2[5][5];
	int answer1, answer2, i, j;
	fstream f;
	f.open("magic_trick.output", ios::out);
	int match, matchingcard;
	int T;
	int casenumber=1;
	cin>>T;
	while(T--)
	{
		match=0;
		matchingcard=0;
		cin>>answer1;
		for(i=1; i<=4; i++)
		{
			for(j=1; j<=4; j++)
			{
				cin>>arrangement1[i][j];
			}
		}
		cin>>answer2;
		for(i=1; i<=4; i++)
		{
			for(j=1; j<=4; j++)
			{
				cin>>arrangement2[i][j];
			}
		}
		for(i=1; i<=4; i++)
		{
			for(j=1; j<=4; j++)
			{
				if(arrangement1[answer1][i]==arrangement2[answer2][j])
				{
					match++;
					matchingcard=arrangement1[answer1][i];
				}
			}
		}
		f<<"Case #"<<casenumber<<": ";
		if(match==1)
		{
			f<<matchingcard<<endl;
		}
		else if(match>1)
		{
			f<<"Bad magician!"<<endl;
		}
		else
		{
			f<<"Volunteer cheated!"<<endl;
		}
		casenumber++;
	}
	return 0;
}
