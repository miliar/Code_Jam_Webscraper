#include <fstream>
#include <iostream>
using namespace std;

static char *ppsz_result[]=
{
	"NO",
	"YES",
};

static int lawn_mower(int *p_status,int height,int length)
{
	int result=1;
	int height_max=0;
	int total_size=length*height;

	for(int i=0;i<total_size;i++)
	{
		if(p_status[i]>height_max)
			height_max=p_status[i];
	}

	result=1;
	for(int i=0;i<total_size;i++)
	{
		if(p_status[i]<height_max)
		{
			int row=i/length;
			int colume=i-row*length;
			int colume_ok=1;
			int row_ok=1;
			for(int k=row*length;k<(row+1)*length;k++)
			{
				if(p_status[k]>p_status[i])
				{
					row_ok=0;
					break;
				}
			}
			for(int j=colume;j<=colume+(height-1)*length;j=j+length)
			{
				if(p_status[j]>p_status[i])
				{
					colume_ok=0;
					break;
				}
			}
			if(row_ok==0&&colume_ok==0)
			{
				result=0;
				break;
			}
		}
	}
	return result;
}

int main()
{
	ifstream fin("B-large.in");
	ofstream fout("result.out");

	int test_count=0;
	int length,height;
	int test[10000];
	fin>>test_count;
	for(int i=0;i<test_count;i++)
	{
		fin>>length>>height;
		for(int j=0;j<length*height;j++)
		{
			fin>>test[j];
		}
		fout<<"Case #"<<i+1<<": "<<ppsz_result[lawn_mower(test,length,height)]<<endl;
	}
	fin.close();
	fout.close();

	return 0;
}
