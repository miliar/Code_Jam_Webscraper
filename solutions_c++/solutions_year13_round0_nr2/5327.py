#include<iostream>

#include<vector>

using namespace std;



int main()
{
	int num;
	cin>>num;
	int n,m;
	int data[100][100];
	int *j;
	int *i;;
	for(int k=0;k<num;k++)
	{
		cin>>n>>m;
		for(int p=0;p<n;p++)
		{
			for(int q=0;q<m;q++)
			{
				cin>>data[p][q];

			}
		}
		i=new int[n];
		j=new int[m];
		
		for(int p=0;p<n;p++)
		{
			i[p]=0;
			for(int z=0;z<m;z++)
			{
				if(data[p][z]>i[p])
					i[p]=data[p][z];




			}
		}


		for(int q=0;q<m;q++)
		{
			j[q]=0;
			for(int z=0;z<n;z++)
			{
				if(data[z][q]>j[q])
					j[q]=data[z][q];




			}
		}

		for(int p=0;p<n;p++)
		{
			for(int q=0;q<m;q++)
			{
				int min=j[q];
				if(i[p]<min)
					min=i[p];
				if(data[p][q]!=min)
					goto no;
			}
		}
	
		cout<<"Case #"<<k+1<<": YES"<<endl;
		goto end;
no:
		
		cout<<"Case #"<<k+1<<": NO"<<endl;



end:

		delete i;
		delete j;
		
	}





}



