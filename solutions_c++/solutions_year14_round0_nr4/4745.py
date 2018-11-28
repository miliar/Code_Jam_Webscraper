#include<iostream>
#include<fstream>
using namespace std;
void sort(float *arr,int N)
{
	for(int i=0;i<N-1;i++)
		for(int j = 0;j<N-1;j++)
		{
			if(arr[j]>arr[j+1])
			{
				float tmp = arr[j];
				arr[j]=arr[j+1];
				arr[j+1]=tmp;
			}
		}
}
int findMax(float num, float *arr,int N)
{
	for(int j = 0;j<N;j++)
		if(num<arr[j])
		{
			arr[j]=0.0;
			return 1;
		}
	return 0;
}
void findMin(float *arr, int N)
{
	for(int k=0;k<N&&arr[k]>0;k++)
	{
		arr[k]=0.0;
		return;
	}
}
int findMin1(float num, float *arr,int N)
{
	for(int j = 0;j<N;j++)
		if(num>arr[j])
		{
			arr[j]=1.0;
			return 1;
		}
	return 0;
}
int main()
{
	int t,N;
	ifstream fin;
	fin.open("C:\\Users\\DeepakG\\Desktop\\BatLife\\asmallattem.txt");
	ofstream fout;
	fout.open("C:\\Users\\DeepakG\\Desktop\\BatLife\\outattempt.txt");
	fin>>t;
	float *res = new float[(int)t];float *res1 = new float[(int)t];
	for(int i =0;i<t;i++)
	{
		fin>>N;
		float *naomi = new float[N];
		float *ken = new float[N];
		float *stone = new float[N];
		int start=1,end=0;
		int pints = 0;
		int ponts = 0;
		for(int k =0 ;k<N;k++){fin>>naomi[k];}for(int k =0 ;k<N;k++){fin>>ken[k];stone[k]=ken[k];}
		sort(naomi,N);sort(ken,N);sort(stone,N);
		
		for(int j = 0;j<N;j++)
		{
			if(findMin1(naomi[j],stone,N))
			{
				//findMax(ken,N);
				pints++;
			}

		}	



		res[i]=pints;



		for(int j = 0;j<N;j++)
		{
			if(!findMax(naomi[j],ken,N))
			{
				findMin(ken,N);
				ponts++;
			}

		}
		res1[i]=ponts;
	}

	for(int i=0;i<t;i++)
	{
		fout<<"Case #"<<i+1<<": "<<res[i]<<" "<<res1[i]<<"\n";
	}
	//system("pause");
	return 0;

}

