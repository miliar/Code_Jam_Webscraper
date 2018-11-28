#include<iostream>
#include<malloc.h>
using namespace std;

int main()
{
	int t,a,b,a1[4][4],b1[4][4],c[4],d[4];
	cin>>t;
	int* res = (int *) calloc (sizeof(int),t);
	int* r = (int *) calloc (sizeof(int),t);
	for(int i=0;i<t;i++)
	{
		cin>>a;
		int q=0;
		for (int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				cin>>a1[j][k];
				if (j+1==a)
				{
					c[q]=a1[j][k];
					q++;
				}
			}
		}
		cin>>b;
		q=0;
		for (int j=0;j<4;j++)
		{
			for(int k=0;k<4;k++)
			{
				cin>>b1[j][k];
				if (j+1==b)
				{
					d[q]=b1[j][k];
					q++;
				}
			}
		}
		//cin>>a1;
		for(int m=0;m<4;m++)
		{
			for(int n=0;n<4;n++)
			{
				if(c[m]==d[n])
				{
				res[i]++;
				r[i]=c[m];
				break;
				}
			}
		}
	}
	
for(int i=0;i<t;i++)
{
	if(res[i]==1)
		cout<<"Case #"<<i+1<<": "<<r[i]<<endl;
	else if (res[i]==0)
		cout<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
	else
		cout<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
}

}
