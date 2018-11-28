#include <iostream>
#include <fstream>
#include <math.h>

using namespace std;
int main()
{
	ifstream in("input.txt");
	ofstream out("out.txt");
	
	int n;
	in>>n;
	for(int j=1;j<=n;j++)
	{
		out<<"Case #"<<j<<": ";
		int start,end;
		in>>start>>end;
		int count=0;
		for(int i=start;i<=end;i++)
		{
			double d_sqrt = sqrt((double)i);
			int i_sqrt = d_sqrt;
			if ( d_sqrt == i_sqrt )
			{
				char temp[20],temp1[20];
				sprintf(temp,"%d",i);
				strcpy(temp1,temp);
				strrev(temp1);
				if( strcmp(temp,temp1) == 0 )
				{
					char temp2[20],temp3[20];
					sprintf(temp2,"%d",i_sqrt);
					strcpy(temp3,temp2);
					strrev(temp3);
					if( strcmp(temp2,temp3) == 0 )
						count++;
				}
					
			}
		}
		out<<count<<endl;
	}
	system("pause");
	return 0;
}
