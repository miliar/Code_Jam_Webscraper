#include <iostream>
#include <vector>

using namespace std;

void skip(int);

int main()
{

int T,M1,M2;
vector<int> m1(4);
vector<int> m2(4);


cin>>T;
for(int k=0; k<T; k++)
{
cin>>M1;

	if(1==M1)		{for(int i=0; i<4; i++) cin>>m1[i]; skip(12);}
	else if(2==M1)	{skip(4);for(int i=0; i<4; i++) cin>>m1[i]; skip(8);}
	else if(3==M1)	{skip(8);for(int i=0; i<4; i++) cin>>m1[i]; skip(4);}
	else			{skip(12);for(int i=0; i<4; i++) cin>>m1[i];}

cin>>M2;

	if(1==M2)		{for(int i=0; i<4; i++) cin>>m2[i]; skip(12);}
	else if(2==M2)	{skip(4);for(int i=0; i<4; i++) cin>>m2[i]; skip(8);}
	else if(3==M2)	{skip(8);for(int i=0; i<4; i++) cin>>m2[i]; skip(4);}
	else			{skip(12);for(int i=0; i<4; i++) cin>>m2[i];}

	int match = 0;
	int count = 0;

	for(int i=0; i<4; i++)
		for(int j=0; j<4; j++)
			if(m1[i]==m2[j]) {count++; match = m1[i];}


	cout<<"Case #"<<k+1<<": ";
	if(count>1) cout<<"Bad magician!";
	else if(0==count) cout<<"Volunteer cheated!";
	else cout<<match;
	cout<<endl;


}


}

void skip(int x)
{
	int y;
	for(int i=0; i<x; i++)
	cin>>y;
}