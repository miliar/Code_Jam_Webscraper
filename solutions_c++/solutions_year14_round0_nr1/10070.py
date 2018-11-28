#include<iostream>
#include<fstream>
using namespace std;
ifstream filein("A-small-attempt0.in");
ofstream fileout("output.in");
int main()
{
	int cases, choice1,choice2,a,b,c,d,ans=0,count=0;
	bool flag1=false, flag2= false;
	int _1st[4][4];
	int _2nd[4][4];
	filein>>cases;

   for(int i=0; i<cases; i++)  
   {
   	filein>>choice1;
   	for(int j=0;j<4;j++) 
   	{
   	for(int m=0;m<4;m++)
   	{
   		filein>>_1st[j][m];
   	}
   }
   	a=_1st[choice1-1][0];
   	b=_1st[choice1-1][1];
   	c=_1st[choice1-1][2];
   	d=_1st[choice1-1][3];
   	filein>>choice2;
   	for(int it=0;it<4;it++) 
   	{
   	for(int ml=0;ml<4;ml++)
   	{
   		filein>>_2nd[it][ml];
   	}
   }
   	if((a==_2nd[choice2-1][0]) || (a==_2nd[choice2-1][1]) || (a==_2nd[choice2-1][2]) || (a==_2nd[choice2-1][3]))
   	{
   	ans= a;
   	count++;
   }
   	if((b==_2nd[choice2-1][0]) || (b==_2nd[choice2-1][1]) || (b==_2nd[choice2-1][2]) || (b==_2nd[choice2-1][3]))
   	{
   	ans= b;
   	count++;
   }
   	if((c==_2nd[choice2-1][0]) || (c==_2nd[choice2-1][1]) || (c==_2nd[choice2-1][2]) || (c==_2nd[choice2-1][3]))
   	{
   	ans= c;
   	count++;
   }
   	if((d==_2nd[choice2-1][0]) || (d==_2nd[choice2-1][1]) || (d==_2nd[choice2-1][2]) || (d==_2nd[choice2-1][3]))
   	{
   	ans= d;
   	count++;
   }
   	if(count==1)
   	fileout<<"Case #"<<i+1<<": "<<ans<<endl;
   	else if(count>1)
   	fileout<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
    else
    fileout<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
   	count=0;
   	flag1=false;
   }
	return 0;
}
