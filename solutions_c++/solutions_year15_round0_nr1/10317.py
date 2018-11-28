#include<conio.h>
#include<iostream.h>
#include<fstream.h>
void main()
{
	int T,arr[1002];
	int k;
	int standing,invites;
	char ch;
	clrscr();
	ifstream fin("C:\\TC\\BIN\\GcodeJam\\2015\\A\\inps1.txt");
	ofstream fout("C:\\TC\\BIN\\GcodeJam\\2015\\A\\outs1.txt");
	cout<<"Google Code Jam 2014 Qualification A !"<<endl;
	fin>>T;
	cout<<"Testcases : "<<T<<endl<<endl;
	for(int i=1;i<=T;i++)
	{
		fout<<"Case #"<<i<<": ";
		standing=0;
		invites=0;
		fin>>k;
		cout<<k;
		fin.get(ch);
		cout<<ch;
		for(int j=0;j<=k;j++)
		{
			fin.get(ch);
			//cout<<ch;
			arr[j]=(int)ch-48;
			cout<<arr[j];
			if(j<=standing)
			{
				standing+=arr[j];
			}
			else
			{
			       if(arr[j]!=0)
			       {
					invites+=j-standing;
					standing+=invites;
					standing+=arr[j];
			       }
			}
		}
		cout<<"\tInvites = "<<invites<<endl;
		fout<<invites<<endl;
		/*if(i%10==0)
		getch();*/
	}
	fout.close();
	getch();
}