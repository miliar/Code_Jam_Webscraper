#include<iostream.h>
#include<conio.h>
#include<string.h>
#include<stdlib.h>
#include<fstream.h>
void main()
{
	int cas,i,j,invite,shy,tot,han,sv;
	ifstream infile("input1.in");
	ofstream outfile("output1.out");
	char str[1001];
	infile>>cas;
	for(i=0;i<cas;i++)
	{ 
		tot=0;invite=0;
		infile>>shy;
		infile>>str;
		shy++;
		for(j=0;j<shy;j++)
		{
			sv=str[j]-48;
			cout<<sv<<" ";			
			if(j>tot)
			{
				han=j-tot;
				invite+=han;
				tot+=han;
			}
			tot+=sv;
		}	
		outfile<<"Case #"<<i+1<<": "<<invite<<endl;
	}
	getch();
}