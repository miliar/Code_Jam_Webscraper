#include<iostream>
#include<fstream>
using namespace std;
int main(){
fstream fileIN("A-small-attempt1.in",ios::in);
fstream fileOUT("A-small-attempt1.out",ios::out);
char ch='!';
int x=0,y=0,i=0,j=1,s=0,t=0;
while(1)
	{fileIN.get(ch);
	if(ch=='\n')
		break;
	i=i*10+(ch-48);
	}
while(j<=i){
	fileIN.get(ch);
	if(ch!=' ')
		x=(ch-48);
	s=0,t=-1,y=0;
	while(1)
		{
		fileIN.get(ch);
		if(ch!=' '){
		if(ch=='\n')
			break;
		t++;
		if(ch!='0')	{
			if(s<t)
				{y=y+(t-s);
				s=s+(t-s);
				}

		s=s+(int)(ch-48);
				}		
		}
}fileOUT<<"Case #"<<j<<": "<<y<<"\n";
j++;}
fileIN.close();
fileOUT.close();
return 0;
}
