/*
Believe you can and you are halfway there.-Divyansh Sharma
*/
#include<iostream>
#include<vector>
#include<algorithm>
#include<cstring>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<functional>
#include<vector>
#include<stack>
#include<set>
#include<fstream>
#include<map>
#include<queue>
#include<deque>
using namespace std;
int main()
{
    ofstream fo;
    fo.open("output.txt");
 short int t,var=1;
 cin>>t;
while(var<=t)
{
short int ans1,ans2,i,j,a1[4][4],a2[4][4],ans,ct=0;
cin>>ans1;
for(i=0;i<4;i++)
    for(j=0;j<4;j++)
     cin>>a1[i][j];
cin>>ans2;
for(i=0;i<4;i++)
    for(j=0;j<4;j++)
     cin>>a2[i][j];
for(i=0;i<4;i++)
{
 for(j=0;j<4;j++)
 {
  if(a1[ans1-1][i]==a2[ans2-1][j])
   {ans=a1[ans1-1][i];
    ct++;
   }
 }
}
if(ct==0)
    fo<<"Case #"<<var<<": Volunteer cheated!"<<endl;
else if(ct==1)
    fo<<"Case #"<<var<<": "<<ans<<endl;
else if(ct>1)
    fo<<"Case #"<<var<<": Bad magician!"<<endl;
    var++;
}
fo.close();
return 0;
}
