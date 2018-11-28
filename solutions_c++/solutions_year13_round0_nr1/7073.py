#include <iostream>
#include <fstream>

using namespace std;


int main()
{
	ifstream in("input.txt");
	ofstream out("output.txt");

	int n;
	in>>n;
	char temp[20];
	in.getline(temp,20);
	for(int i=1;i<=n;i++)
	{
		//system("pause");
		out<<"Case #"<<i<<": ";
		char arr[5][5];
		for(int j=0;j<4;j++)
		{
			in.getline(arr[j],20);
		//	out<<arr[j]<<endl;
		}
		//out<<endl;
		
		int rx[4]={0,0,0,0};
		int ro[4]={0,0,0,0};
		int cx[4]={0,0,0,0};
		int co[4]={0,0,0,0};
		int dot=0;
		int dix[2]={0,0};
		int dio[2]={0,0};
		for(int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{

				if(arr[j][k] == 'X' || arr[j][k]=='T')
				{
					rx[j]++;
					cx[k]++;
					if(j==k)
						dix[0]++;
					
					if(j+k == 3)
						dix[1]++;
				}
				if(arr[j][k] == 'O' || arr[j][k]=='T')
				{
					ro[j]++;
					co[k]++;
					if(j==k)
						dio[0]++;
					
					if(j+k == 3)
						dio[1]++;
				}
				if(arr[j][k] == '.')
				{
					dot++;
				}
			}
		}
		bool won=false;
		for(int i=0;i<4;i++)
		{
			if(rx[i]==4 || cx[i]==4 || dix[i/2]==4)
			{
				out<<"X won";
				won=true;
				break;
			}
		}
		for(int i=0;i<4 && !won;i++)
		{
			if(ro[i]==4 || co[i]==4 || dio[i/2]==4)
			{
				out<<"O won";
				won =true;
				break;
			}
		}
		if(!won){
		if(dot)
				out<<"Game has not completed";
		else
				out<<"Draw";
		}
		out<<endl;
		in.getline(temp,20);
	}

	system("pause");
	return 0;
}