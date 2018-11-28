#include<iostream>
using namespace std;
int main()
{
	int Tcases;
	int N,M;
	int i,j,temp;
	int ** area;
	int ** temparea;
	cin>>Tcases;
	temp=Tcases;
	for(Tcases; Tcases>0;Tcases--)
	{
		if(temp - Tcases != 0)
			cout << endl;
		int* max;
		int result =0;
		cin>>N>>M;
		max = new int[N];
		area = new int *[N];
		temparea = new int*[N];
		for(i=0; i <N; i++)
		{
			area[i] = new int[M];
			for(j=0; j<M;j++)
			{
				cin>>area[i][j];
			}
		}
		for(i=0;i<N;i++)
		{
			max[i] = 0;
			temparea[i]= new int[M];
			for(j=0;j<M;j++)
			{
				if (area[i][j]>max[i])
				max[i] = area[i][j];
			}
			for(j=0;j<M;j++)
			{
				temparea[i][j] = max[i];
			}
		}
		for(j=0;j<M;j++)
		{
			max[j]=0;
			for(i=0;i<N;i++)
			{
				if(area[i][j]>max[j])
				max[j]=area[i][j];
			}
			for(i=0;i<N;i++)
			{
				if(temparea[i][j]>max[j])
				temparea[i][j]= max[j];
			}
		}
	/*	for(int i=0; i <N; i++)
		{
			for(int j=0; j<M;j++)
			{
				cout<<temparea[i][j];
			}
			cout<<endl;
		}*/
		for( i=0; i <N; i++)
		{
			for(j=0; j<M;j++)
			{
				if(area[i][j]-temparea[i][j] !=0)
				{
					result = 1;
					i=N;
					break;
				}
			}
		}
//		delete max;
//		delete area;
		if(result==1)
		cout<< "Case #"	<<temp-Tcases + 1<<": NO";
		else
		cout<< "Case #"	<<temp-Tcases + 1<<": YES";
	}
	return 0;
}
