#include<iostream>

using namespace std;

int print(int *a)
{
	for(int i=0;i<4;i++)
		cout<<a[i]<<" ";
	cout<<endl;
	
}

int main()
{
	int T;
	cin>>T;
	for(int w=1;w<=T;w++)
	{
		int ROcount[4]={0},RXcount[4]={0},COcount[4]={0},CXcount[4]={0},ODig=0,XDig=0,rev_ODig=0,rev_XDig=0;
		string s;
		bool emptyCell=false;
		for(int i=0;i<4;i++)
		{
			cin>>s;
			for(int j=0;j<4;j++)
				{
					if(s[j]=='X')
					{
						if(i==j)XDig++;
						else if(i+j==3) rev_XDig++;
						RXcount[i]++,CXcount[j]++;
					}
					else if(s[j]=='O')
					{
						if(i==j)ODig++;
						else if(i+j==3)rev_ODig++;
						ROcount[i]++,COcount[j]++;
					}
					else if(s[j]=='T')
					{
						if(i==j) XDig++,ODig++;
						else if(i+j==3) rev_XDig++,rev_ODig++;
						ROcount[i]++,RXcount[i]++,COcount[j]++,CXcount[j]++;
					}
					else
						emptyCell=true;
				}
		}
		int i=0;
		/*cout<<"Row X"<<endl;
			print(RXcount);
		cout<<"Row O\n";
			print(ROcount);
		cout<<"Colmn X\n";
			print(CXcount);
		cout<<"Colmn O\n";
			print(COcount);
		cout<<"DigX "<<XDig<<"  "<<"DigO "<<ODig<<" rev_XDig "<<rev_XDig<<" rev_ODig "<<rev_ODig<<endl;
		*/
		for(i=0;i<4;i++)
			{
			if(RXcount[i]==4 || CXcount[i]==4 || XDig==4 || rev_XDig==4)
				{cout<<"Case #"<<w<<": X won\n"; break;}
			if(ROcount[i]==4 || COcount[i]==4 || ODig==4 || rev_ODig==4)
				{cout<<"Case #"<<w<<": O won\n";break;}
			}
			
		if(i==4 && emptyCell==true)
			{
			cout<<"Case #"<<w<<": Game has not completed\n";
			}
		else if(i==4)
			{
			cout<<"Case #"<<w<<": Draw\n";
			}
	}
return 0;
}
