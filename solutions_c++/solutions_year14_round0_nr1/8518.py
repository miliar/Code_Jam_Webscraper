#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	
int testcase  , flog , abc , xyz , array[4][4] , brray[4][4] , sol;
cin>>testcase;

for(int x=1;x<=testcase;x++)
{

cin>>abc;

for(int y=0;y<4;y++)
{
for(int z=0;z<4;z++)
{
	cin>>array[y][z];
}
}

cin>>xyz;

for(int y=0;y<4;y++)
{
for(int z=0;z<4;z++)
{
	cin>>brray[y][z];
}
}

flog = 0;
for(int y=0;y<4;y++)
{
	 
for(int z = 0 ; z<4 ; z++)

{if(array[abc-1][y] == brray[xyz-1][z])
{sol = array[abc-1][y];
flog++;
}
}
}

if(flog==1)
cout<<"Case #"<<x<<": "<<sol<<endl;

if(flog == 0 )
cout<<"Case #"<<x<<": "<<"Volunteer cheated!"<<endl;

if(flog>1)
cout<<"Case #"<<x<<": "<<"Bad magician!"<<endl;

}

return 0;
}
