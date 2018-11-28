#include <iostream>
#include <stdlib.h>
#include <string>
#include <algorithm>
#include <math.h>
#include <stdio.h>
using namespace std;
int q,w,e,n,m,m1,i,j,k=0,s=0;
	int res[10][10];
	int r[10][10];
	int t[11000];
int main()
{



//freopen("a-small-attempt8.in","rt",stdin);
//freopen ("a-small-attempt8.out","wt",stdout);

	cin>>n;
	for (q=1;q<=n;q++)
	{
		k=0;
		cin>>m;
	for (i=1;i<=4;i++)
	 {
	 	for (j=1;j<=4;j++)
		 {
		 	cin>>res[i][j];
	 	 }
	 }
	 cin>>m1;
	 	
	for (i=1;i<=4;i++)
	 {
	 	for (j=1;j<=4;j++)
		 {
		 	cin>>r[i][j];
	 	 }
	 }
	 
	 for (w=1;w<=4;w++)
	 {
	 	for (e=1;e<=4;e++)
		 {
		 	if (res[m][w]!=0 &&   res[m][w]==r[m1][e]) {s=res[m][w];res[m][w]=0;k++;}
	 	 }
	 }
	 
	 if (k==0 ){t[q]=-1;}
	 if (k==1) {t[q]=s;	 }
	 if (k>1) {t[q]=0;	 }
	 k=0;
	 
	}
	for (q=1;q<=n;q++)
	{
	if (t[q]>0) cout<<"Case #"<<q<<": "<<t[q]<<endl;
	if (t[q]==0) cout<<"Case #"<<q<<": Bad magician!"<<endl;
	if (t[q]==-1) cout<<"Case #"<<q<<": Volunteer cheated!"<<endl;
	}
	
	
	return 0;
}

