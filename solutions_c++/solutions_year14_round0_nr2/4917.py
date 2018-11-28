#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	float t,C,F,X;
	float R=2.0;
	float time,time1;
	ifstream fin;
	fin.open("C:\\Users\\DeepakG\\Desktop\\BatLife\\asmallattem.txt");
	ofstream fout;
	fout.open("C:\\Users\\DeepakG\\Desktop\\BatLife\\outattempt.txt");
	fin>>t;
	float *res = new float[(int)t];
	for(int i =0;i<t;i++)
	{
		fin>>C>>F>>X;
		time = X/R;
		for(int j=1;;j++)
		{
			time1=0;
			for(int k =0 ; k<j;k++)
			{
				time1+=(C/(R+(k*F)));
			}
			time1+=(X/(R+j*F));
			if(time1>time)break;
			time=time1;
		}
		
		res[i]=time;
		
	}

	fout<<fixed;
	fout.precision(7);
	for(int i=0;i<t;i++)
	{
		fout<<"Case #"<<i+1<<": "<<res[i]<<"\n";
	}
	//system("pause");
	return 0;

}