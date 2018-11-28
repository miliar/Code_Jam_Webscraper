#include <iostream>
#include <fstream>
#include <windows.h>

using std::ifstream; 
using std::ofstream;
using std::cout;





int main()
{
	int x,r1,r2,arr1[4][4],arr2[4][4],count=0,no=0;
	char mes1[51]="Bad magician!",mes2[51]="Volunteer cheated!";
	ifstream file;
	ofstream output;
    file.open("A-small-attempt3.in");
	output.open("output.txt");
    file>>x;
	for(int l=0;l<x;l++)
	   {
	     file>>r1;
		 cout<<"r1   "<<r1<<"\n";
		 
		 for(int i=0;i<=3;i++)
		 {
			 for(int j=0;j<=3;j++)
			 {
				
				 file>>arr1[i][j];
				 cout<<arr1[i][j]<<" ";
			 }
			 cout<<"\n";
		 }//Sleep(10000);
		 file>>r2;
		 cout<<"r2   "<<r2<<"\n";
		 
		 for(int i=0;i<=3;i++)
		 {
			 for(int j=0;j<=3;j++)
			 {
				 file>>arr2[i][j];
				 cout<<arr2[i][j]<<" ";
			 }cout<<"\n";
			 
		 }//Sleep(10000);
		 for(int i=0;i<=3;i++)
		 {
		 for(int j=0;j<=3;j++)
		 {
			 if(arr1[(r1-1)][i]==arr2[(r2-1)][j])
			 {
				 cout<<"r1  "<<r1<<"\t"<<"   r2  "<<r2<<"\n";
				 count++;
				 cout<<"Matching  are  "<<arr2[(r2-1)][j]<<"\t"<<arr1[(r1-1)][i]<<"   At  "<<i<<','<<r1-1<<'.'<<j<<','<<r2-1<<"\n";
			 }
		 }
			 }
	if(count==1)
	{
      for(int i=0;i<=3;i++)

	   {
		    for(int j=0;j<=3;j++)
			{
				if(arr1[(r1-1)][i]==arr2[(r2-1)][j])
			 {
				 no=arr1[r1-1][i];
			 }
			}
	  }
        output<<"Case #"<<(l+1)<<':'<<' '<<no<<"\n";
	  }
	else
		if(count>1)
		{
		output<<"Case #"<<(l+1)<<':'<<' '<<mes1<<"\n";
		}
	else
		if(count==0)
		{
		output<<"Case #"<<(l+1)<<':'<<' '<<mes2<<"\n";
		}
		count=0;
		no=0;
	}
	
	file.close();
	output.close();
	system("pause");

	return 0;
}