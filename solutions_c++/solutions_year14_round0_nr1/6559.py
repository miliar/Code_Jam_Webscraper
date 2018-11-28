#include<iostream>

using namespace std;

int main()
{
int T,arr[4][4],noc,rowno,i,j,res[4],ri,a=0;
cin>>T;
while(T--)
{
	a++;
noc=0;
cin>>rowno;
for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
{
cin>>arr[i][j];
}
}

ri=0;
for(i=0;i<4;i++)
{
res[ri++]=arr[rowno-1][i];
}

cin>>rowno;
for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
{
cin>>arr[i][j];
}
}
int ans=-1;
for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
{
if(res[j]==arr[rowno-1][i])
{
noc++; ans=res[j];
}

}
}
cout<<"Case #"<<a<<": ";
if(noc==1)
{
cout<<ans<<endl;
}
else if(noc==0)
	cout<<"Volunteer cheated!"<<endl;
else
	cout<<"Bad magician!"<<endl;
}


return 0;
}