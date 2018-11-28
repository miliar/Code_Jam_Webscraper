# include <iostream>

using namespace std;


void shorting (double *arr,int size)
{
	double temp;
	int i,j;
	for(i=0;i<size;i++)
	{	for(j=0;j<size;j++)
		{
			if(arr[i]<arr[j])
			{
				temp=arr[i];
				arr[i]=arr[j];
				arr[j]=temp;
			}
		}
	}
}

void shorting1 (double *arr,int size)
{
	double temp;
	int i,j;
	for(i=0;i<size;i++)
	{	for(j=0;j<size;j++)
		{
			if(arr[i]>arr[j])
			{
				temp=arr[i];
				arr[i]=arr[j];
				arr[j]=temp;
			}
		}
	}
}


int main ()
{
	int N,T,itr,i,j,win1,win2,value;
	double mass1[1000];
	double mass2[1000];
	cin>>T;
	for(itr=1;itr<=T;itr++)
	{
		win1=0;
		win2=0;
		cin>>N;
		value=N;
		for(int a=0;a<N;a++)
			cin>>mass1[a];
		for(int a=0;a<N;a++)
			cin>>mass2[a];
		
		shorting(mass1,N);
		shorting(mass2,N);
		j=0;
		for(i=0;i<N;i++)
		{
			for(;j<N;j++)
			{
				if(mass1[i] <  mass2[j])
				{
					win1++;
					j++;
					break;
				}
			}
		}

		shorting1(mass1,N);
		shorting1(mass2,N);
		j=0;
		for(i=0;i<value;i++)
		{
			for(;j<N;j++)
			{
				if(mass1[i] >  mass2[j])
				{
					win2++;
					j++;
					break;
				}
				else
				{
					value--;
				}
			}
		}
		cout<<"Case #"<<itr<<": "<<win2<<" "<<N-win1<<endl;
	
	}

	return 0;

}