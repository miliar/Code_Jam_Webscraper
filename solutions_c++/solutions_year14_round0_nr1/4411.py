#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

void run()
{
	int a,b;
	int fst[16]={0}, snd[16]={0};
	int tmp;
	cin>>a;
	for(int i=1;i<=4;i++)
	{
		for(int j=0;j<4;j++)
		{
			cin>>tmp;
			if(i==a)
			{
				fst[tmp-1]=1;
			}
		}
	}
	cin>>b;
	for(int i=1;i<=4;i++)
	{
		for(int j=0;j<4;j++)
		{
			cin>>tmp;
			if(i==b)
			{
				snd[tmp-1]=1;
			}
		}
	}

	int cmn = 0;
	int fstCmn;
	for(int i=0;i<16;i++)
	{
		if(fst[i]==1 && snd[i]==1)
		{
			cmn++;
			fstCmn = i+1;
		}
	}

	if(cmn == 0)
		cout<<"Volunteer cheated!\n";
	else if(cmn==1)
		cout<<fstCmn<<endl;
	else
		cout<<"Bad magician!\n";		
}

int main()
{
	string input_name = "A-small-attempt0 (1).in";
	string output_name = "output.txt";

	freopen(input_name.c_str(),"r",stdin);
	freopen(output_name.c_str(),"w",stdout);

	int test;
	cin>>test;
	for(int i = 1;i<=test;i++)
	{
		cout<<"Case #"<<i<<": ";
		run();
	}
	return 0;
}