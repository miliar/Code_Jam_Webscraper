#include<iostream>
#include<stdlib.h>
#include<fstream>

using namespace std;

int main()
{
	int i,j,k,l;
	int T,a[4][4];
	long long P,Q;
	long long *sw,*ou,temp,*swt,*flip,flag,pow;
	char c;
	ifstream ip("A-small-attempt2.in");;
	ofstream op("output1.txt");;
	ip>>T;
	long long power[51];
	power[0]=1;
	for(i=1;i<=50;i++)
		power[i]=power[i-1]*2;
	//cout<<T;
	for(l=1;l<=T;l++)
	{
		ip>>P>>c>>Q;
		for(i=0;i<=10;i++)
			if(Q==power[i])
				break;	
		op<<"Case #"<<l<<": ";
		if(i!=11)
		{
			for(j=0;j<=i;j++)
			{
				if(P*2>=Q)
					break;
				else 
					P=P*2;
			}
			op<<j+1<<"\n";
		}		
		else
			op<<"impossible\n";
	}
	return 0;
}
