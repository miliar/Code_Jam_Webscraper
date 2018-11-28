#include <iostream>  
#include <algorithm>  
#include <cmath>  
#include <vector>  
#include <string>  
#include <ctime>
#include <iomanip>
using namespace std;  

int n,m,i,j,t,y,x,k,w,l,r,p,v,a[5][5],b[5][5],q;	

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>w;
	v=w;
	while(w--)
	{
		cin>>x;
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				cin>>a[i][j];
		cin>>y;
		for(i=1;i<=4;i++)
			for(j=1;j<=4;j++)
				cin>>b[i][j];
		for(i=1;i<=4;i++)
		{
			for(j=1;j<=4;j++)
			{
				if(a[x][i]==b[y][j])
				{
					k=a[x][i];
					q++;
				}
			}
		}
		if(q==1)
			cout<<"Case #"<<v-w<<": "<<k<<endl;
		if(q>1)
			cout<<"Case #"<<v-w<<": Bad magician!"<<endl;
		if(q==0)
			cout<<"Case #"<<v-w<<": Volunteer cheated!"<<endl;
		q=0;
	}
	return 0;
}





