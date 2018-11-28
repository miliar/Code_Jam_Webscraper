#include<iostream>
#include<algorithm>
#include<cstdio>
#include<vector>
using namespace std;
vector<vector<int> > input;
int m,n;
bool checkRow(int a,int num)
{
int i;
for( i =0;i<n;i++)
{
if(input[a][i] > num)
 break;

}
if(i<n)
 return false;
return true;

}
bool checkCol(int a,int num)
{
int i;
for(i=0;i<m;i++)
{
if(input[i][a] > num)
  break;

}
if(i<m)
return false;
return true;
}
int main()
{
int test,t=1,a;
cin >> test;
while(t<=test)
{
cin >> m >> n;
input.clear();
for(int i =0;i<m;i++)
{
vector<int> temp;
for(int j=0;j<n;j++)
{
cin >> a;
temp.push_back(a);
}
input.push_back(temp);
}
int i;
for( i =0;i<m;i++)
{
int j;
for( j=0;j<n;j++)
{
if(!checkRow(i,input[i][j]) && !checkCol(j,input[i][j]))
  break;
}
if(j<n)
 {
  break; 

 }
}
cout <<"Case #"<<t<<": ";
if(i<m)
{
cout << "NO"<<endl;

}
else
cout << "YES"<<endl;
t++;
}
return 0;
}
