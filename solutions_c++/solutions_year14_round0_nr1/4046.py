#include<iostream>
#include<fstream>
using namespace std;


int main ()
{
	ifstream ifile;
	ifile.open("A-small-attempt0.in");
	ofstream ofile;
	ofile.open("output.txt");

	int total;
	const int size = 4;
	ifile>>total;

	int arr[size] , arr2[size], dummy[size], pointed=0;
	char arry[size+1];
	bool save; 
	for(int a=0 ; a<total ; a++)
	{
		for(int k= 0 ;k<2; k++)
		{
			ifile>>pointed;
			save = false;
			for(int i=0 ; i<size ; i++)
			{
				
				for(int j=0 ; j<size ; j++)
				{
					if(save) ifile>>dummy[j];
					else if(k==0)
						ifile>>arr[j];
					else if(k==1)
						ifile>>arr2[j];
 				}
				if(i==pointed-1) save = true;
			}
		}



		bool flag=false , once=false;
		int no;

		for(int i=0 ; i<size ; i++)
		{
			for(int k=0 ; k<size ; k++)
			{
				if(arr[k]==arr2[i])
				{
					if(!flag)
					{
						flag= once= true;
						no =arr[k];
					}
					else{ once = false;  break; }

				}
			}
			
			
		}
		if(once)
			{
				ofile<<"Case #"<<a+1<<": "<<no<<endl;

			}
		if(!flag)
		{
			ofile<<"Case #"<<a+1<<": Volunteer cheated!"<<endl;
		}
		if(!once && flag)
		ofile<<"Case #"<<a+1<<": Bad magician!"<<endl;
	}

	ofile.close();
	ifile.close();
	return 0;
}