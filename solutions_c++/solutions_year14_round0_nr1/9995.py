#include<iostream>
#include<fstream>
#include<string>
#include<string.h>
#include<conio.h>
using namespace std;
ifstream fin("A-small-attempt2.in");
ofstream fout("magic.in");
int main()
{
	int ca, c1,c2,a,b,c,d,ans=0,count=0;
	bool flag1=false, flag2= false;
	int array[4][4];
	int array2[4][4];
	fin>>ca;

//	fout<<ca;
   for(int i=0; i<ca; i++)  //in case
   {
   	fin>>c1;
  // 	cout<<"c1 "<<c1<<endl;
   	for(int j=0;j<4;j++)   //in getting inside
   	{
   	for(int m=0;m<4;m++)
   	{
   		fin>>array[j][m];
//		   cout<<" "<<array[j][m];
   	}
  // 	cout<<endl;
   }
 //  cout<<"........."<<endl;
   	a=array[c1-1][0];
   //	cout<<"a  "<<a<<endl;
   	b=array[c1-1][1];
   //	cout<<"b  "<<b<<endl;
   	c=array[c1-1][2];
   	d=array[c1-1][3];
   	fin>>c2;
   //	cout<<"c2 "<<c2<<endl;
   	for(int jk=0;jk<4;jk++)   //in getting inside
   	{
   	for(int ml=0;ml<4;ml++)
   	{
   		fin>>array2[jk][ml];
   //		cout<<" "<<array2[jk][ml];
   	}
   //	cout<<endl;
   }
   	
       
   		
       	
  // 	cout<<"a2  "<<array2[c2-1][0]<<endl;
  // 	cout<<"b2  "<<array2[c2-1][1]<<endl;
   	if((a==array2[c2-1][0]) || (a==array2[c2-1][1]) || (a==array2[c2-1][2]) || (a==array2[c2-1][3]))
   	{
   	ans= a;
   	count++;
   }
   	if((b==array2[c2-1][0]) || (b==array2[c2-1][1]) || (b==array2[c2-1][2]) || (b==array2[c2-1][3]))
   	{
   	ans= b;
   	count++;
   }
   	if((c==array2[c2-1][0]) || (c==array2[c2-1][1]) || (c==array2[c2-1][2]) || (c==array2[c2-1][3]))
   	{
   	ans= c;
   	count++;
   }
   	if((d==array2[c2-1][0]) || (d==array2[c2-1][1]) || (d==array2[c2-1][2]) || (d==array2[c2-1][3]))
   	{
   	ans= d;
   	count++;
   }
   	if(count==1)
   	fout<<"Case #"<<i+1<<": "<<ans<<endl;
   	else if(count>1)
   	fout<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
    else
    fout<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
   
  // 	cout<<"..................................."<<endl;
  // 	getch();
   	count=0;
   	flag1=false;
   }
	return 0;
}
