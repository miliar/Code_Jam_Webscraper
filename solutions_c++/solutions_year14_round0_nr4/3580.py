#include <iostream>
#include <fstream>
using namespace std;


void sort(float* array1,int size)
{
	float temp;
	for(int i=0; i<size; i++)
	{
		for(int j=0; j<size-1; j++)
		{
			if(array1[j]>array1[j+1])
			{
				temp=array1[j];
				array1[j]=array1[j+1];
				array1[j+1]=temp;        
			}
		}         
	} 
}


int main()
{	bool flag;
	float knlast;
	int klast=0;
	float *na;
	float *kn;
	int total,left;
	int size,k,i,i1,i2,j=0,wins,wins2,ik;
	ifstream fin("D-large.in");
	ofstream fout("output.txt");
	fin>>size;
	for(k=0;k<size;k++)
	{
		ik=wins=wins2=i1=i2=0;
		flag=true;
		fin>>left;
		total=left;
		na=new float [left];
		kn = new float [left];


		for(i=0;i<total;i++)
			fin>>na[i];
		for(i=0;i<left;i++)
			fin>>kn[i];



	sort(na,total);
	sort(kn,total);


	for(i=0;i<total;i++)
	{
		while( na[i]>kn[ik])
		{
			if(ik==total)
				break;
			ik++;
			
			wins2++;
		}
		if(ik==total)
				break;
		ik++;
	}






		for(i=0;i<total;i++)
		{
			
			while(kn[i1]==0)
				i1++;
			while(na[i2]==0||na[i2]<kn[i1])
			{
				i2++;
				if(i2==total)
				{
					flag=false;
					break;
				}
			}
			if (flag==false)
				break;
			wins++;
			na[i2]=0;
			kn[i1]=0;

		}
		fout<<"Case #"<<k+1<<": "<<wins<<" "<<wins2<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}