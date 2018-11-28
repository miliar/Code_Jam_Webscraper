#include <stdio.h>
#include <iostream>
#include <cstring>
#include <vector>
#include <utility>
#include <stdlib.h>
#include <algorithm>
#include <queue>
#include <functional>
#include <cstring>
#include <string> 
#include <queue>
#include <fstream>
#include <sstream>
#include <map>
#include <math.h>
#define outout freopen ("out.txt","w",stdout)
#define readread freopen("A-large.in", "r",stdin)

//#include <bits/stdc++.h>

using namespace std;

vector<bool> vis;
bool fin(long long n)
{
	for(int i=0;i<10;i++)
		if(!vis[i])
			return false;
	return true;
}
void fill(long long n)
{
	while(n>0)
	{
		vis[n%10]=true;
		n/=10;
	}
}
int main()
{
	ios_base::sync_with_stdio(false);
	cin.tie(0);
	readread;
	outout;
	unsigned long long n,t,ii,c=1;
	cin>>t;
	while(t--)
	{
		cin>>n;
		if(n==0)
		{
			cout<<"Case #"<<c++<<": INSOMNIA\n";
			continue;
		}
		vis=vector<bool>(10,false);
		for(ii=1; n<=ULLONG_MAX/ii && !fin(n*ii); ii++)
			fill(n*ii);
		
		cout<<"Case #"<<c++<<": "<<n*(ii-1)<<"\n";
	}

	return 0;
}

//#include <iostream>
////#include <bits/stdc++.h>
//using namespace std;
//
//int poli[102][102];
//int aux[102][102];
//int color[102][102];
//
//int fila,columna;
//
//void dfs(int y,int x,int col)
//{
//	color[y][x]=col;
//	if(y+1<fila && poli[y][x]==poli[y+1][x] && color[y+1][x]==-1)
//		dfs(y+1,x,col);
//	if(x+1<columna && poli[y][x]==poli[y][x+1] && color[y][x+1]==-1)
//		dfs(y,x+1,col);
//	if(x-1>=0 && poli[y][x]==poli[y][x-1] && color[y][x-1]==-1)
//		dfs(y,x-1,col);
//}
//
//int main()
//{
//	ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);
//	int res;
//	while(cin>>fila>>columna)
//	{
//		for(int i=0;i<fila;i++)
//			for(int e=0;e<columna;e++)
//			{
//				cin>>poli[i][e];
//				color[i][e]=-1;
//			}
//
//		res=5;
//
//		///////// CARAS HORIZONTALES
//
//		for(int i=0;i<fila;i++)
//			for(int e=0;e<columna-1;e++)
//			{
//				aux[i][e]=poli[i][e]-poli[i][e+1];
//				if(aux[i][e]!=0)
//					res++;
//			}
//		for(int e=0;e<columna-1;e++)
//			for(int i=0;i<fila-1;i++)
//				if(aux[i][e]>0 && aux[i+1][e]>0 && poli[i][e]>poli[i+1][e+1] && poli[i][e+1]<poli[i+1][e])
//					res--;
//				else if(aux[i][e]<0 && aux[i+1][e]<0 && poli[i][e]<poli[i+1][e+1] && poli[i+1][e]<poli[i][e+1])
//					res--;
//
//		///////////// CARAS VERTICALES
//
//		for(int i=0;i<fila-1;i++)
//			for(int e=0;e<columna;e++)
//			{
//				aux[i][e]=poli[i][e]-poli[i+1][e];
//				if(aux[i][e]!=0)
//					res++;
//			}
//
//		for(int i=0;i<fila-1;i++)
//			for(int e=0;e<columna-1;e++)
//				if(aux[i][e]>0 && aux[i][e+1]>0 && poli[i][e]>poli[i+1][e+1] && poli[i+1][e]<poli[i][e+1])
//					res--;
//				else if(aux[i][e]<0 && aux[i][e+1]<0 && poli[i][e]<poli[i+1][e+1] && poli[i][e+1]<poli[i+1][e])
//					res--;
//
//		
//		int col=0;
//		for(int i=0;i<fila;i++)
//			for(int e=0;e<columna;e++)
//				if(color[i][e]==-1)
//				{
//					dfs(i,e,col);
//					col++;
//				}
//
//		cout<<res+col<<endl;
//	
//
//	}
//	return 0;
//}