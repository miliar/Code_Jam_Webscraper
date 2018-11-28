#include <fstream>
#include <iostream>
using namespace std;


int main()
{
	fstream file_in,file_out;
	file_in.open("A-small-attempt0.in",ios::in);
	file_out.open("output.txt",ios::out);

	int n;
	file_in>>n;
	for (int case_num = 0; case_num < n; case_num++)
	{
		file_out<<"Case #"<<case_num+1<<": ";
		int q1,q2;
        int array1[16],array2[16];
		file_in>>q1;
		for (int i = 0;i<16;i++)
		{
			file_in>>array1[i];
		}
		file_in>>q2;
		for (int i = 0;i<16;i++)
		{
			file_in>>array2[i];
		}
        int result_col = -1;
		int isfind = 0;
		for (int i=0;i<4;i++)
		{
			int temp =array1[(q1-1)*4+i];
			for (int j=0;j<4;j++)
			{
				if (array2[(q2-1)*4+j] == temp)
				{
					result_col = i;
					isfind++;
				}
			}
		}
		if (isfind > 1)
		{
			file_out<<"Bad magician!"<<endl;
		}
		else if (isfind == 0)
		{
			file_out<<"Volunteer cheated!"<<endl;
		}
		else
		{
			file_out<<array1[(q1-1)*4+result_col]<<endl;
		}

	}
	
	return 0;
}


