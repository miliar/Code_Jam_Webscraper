#include<cstdio>
#include<iostream>
using namespace std;

int check(const char arr[])
{
	int sum[10];
	sum[0]=arr[0]+arr[1]+arr[2]+arr[3];
	sum[1]=arr[4]+arr[5]+arr[6]+arr[7];
	sum[2]=arr[8]+arr[9]+arr[10]+arr[11];
	sum[3]=arr[12]+arr[13]+arr[14]+arr[15];
	sum[4]=arr[0]+arr[5]+arr[10]+arr[15];
	sum[5]=arr[0]+arr[4]+arr[8]+arr[12];
	sum[6]=arr[1]+arr[5]+arr[9]+arr[13];
	sum[7]=arr[2]+arr[6]+arr[10]+arr[14];
	sum[8]=arr[3]+arr[7]+arr[11]+arr[15];
	sum[9]=arr[3]+arr[6]+arr[9]+arr[12];
	for (int i=0 ; i<10 ; i++)
	{
		if (sum[i]==352 || sum[i]==348)
		{
			return 1; // X WIN
		}
	}
	for (int i=0 ; i<10 ; i++)
	{
		if ( sum[i]==316 || sum[i]==321 )
		{
			return 2; // O WIN
		}
	}
	for (int i=0 ; i<10 ; i++)
	{
		if ( arr[0]!='.' && arr[1]!='.' && arr[2]!='.' && arr[3]!='.' && arr[4]!='.' && arr[5]!='.' && arr[6]!='.' && arr[7]!='.' &&
		arr[8]!='.' && arr[9]!='.' && arr[10]!='.' && arr[11]!='.' &&arr[12]!='.' &&arr[13]!='.' &&arr[14]!='.' &&arr[15])
		{
			return 3; // DRAW	
		}
		else
		{
			return 4; // NOT FINISHED
		}
	}

}
void main()
{
	freopen ("Ainput.in","r",stdin);
	freopen ("Aoutput.txt","w",stdout);
	int t;
	cin>>t;
	int* ptr=new int[t];
	char arr[16];
	for (int r=0 ; r<t ; r++)
	{
		scanf("\n%c%c%c%c\n%c%c%c%c\n%c%c%c%c\n%c%c%c%c"
			,&arr[0],&arr[1],&arr[2],&arr[3],&arr[4],&arr[5],&arr[6],&arr[7],&arr[8]
		,&arr[9],&arr[10],&arr[11],&arr[12],&arr[13],&arr[14],&arr[15]);
		ptr[r]=check(arr);
	}
	for (int r=0 ; r<t ; r++)
	{
		switch (ptr[r])
		{
		case 1:
			cout<<"Case #"<<r+1<<": X won"<<endl;
			break;
			
		case 2:
			cout<<"Case #"<<r+1<<": O won"<<endl;
			break;
			
		case 3:
			cout<<"Case #"<<r+1<<": Draw"<<endl;
			break;
			
		case 4:
			cout<<"Case #"<<r+1<<": Game has not completed"<<endl;
			break;
		}
	}
}