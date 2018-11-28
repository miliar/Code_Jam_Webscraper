#include<iostream>
#include<fstream>
using namespace std;

int main()
{	
	  ofstream op;
	  op.open ("output.txt");
	int T=1,totN=0,standN=0,sMax=0,y=0;
	char ch;
	int sArray[1005];
	cin>>T;
//	op<<"\nNo of Test Cases : "<<T<<"\n";
	for(int i=0;i<T;i++)
	{	totN=0;standN=0;y=0;sMax=0;
		cin>>sMax;
		for(int j=0;j<=sMax;j++)
		{	cin>>ch;
			sArray[j]=int(ch)-48;
			//op<<sArray[j];
			totN=totN+sArray[j];
		}
/*//		op<<sArray;
//		op<<totN<<standN;
op<<"\n****************************TEST CASE  ["<<i+1<<"]*********";
op<<"\n"<<sMax<<" \n";
	for(int j=0;j<=sMax;j++)
		{op<<sArray[j];
	}
op<<"\n****************************TEST CASE  ["<<i+1<<"]*********";
*/
		int x=i+1,y=0;
		for(int j=0;j<=sMax;j++)
		{	if(sArray[j]==0) 
				continue;
			if(j<=standN)
			{	standN = standN +sArray[j];
				continue;
			}
			else
			{	y=y+ (j-standN);
				standN = standN + y;
				standN = standN +sArray[j];
			}
		}
		op<<"\nCase #"<<x<<": "<<y;
	}
	  op.close();
	return(0);
}
