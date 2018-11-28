#include<iostream>
using std::cout;
using std::cin;
int main()
{	int T=1,totN=0,standN=0,sMax=0,y=0;
	char ch;
	int sArray[1000];
	cin>>T;
//	cout<<"\nNo of Test Cases : "<<T<<"\n";
	for(int i=0;i<T;i++)
	{	totN=0;standN=0;y=0;sMax=0;
		cin>>sMax;
		for(int j=0;j<=sMax;j++)
		{	cin>>ch;
			sArray[j]=int(ch)-48;
			//cout<<sArray[j];
			totN=totN+sArray[j];
		}
/*//		cout<<sArray;
//		cout<<totN<<standN;
cout<<"\n****************************TEST CASE  ["<<i+1<<"]*********";
cout<<"\n"<<sMax<<" \n";
	for(int j=0;j<=sMax;j++)
		{cout<<sArray[j];
	}
cout<<"\n****************************TEST CASE  ["<<i+1<<"]*********";
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
		cout<<"\nCase #"<<x<<": "<<y;
	}
	return(0);
}
