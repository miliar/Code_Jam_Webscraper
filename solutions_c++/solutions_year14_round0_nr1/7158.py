#include<iostream>
using namespace std;
//x=row;y=col
int pos1[4][4],pos2[4][4],num,r1,r2;

void init()
{for(int x=0;x<4;x++) for(int y=0;y<4;y++)
	{pos1[x][y]=pos2[x][y]=0;} num=0;r1=r2=-1;}

void readarr(bool is1)
{if(is1) for(int x=0;x<4;x++) for(int y=0;y<4;y++) cin>>pos1[x][y];
else for(int x=0;x<4;x++) for(int y=0;y<4;y++) cin>>pos2[x][y];}

bool search(int no,int row)
{for(int y=0;y<4;y++) if(pos2[row][y]==no) return true;
return false;}

int process(int c)
{init();
cin>>r1;
readarr(true);
cin>>r2;
readarr(false);r1--;r2--;
int count=0,cno=0;
for(int y=0;y<4;y++)
{if(search(pos1[r1][y],r2)) {count++;cno=pos1[r1][y];}}

if(count==1) return cno;
else if(count==0) return -1;
else return 0;
}

int main()
{int test;cin>>test;
for(int c=1;c<=test;c++)
{int x=process(c);cout<<"Case #"<<c<<": ";
if(x>0) cout<<x<<'\n';
else if(x==0) cout<<"Bad magician!\n";
else cout<<"Volunteer cheated!\n";}}



