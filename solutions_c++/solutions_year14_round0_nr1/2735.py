
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <map>
#include <cstring>
#include <fstream>
using namespace std;

//https://code.google.com/codejam/contest/351101/dashboard#s=p0

int main()
{

    freopen("A-small-attempt0.in","r",stdin);
    freopen("out1.out","w",stdout);
int arr1[4][4];
int arr2[4][4] ;
int cs=1 ;
int t,ans1,ans2 ;
cin>>t ;
while(t--)
{
cin>>ans1 ;
for(int i=0;i<4;i++)
for(int j=0;j<4;j++)
cin>>arr1[i][j] ;

cin>>ans2 ;
for(int i=0;i<4;i++)
for(int j=0;j<4;j++)
cin>>arr2[i][j] ;

int num,isct=0;

for(int i=0;i<4;i++)
for(int j=0;j<4;j++)
if(arr1[ans1-1][i]==arr2[ans2-1][j])
{
num=arr1[ans1-1][i] ;
isct++ ;
}
cout<<"Case #"<<cs<<": ";
if(isct==0)
cout<<"Volunteer cheated!"<<endl;
if(isct>1)
cout<<"Bad magician!"<<endl ;
if(isct==1)
cout<<num<<endl ;
cs++ ;
}
return 0;
}
