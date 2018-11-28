#include<iostream>
#include<string>
#include<cstring>
#include<cstdio>
#include<queue>
using namespace std;
string solveGame()
{
    int n,m;
    string yes="YES",no="NO";
    int matrix[128][128];
	bool rows[128],columns[128];

	queue<pair<int,int> > ones;
    scanf("%d%d",&n,&m);
for(int i=1;i<=max(n,m);i++)
{
  rows[i]=false;
  columns[i]=false;
}
    for(int i=1;i<=n;i++)
        for(int j=1;j<=m;j++)
            {
               scanf("%d",&matrix[i][j]);
			   if(matrix[i][j]==1)
                ones.push(make_pair(i,j));
            }
   for(int i=1;i<=n;i++)
	   for(int j=1;j<=m;j++)
	   {
		   if(matrix[i][j]!=1) {rows[i]=true; break;}
	   }

     for(int j=1;j<=m;j++)
	 for(int i=1;i<=n;i++)
	   {
		   if(matrix[i][j]!=1) {columns[j]=true; break;}
	   }
	   pair<int,int> el;
/*
for(int i=1;i<=n;i++)
cout<<rows[i]<<" ";
cout<<endl;
for(int i=1;i<=m;i++)
cout<<columns[i]<<" ";
cout<<endl;
*/

	   while(!ones.empty())
	   {
		   el=ones.front();
		   ones.pop();
		  // cout<<el.first<<" "<<el.second<<endl;
		   if(rows[el.first]==true&&columns[el.second]==true)
		   {
			   return no;
		   }
	   }
return yes;
}

int main()
{
    int n;
  scanf("%d",&n);
  for(int i=1;i<=n;i++)
    {
      cout<<"Case #"<<i<<": "<<solveGame()<<endl;
    }
return 0;
}
