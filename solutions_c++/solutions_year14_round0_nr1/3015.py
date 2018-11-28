#include<iostream>
using namespace std;
int main(){
std::ios_base::sync_with_stdio(false);
int t;
cin>>t;
for(int k=1;k<=t;k++)
{
int ans1,ans2;
int array1[4][4],array2[4][4];
bool covered[17];
for(int i=0;i<17;i++)
covered[i]=false;
cin>>ans1;
for(int i=0;i<4;i++)
{for(int j=0;j<4;j++)
{
cin>>array1[i][j];
if(i==ans1-1)covered[array1[i][j]]=true;
}
}
cin>>ans2;
int count=0,fin;
for(int i=0;i<4;i++)
{
for(int j=0;j<4;j++)
{
cin>>array2[i][j];
if(ans2==i+1){if(covered[array2[i][j]]) {count++;fin=array2[i][j];}}
}
}
if(count==0)
cout<<"Case #"<<k<<": Volunteer cheated!\n";
else if (count ==1)
cout<<"Case #"<<k<<": "<<fin<<endl;
else
cout<<"Case #"<<k<<": Bad magician!\n";
}

return 0;
}
