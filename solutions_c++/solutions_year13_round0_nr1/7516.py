#include <iostream>
#include <fstream>
#include <string>

using namespace std;

string check(char t[])
{
	string ans;
	//win either one
	if((t[0]=='X'||t[0]=='T')&&(t[1]=='X'||t[1]=='T')&&(t[2]=='X'||t[2]=='T')&&(t[3]=='X'||t[3]=='T'))
	{ans="X won";}
	else if((t[0]=='O'||t[0]=='T')&&(t[1]=='O'||t[1]=='T')&&(t[2]=='O'||t[2]=='T')&&(t[3]=='O'||t[3]=='T'))
	{ans="O won";}
	else if((t[4]=='X'||t[4]=='T')&&(t[5]=='X'||t[5]=='T')&&(t[6]=='X'||t[6]=='T')&&(t[7]=='X'||t[7]=='T'))
	{ans="X won";}
	else if((t[4]=='O'||t[4]=='T')&&(t[5]=='O'||t[5]=='T')&&(t[6]=='O'||t[6]=='T')&&(t[7]=='O'||t[7]=='T'))
	{ans="O won";}
	else if((t[8]=='X'||t[8]=='T')&&(t[9]=='X'||t[9]=='T')&&(t[10]=='X'||t[10]=='T')&&(t[11]=='X'||t[11]=='T'))
	{ans="X won";}
	else if((t[8]=='O'||t[8]=='T')&&(t[9]=='O'||t[9]=='T')&&(t[10]=='O'||t[10]=='T')&&(t[11]=='O'||t[11]=='T'))
	{ans="O won";}
	else if((t[12]=='X'||t[12]=='T')&&(t[13]=='X'||t[13]=='T')&&(t[14]=='X'||t[14]=='T')&&(t[15]=='X'||t[15]=='T'))
	{ans="X won";}
	else if((t[12]=='O'||t[12]=='T')&&(t[13]=='O'||t[13]=='T')&&(t[14]=='O'||t[14]=='T')&&(t[15]=='O'||t[15]=='T'))
	{ans="O won";}
	else if((t[0]=='X'||t[0]=='T')&&(t[4]=='X'||t[4]=='T')&&(t[8]=='X'||t[8]=='T')&&(t[12]=='X'||t[12]=='T'))
	{ans="X won";}
	else if((t[0]=='O'||t[0]=='T')&&(t[4]=='O'||t[4]=='T')&&(t[8]=='O'||t[8]=='T')&&(t[12]=='O'||t[12]=='T'))
	{ans="O won";}
	else if((t[1]=='X'||t[1]=='T')&&(t[5]=='X'||t[5]=='T')&&(t[9]=='X'||t[9]=='T')&&(t[13]=='X'||t[13]=='T'))
	{ans="X won";}
	else if((t[1]=='O'||t[1]=='T')&&(t[5]=='O'||t[5]=='T')&&(t[9]=='O'||t[9]=='T')&&(t[13]=='O'||t[13]=='T'))
	{ans="O won";}
	else if((t[2]=='X'||t[2]=='T')&&(t[6]=='X'||t[6]=='T')&&(t[10]=='X'||t[10]=='T')&&(t[14]=='X'||t[14]=='T'))
	{ans="X won";}
	else if((t[2]=='O'||t[2]=='T')&&(t[6]=='O'||t[6]=='T')&&(t[10]=='O'||t[10]=='T')&&(t[14]=='O'||t[14]=='T'))
	{ans="O won";}
	else if((t[3]=='X'||t[3]=='T')&&(t[7]=='X'||t[7]=='T')&&(t[11]=='X'||t[11]=='T')&&(t[15]=='X'||t[15]=='T'))
	{ans="X won";}
	else if((t[3]=='O'||t[3]=='T')&&(t[7]=='O'||t[7]=='T')&&(t[11]=='O'||t[11]=='T')&&(t[15]=='O'||t[15]=='T'))
	{ans="O won";}
	else if((t[0]=='X'||t[0]=='T')&&(t[5]=='X'||t[5]=='T')&&(t[10]=='X'||t[10]=='T')&&(t[15]=='X'||t[15]=='T'))
	{ans="X won";}
	else if((t[0]=='O'||t[0]=='T')&&(t[5]=='O'||t[5]=='T')&&(t[10]=='O'||t[10]=='T')&&(t[15]=='O'||t[15]=='T'))
	{ans="O won";}
	else if((t[12]=='X'||t[12]=='T')&&(t[9]=='X'||t[9]=='T')&&(t[6]=='X'||t[6]=='T')&&(t[3]=='X'||t[3]=='T'))
	{ans="X won";}
	else if((t[12]=='O'||t[12]=='T')&&(t[9]=='O'||t[9]=='T')&&(t[6]=='O'||t[6]=='T')&&(t[3]=='O'||t[3]=='T'))
	{ans="O won";}
	else
	{
		for(int z=0;z<16;z++)
		{
			//not complete
			if(t[z]=='.')
			{ans="Game has not completed";break;}
			//draw
			else
			{
				ans="Draw";
			}
		}
	}
	return ans;
}

void main()
{
	string a,in,answer;
	char tick[16]={NULL}, temp[5]={NULL};
	int num=NULL;
	fstream input;
	fstream oput;
	input.open("A-large.in",ios::in);
	oput.open("outputfile.txt",ios::out);
	getline(input,a);
	num=stoi(a);
	//cout<<num<<endl;
	for(int i=0, x=0, y=0, count; i<num; i++)
	{
		count=0;
		for(int b=0;b<16;b++){tick[b]==NULL;}
		x=0;
		while(x<4)
		{
			y=0;
			in.clear();
			getline(input,in);
			strcpy(temp,in.c_str());
			while(y<4)
			{
				tick[count]=temp[y];
				y++;
				//if(tick[count]=='T'){tick[count]='X';}
				//cout<<tick[count]<<"("<<count<<")";
				count++;
			}
			//cout<<endl;
			x++;
		}
		//for(int b=0;b<16;b++){cout<<tick[b];}
		answer=check(tick);
		oput<<"Case #"<<i+1<<": "<<answer<<endl;
		cout<<"Case #"<<i+1<<": "<<answer<<endl;
		//system("pause");
		getline(input,in);
	}
	input.close();
	oput.close();
}