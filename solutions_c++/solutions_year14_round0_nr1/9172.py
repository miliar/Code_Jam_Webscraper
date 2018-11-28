#include<iostream>
#include<vector>
using namespace std;
int main(){
int t;
cin>>t;
for(int i=0;i<t;i++)
{
vector<int> a1,a2;
int row1;
int row2;
cin>>row1;
for(int j=0;j<16;j++)
{
int c;
cin>>c;
	a1.push_back(c);
}
cin>>row2;
for(int j=0;j<16;j++)
{
int c;
cin>>c;
	a2.push_back(c);
}
int k=-1;
bool bad =false;
for(int j=0;j<4;j++)
{
	for(int arb=0;arb<4;arb++)
	{
		//cout<<a1[4*(row1-1)+j]<<a2[4*(row2-1)+arb]<<endl;
		if(a1[4*(row1-1)+j]==a2[4*(row2-1)+arb])
		{
			if(k!=-1) bad=true;
			k=a1[4*(row1-1)+j];
		}
	}
}
if(bad) cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
else if(k==-1) cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
else cout<<"Case #"<<i+1<<": "<<k<<endl;
}}
