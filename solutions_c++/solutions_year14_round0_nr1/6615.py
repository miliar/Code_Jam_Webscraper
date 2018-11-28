#include<iostream>
#include<fstream>
using namespace std;
int main()
{
int t,a1[4][4],a2[4][4],ans1,ans2,i,j,flag1=0,flag2=0,flag3=0,flag4=0,m=1;
ofstream fout;
fout.open("example.txt");
cin>>t;
while(t--)
{	flag1=0,flag2=0,flag3=0,flag4=0;
	cin>>ans1;
	for(i=0;i<4;i++)
	for(j=0;j<4;j++)
	cin>>a1[i][j];
	cin>>ans2;
	for(i=0;i<4;i++)
	for(j=0;j<4;j++)cin>>a2[i][j];	
fout<<"Case #"<<m<<": ";
m++;
	for(j=0;j<4;j++)
	  { if(a1[ans1-1][0]==a2[ans2-1][j]) flag1=a1[ans1-1][0];
	    if(a1[ans1-1][1]==a2[ans2-1][j]) flag2=a1[ans1-1][1];
	    
	    if(a1[ans1-1][2]==a2[ans2-1][j]) flag3=a1[ans1-1][2];
	    
	    if(a1[ans1-1][3]==a2[ans2-1][j]) flag4=a1[ans1-1][3];
	    
	}
if((flag1==0) && (flag2==0) && (flag3==0) && (flag4==0))fout<<"Volunteer cheated!"<<endl;
else if((flag1 && flag2) || (flag1 && flag3) ||(flag1 && flag4) || (flag2&&flag3)||(flag2&&flag4)||(flag3&&flag4))
fout<<"Bad magician!"<<endl;

else {
if(flag1)fout<<flag1<<endl;
else if(flag2)fout<<flag2<<endl;
else if(flag3)fout<<flag3<<endl;
else if(flag4)fout<<flag4<<endl;
}

}
fout.close();
return 0;
}


