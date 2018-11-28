#include<iostream>
#include<algorithm>
#include<fstream>
using namespace std;
int deal(int * first,int * second)
{
	int cnt=0;
	int tmp;
	for(int i=0;i<4;i++)
		for(int j=0;j<4;j++)
			if(first[i]==second[j])
			{
				tmp=first[i];
				cnt++;
			}
	if(cnt==0)
		return -1;
	if(cnt==1)
		return tmp;
	else
		return 0;
}



int main()
{
	int a[4][4];
	fstream in("A-small-attempt4.in");
	fstream out("ans.out");
	int T;
	in>>T;
	for(int kcase=1;kcase<=T;kcase++)
	{
		int choose;
		in>>choose;
		int tmp1[4],tmp2[4];
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				in>>a[i][j];
		for(int i=0;i<4;i++)
			tmp1[i]=a[choose-1][i];
		in>>choose;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				in>>a[i][j];
		for(int i=0;i<4;i++)
			tmp2[i]=a[choose-1][i];
		int ans=deal(tmp1,tmp2);
		if(ans==0)
			{
				out<<"Case #"<<kcase<<": "<<"Bad magician!"<<endl;
		}
		if(ans==-1)
		{
			out<<"Case #"<<kcase<<": "<<"Volunteer cheated!"<<endl;
		}

		if(ans>=1)
			{
				out<<"Case #"<<kcase<<": "<<ans<<endl;
		}
	}
	return 0;
}
