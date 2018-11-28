#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
int t  , flag , a , b , ar[4][4] , br[4][4] , ans;
cin>>t;

for(int i=1;i<=t;i++)
{

cin>>a;

for(int j=0;j<4;j++)
{
for(int k=0;k<4;k++)
{
	cin>>ar[j][k];
}
}

cin>>b;

for(int j=0;j<4;j++)
{
for(int k=0;k<4;k++)
{
	cin>>br[j][k];
}
}

flag = 0;
for(int l=0;l<4;l++)
{
	 
for(int k = 0 ; k<4 ; k++)

{if(ar[a-1][l] == br[b-1][k])
{ans = ar[a-1][l];
flag++;
}
}
}

if(flag==1)
cout<<"Case #"<<i<<": "<<ans<<endl;

if(flag == 0 )
cout<<"Case #"<<i<<": "<<"Volunteer cheated!"<<endl;

if(flag>1)
cout<<"Case #"<<i<<": "<<"Bad magician!"<<endl;

}

return 0;
}
