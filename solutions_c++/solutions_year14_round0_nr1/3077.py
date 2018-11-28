#include <iostream>
//#include <fstream>
/* run this program using the console pauser or add your own getch, system("pause") or input loop */
using namespace std;

int main(int argc, char *argv[]) {
	
	// ifstream cin("file.in");
    //ofstream cout("file.out");

int cnt,count=0,cntt=0;
int cat[4][4],sel1[4],sel2[4],in1,in2,op;
cin>>cnt;	
while(cnt--)
{
	cntt++;
	cout<<"Case #"<<cntt<<": ";
	cin>>in1;
	in1--;
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			cin>>cat[i][j];
		}
	}// taken input for first arrangement
	for(int i=0;i<4;i++)
	{
		sel1[i]=cat[in1][i];
	}
	cin>>in2;
	in2--;
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			cin>>cat[i][j];
		}
	}// taken input for first arrangement
	for(int i=0;i<4;i++)
	{
		sel2[i]=cat[in2][i];
	}
	count=0;
	for(int i=0;i<4;i++)
	{
		for(int j=0;j<4;j++)
		{
			if(sel1[i]==sel2[j])
			{
							count++;
				op=sel1[i];
			}
		}
		if(count>1)
			{
				cout<<"Bad magician!";
				break;
			}
	}
	if(count==1)
	{
		cout<<op;
	}
	if(count==0)
	{
		cout<<"Volunteer cheated!";
	}
	cout<<endl;
	
}	
	return 0;
}