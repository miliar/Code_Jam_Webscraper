#include<iostream>
using namespace std;
int main()
{
int t;
cin>>t;
int **field;
int **design;

for(int p=0;p<t;p++)
{
	int n,m;
	cin>>m>>n;
	field=new int*[m];
	design=new int*[m];
	for(int i=0;i<m;i++)
		{
		field[i]=new int[n];
		design[i]=new int[n];
		for(int j=0;j<n;j++)
			{
			cin>>field[i][j];
			design[i][j]=100;
			}
			
		}


int rowmax[m];
int colmax[n];

	for(int i=0;i<m;i++)
		{
		rowmax[i]=field[i][0];
//		cout<<rowmax[i];
			for(int j=1;j<n;j++)
			{
//				cout<<"("<<i<<j<<")"<<field[i][j];
				if(rowmax[i]<field[i][j])
				{

					rowmax[i]=field[i][j];
		
				
				}
			}
		}
//	cout<<rowmax[0]<<endl;
	for(int i=0;i<m;i++)
		for(int j=0;j<n;j++)		
		{
			if(design[i][j]>rowmax[i])
				design[i][j]=rowmax[i];
		}

	
//	cout<<"-------------------"<<endl;

//	for(int i=0;i<m;i++)
//		{
//		for(int j=0;j<n;j++)
//			cout<<design[i][j];
//		cout<<endl;
//		}

//	cout<<"-------------------"<<endl;










	for(int i=0;i<n;i++)
		{
		colmax[i]=field[0][i];

			for(int j=1;j<m;j++)
			{
				if(colmax[i]<field[j][i])
				{
					colmax[i]=field[j][i];
		
				
				}
			}
		}
//	for(int i=0;i<n;i++)
//		cout<<colmax[i];
//	cout<<"----"<<endl;
	for(int i=0;i<n;i++)
		for(int j=0;j<m;j++)		
		{
			if(design[j][i]>colmax[i])
				design[j][i]=colmax[i];
		}
	

//	for(int i=0;i<m;i++)
//		{
//		for(int j=0;j<n;j++)
//			cout<<design[i][j];
//		cout<<endl;
//		}

	int correct=1;
	for(int i=0;i<m;i++)
		for(int j=0;j<n;j++)
		{
			if(field[i][j]!=design[i][j])
			{
				correct=0;			
				break;
			}
		}
	if(correct==1)
		cout<<"Case #"<<p+1<<": YES"<<endl;
	else
		cout<<"Case #"<<p+1<<": NO"<<endl;

}

return 0;
}
