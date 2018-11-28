#include <iostream>
#include <fstream>
using namespace std;

int main() {
	ifstream in("input.txt");
	ofstream out("output.txt");
	int t,a1,a2,m1[4][4],m2[4][4],cnt,res;
	in>>t;
	for(int i=0;i<t;i++)
	{
		cnt=0;
		res=0;
		in>>a1;
		for(int j=0;j<4;j++)
		for(int k=0;k<4;k++)
		in>>m1[j][k];
		in>>a2;
		for(int j=0;j<4;j++)
		for(int k=0;k<4;k++)
		in>>m2[j][k];
		for(int j=0;j<4;j++)
		for(int k=0;k<4;k++)
		{
			if(m1[a1-1][j]==m2[a2-1][k])
			{
				cnt++;
				res=m1[a1-1][j];
			}

		}
		if(cnt==1)
		out<<"Case #"<<i+1<<": "<<res<<endl;
		else
		if(cnt==0)
		out<<"Case #"<<i+1<<": "<<"Volunteer cheated!"<<endl;
		else
		out<<"Case #"<<i+1<<": "<<"Bad magician!"<<endl;
		//in.close();
		//out.close();


	}
	return 0;


}
