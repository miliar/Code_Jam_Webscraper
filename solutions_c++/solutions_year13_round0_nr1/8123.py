#include<iostream>
#include<cstring>
#include<string>
#include<fstream>
#include<math.h>
using namespace std;
int main()
{
int i=0,n=80,t,l=0;
char line[1000],line1[1000],line2[1000],line3[1000],l3[1000],ans[100];
ofstream fout;
fout.open("main0.txt");
FILE *f=fopen("A-small-attempt2.in","r");
fgets(l3,80,f);
t=strlen(l3);
for(int k=(t-2);k>-1;k--)
{
        i=i+((l3[k]-48)*pow(10,l));
        l++;
}
t=0;
cout<<i;
for(l=0;l<i;l++)
{
	fgets(line,6,f);
	fgets(line1,6,f);
	fgets(line2,6,f);
	fgets(line3,6,f);
	fgets(ans,6,f);
	fout<<"Case #"<<l+1<<": ";

	if(line[t]=='O' || line[t]=='T')
	{
		if((line[t+1]=='O' || line[t+1]=='T') && (line[t+2]=='O' || line[t+2]=='T') && (line[t+3]=='O' || line[t+3]=='T'))
		{
			fout<<"O won"<<"\n";
			continue;
		}
		else if((line1[t]=='O' || line1[t]=='T') && (line2[t]=='O' || line2[t]=='T') && (line3[t]=='O' || line3[t]=='T'))
		{
			fout<<"O won"<<"\n";
			continue;
		}
		else if((line1[t+1]=='O' || line1[t+1]=='T') && (line2[t+2]=='O' || line2[t+2]=='T') && (line3[t+3]=='O' || line3[t+3]=='T'))
		{
			fout<<"O won"<<"\n";
			continue;
		}
	}
	 if(line1[t]=='O' || line1[t]=='T')
        {
                if((line1[t+1]=='O' || line1[t+1]=='T') && (line1[t+2]=='O' || line1[t+2]=='T') && (line1[t+3]=='O' || line1[t+3]=='T'))
                {
                        fout<<"O won"<<"\n";
                        continue;
                }
	}
	 if(line2[t]=='O' || line2[t]=='T')
        {
                if((line2[t+1]=='O' || line2[t+1]=='T') && (line2[t+2]=='O' || line2[t+2]=='T') && (line2[t+3]=='O' || line2[t+3]=='T'))
                {
                        fout<<"O won"<<"\n";
                        continue;
                }
	}
	 if(line3[t]=='O' || line3[t]=='T')
        {
                if((line3[t+1]=='O' || line3[t+1]=='T') && (line3[t+2]=='O' || line3[t+2]=='T') && (line3[t+3]=='O' || line3[t+3]=='T'))
                {
                        fout<<"O won"<<"\n";
                        continue;
                }
	}



	if(line[t+1]=='O' || line[t+1]=='T')
	{
		if((line1[t+1]=='O' || line1[t+1]=='T') && (line2[t+1]=='O' || line2[t+1]=='T') && (line3[t+1]=='O' || line3[t+1]=='T'))
		{
			fout<<"O won"<<"\n";
			continue;
		}
	}
	if(line[t+2]=='O' || line[t+2]=='T')
        {
                if((line1[t+2]=='O' || line1[t+2]=='T') && (line2[t+2]=='O' || line2[t+2]=='T') && (line3[t+2]=='O' || line3[t+2]=='T'))
                {
                        fout<<"O won"<<"/n";
                        continue;
                }
        }
	if(line[t+3]=='O' || line[t+3]=='T')
        {
                if((line1[t+3]=='O' || line1[t+3]=='T') && (line2[t+3]=='O' || line2[t+3]=='T') && (line3[t+3]=='O' || line3[t+3]=='T'))
                {
                        fout<<"O won"<<"\n";
                        continue;
                }
		else if((line3[t]=='O' || line3[t]=='T') && (line2[t+1]=='O' || line2[t+1]=='T') && (line1[t+2]=='O' || line1[t+2]=='T'))
                {
                        fout<<"O won"<<"\n";
                        continue;
                }

        }
	if(line[t]=='X' || line[t]=='T')
	{
		if((line[t+1]=='X' || line[t+1]=='T') && (line[t+2]=='X' || line[t+2]=='T') && (line[t+3]=='X' || line[t+3]=='T'))
		{
			fout<<"X won"<<"\n";
			continue;
		}
		else if((line1[t]=='X' || line1[t]=='T') && (line2[t]=='X' || line2[t]=='T') && (line3[t]=='X' || line3[t]=='T'))
		{
			fout<<"X won"<<"\n";
			continue;
		}
		else if((line1[t+1]=='X' || line1[t+1]=='T') && (line2[t+2]=='X' || line2[t+2]=='T') && (line3[t+3]=='X' || line3[t+3]=='T'))
		{
			fout<<"X won"<<"\n";
			continue;
		}
	}
	 if(line1[t]=='X' || line1[t]=='T')
        {
                if((line1[t+1]=='X' || line1[t+1]=='T') && (line1[t+2]=='X' || line1[t+2]=='T') && (line1[t+3]=='X' || line1[t+3]=='T'))
                {
                        fout<<"X won"<<"\n";
                        continue;
                }
	}
	 if(line2[t]=='X' || line2[t]=='T')
        {
                if((line2[t+1]=='X' || line2[t+1]=='T') && (line2[t+2]=='X' || line2[t+2]=='T') && (line2[t+3]=='X' || line2[t+3]=='T'))
                {
                        fout<<"X won"<<"\n";
                        continue;
                }
	}
	 if(line3[t]=='X' || line3[t]=='T')
        {
                if((line3[t+1]=='X' || line3[t+1]=='T') && (line3[t+2]=='X' || line3[t+2]=='T') && (line3[t+3]=='X' || line3[t+3]=='T'))
                {
                        fout<<"X won"<<"\n";
                        continue;
                }
	}



	if(line[t+1]=='X' || line[t+1]=='T')
	{
		if((line1[t+1]=='X' || line1[t+1]=='T') && (line2[t+1]=='X' || line2[t+1]=='T') && (line3[t+1]=='X' || line3[t+1]=='T'))
		{
			fout<<"X won"<<"\n";
			continue;
		}
	}
	if(line[t+2]=='X' || line[t+2]=='T')
        {
                if((line1[t+2]=='X' || line1[t+2]=='T') && (line2[t+2]=='X' || line2[t+2]=='T') && (line3[t+2]=='X' || line3[t+2]=='T'))
                {
                        fout<<"X won"<<"/n";
                        continue;
                }
        }
	if(line[t+3]=='X' || line[t+3]=='T')
        {
                if((line1[t+3]=='X' || line1[t+3]=='T') && (line2[t+3]=='X' || line2[t+3]=='T') && (line3[t+3]=='X' || line3[t+3]=='T'))
                {
                        fout<<"X won"<<"\n";
                        continue;
                }
		else if((line3[t]=='X' || line3[t]=='T') && (line2[t+1]=='X' || line2[t+1]=='T') && (line1[t+2]=='X' || line1[t+2]=='T'))
                {
                        fout<<"X won"<<"\n";
                        continue;
                }

        }
	for(int y=0;y<4;y++)
	{
		if(line[y]=='.' || line1[y]=='.' || line2[y]=='.' || line3[y]=='.')
		{
			fout<<"Game has not completed"<<"\n";
			break;
		}
		else
		{
			fout<<"Draw"<<"\n";
			break;
		}
	}
}
return 0;
}
