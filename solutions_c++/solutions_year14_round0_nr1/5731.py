#include <iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;
int main()
{
freopen("in1.txt","r",stdin);
freopen("out1.txt","w",stdout);
int a[5][5],b[5][5],ans1,ans2,t,i,j,k,test;
vector<int> v,ans;
scanf("%d",&t);
for(test=1;test<=t;test++)
{
scanf("%d",&ans1);
ans1--;
v.clear();
ans.clear();
for(i=0;i<4;i++)
for(j=0;j<4;j++)
{
scanf("%d",&a[i][j]);

if(i==ans1)
v.push_back(a[i][j]);

}

scanf("%d",&ans2);
ans2--;
for(i=0;i<4;i++)
for(j=0;j<4;j++)
{
scanf("%d",&b[i][j]);
if(i==ans2)
{
for(k=0;k<v.size();k++)
{
if(v[k]==b[i][j])
ans.push_back(v[k]);

}
}

}
if(ans.size()==1)
cout<<"Case #"<<test<<": "<<ans[0]<<endl;
else if(ans.size()>1)
cout<<"Case #"<<test<<": "<<"Bad magician!"<<endl;
else
cout<<"Case #"<<test<<": "<<"Volunteer cheated!"<<endl;

}

return 0;
}
