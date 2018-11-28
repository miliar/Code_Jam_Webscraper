#include<iostream>
#include<fstream>
using namespace std;
int main()
{
	int T,i,j,l1,l2,temp,sum;
	int s[4][4];
	int L1[4];
	int L2[4];
	fstream fin("A-small-attempt3.in",ios::in);
	fstream fout("999.doc",ios::out);
	fin>>T;
	cout<<T<<endl;
	for(i=0;i<T;i++)
	{
	fin>>l1;
	cout<<l1<<endl;
	for(int p=0;p<4;p++)
	{
		for(int q=0;q<4;q++)
		{fin>>s[p][q];
	//	cout<<s[p][q]<<" ";
		}
	//	cout<<endl;
	}
	for(j=0;j<4;j++)
	{	L1[j]=s[l1-1][j];/*cout<<L1[j];*/}
//	cout<<endl;
	fin>>l2;
//	cout<<l2<<endl;
	for(int p1=0;p1<4;p1++)
	{
		for(int q1=0;q1<4;q1++)
		{fin>>s[p1][q1];
	/*cout<<s[p1][q1]<<" ";*/
		}	
	//cout<<endl;
	}
	for(j=0;j<4;j++)
	{L2[j]=s[l2-1][j];/*cout<<L2[j];*/}
	//cout<<endl;
	sum=0;
   for(int x=0;x<4;x++)
   {
	for(int y=0;y<4;y++)
	if(L1[x]==L2[y])
	{sum+=1;/*cout<<sum<<endl;cout<<sum<<endl;*/	temp=L1[x];/*cout<<temp<<endl;*/}
   }
if(sum==1)
fout<<"Case #"<<i+1<<": "<<temp<<"\n";
else{
	if(sum==0)
		fout<<"Case #"<<i+1<<": Volunteer cheated!"<<"\n";
	else
		fout<<"Case #"<<i+1<<": Bad magician!"<<"\n";
	}
}
	return 0;
}