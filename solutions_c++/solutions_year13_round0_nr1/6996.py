#include<iostream>
#include<stdio.h>

using namespace std;

main(){
	freopen("A-large.in","r",stdin);
	freopen("myfile.txt","w",stdout);
	int line;
	char harf;
	char inputs[16];
	int puan=0;
	int puan1;
	int puan2;
	int max;
	int yer,i,j,k;
	int ikinokta=0;
	scanf("%d", &line);

	for(j=0;line>j;j++)
	{
		for(i=0;i<16;i++)
		{
			scanf("%c", &harf);
			inputs[i]=harf;
			if(harf=='\n')
				i--;
		}

			if((((inputs[0]=='X') || (inputs[0]=='T')) && ((inputs[1]=='X') || (inputs[1]=='T'))  && ((inputs[2]=='X') || (inputs[2]=='T')) && ((inputs[3]=='X') || (inputs[3]=='T'))) || (((inputs[4]=='X') || (inputs[4]=='T')) && ((inputs[5]=='X') || (inputs[5]=='T'))  && ((inputs[6]=='X') || (inputs[6]=='T')) && ((inputs[7]=='X') || (inputs[7]=='T')))|| (((inputs[8]=='X') || (inputs[8]=='T')) && ((inputs[9]=='X') || (inputs[9]=='T'))  && ((inputs[10]=='X') || (inputs[10]=='T')) && ((inputs[11]=='X') || (inputs[11]=='T')))|| (((inputs[12]=='X') || (inputs[12]=='T')) && ((inputs[13]=='X') || (inputs[13]=='T'))  && ((inputs[14]=='X') || (inputs[14]=='T')) && ((inputs[15]=='X') || (inputs[15]=='T'))) || (((inputs[0]=='X') || (inputs[0]=='T')) && ((inputs[4]=='X') || (inputs[4]=='T'))  && ((inputs[8]=='X') || (inputs[8]=='T')) && ((inputs[12]=='X') || (inputs[12]=='T'))) || (((inputs[1]=='X') || (inputs[1]=='T')) && ((inputs[5]=='X') || (inputs[5]=='T'))  && ((inputs[9]=='X') || (inputs[9]=='T')) && ((inputs[13]=='X') || (inputs[13]=='T')))|| (((inputs[2]=='X') || (inputs[2]=='T')) && ((inputs[6]=='X') || (inputs[6]=='T'))  && ((inputs[10]=='X') || (inputs[10]=='T')) && ((inputs[14]=='X') || (inputs[14]=='T')))|| (((inputs[3]=='X') || (inputs[3]=='T')) && ((inputs[7]=='X') || (inputs[7]=='T'))  && ((inputs[11]=='X') || (inputs[11]=='T')) && ((inputs[15]=='X') || (inputs[15]=='T')))  || (((inputs[0]=='X') || (inputs[0]=='T')) && ((inputs[5]=='X') || (inputs[5]=='T'))  && ((inputs[10]=='X') || (inputs[10]=='T')) && ((inputs[15]=='X') || (inputs[15]=='T'))) || (((inputs[3]=='X') || (inputs[3]=='T')) && ((inputs[6]=='X') || (inputs[6]=='T'))  && ((inputs[9]=='X') || (inputs[9]=='T')) && ((inputs[12]=='X') || (inputs[12]=='T'))))
			{
				if((j+1)==line)
				cout<<"Case #"<<j+1<<": X won";
				else
				cout<<"Case #"<<j+1<<": X won"<<endl;
			}

			else if((((inputs[0]=='O') || (inputs[0]=='T')) && ((inputs[1]=='O') || (inputs[1]=='T'))  && ((inputs[2]=='O') || (inputs[2]=='T')) && ((inputs[3]=='O') || (inputs[3]=='T'))) || (((inputs[4]=='O') || (inputs[4]=='T')) && ((inputs[5]=='O') || (inputs[5]=='T'))  && ((inputs[6]=='O') || (inputs[6]=='T')) && ((inputs[7]=='O') || (inputs[7]=='T')))|| (((inputs[8]=='O') || (inputs[8]=='T')) && ((inputs[9]=='O') || (inputs[9]=='T'))  && ((inputs[10]=='O') || (inputs[10]=='T')) && ((inputs[11]=='O') || (inputs[11]=='T')))|| (((inputs[12]=='O') || (inputs[12]=='T')) && ((inputs[13]=='O') || (inputs[13]=='T'))  && ((inputs[14]=='O') || (inputs[14]=='T')) && ((inputs[15]=='O') || (inputs[15]=='T'))) || (((inputs[0]=='O') || (inputs[0]=='T')) && ((inputs[4]=='O') || (inputs[4]=='T'))  && ((inputs[8]=='O') || (inputs[8]=='T')) && ((inputs[12]=='O') || (inputs[12]=='T'))) || (((inputs[1]=='O') || (inputs[1]=='T')) && ((inputs[5]=='O') || (inputs[5]=='T'))  && ((inputs[9]=='O') || (inputs[9]=='T')) && ((inputs[13]=='O') || (inputs[13]=='T')))|| (((inputs[2]=='O') || (inputs[2]=='T')) && ((inputs[6]=='O') || (inputs[6]=='T'))  && ((inputs[10]=='O') || (inputs[10]=='T')) && ((inputs[14]=='O') || (inputs[14]=='T')))|| (((inputs[3]=='O') || (inputs[3]=='T')) && ((inputs[7]=='O') || (inputs[7]=='T'))  && ((inputs[11]=='O') || (inputs[11]=='T')) && ((inputs[15]=='O') || (inputs[15]=='T')))  || (((inputs[0]=='O') || (inputs[0]=='T')) && ((inputs[5]=='O') || (inputs[5]=='T'))  && ((inputs[10]=='O') || (inputs[10]=='T')) && ((inputs[15]=='O') || (inputs[15]=='T'))) || (((inputs[3]=='O') || (inputs[3]=='T')) && ((inputs[6]=='O') || (inputs[6]=='T'))  && ((inputs[9]=='O') || (inputs[9]=='T')) && ((inputs[12]=='O') || (inputs[12]=='T'))))
			{
				if((j+1)==line)
				cout<<"Case #"<<j+1<<": O won";
				else
				cout<<"Case #"<<j+1<<": O won"<<endl;
			}

			else
			{
				for(i=0;i<16;i++)
				{
					if(inputs[i]=='.')
					{
						puan=1;
						if((j+1)==line)
						cout<<"Case #"<<j+1<<": Game has not completed";
						else
						cout<<"Case #"<<j+1<<": Game has not completed"<<endl;
						break;
					}
				}
				if(!puan)
					{
						if((j+1)==line)
						cout<<"Case #"<<j+1<<": Draw";
						else
						cout<<"Case #"<<j+1<<": Draw"<<endl;
					}
			}
			puan=0;
	}



return 0;
}
