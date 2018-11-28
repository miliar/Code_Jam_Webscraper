 
#include<set>
#include<string>
#include<vector>
#include<algorithm>
#include<math.h>
#include<map>
#include<cctype>
#include<iterator>
#include<fstream>
using namespace std; 
int main()
{ 
	 std::fstream mydata("D:\\A-small-attempt0.in", std::ios_base::in);
	 ofstream myfile ("Output.txt");
	int n,m;
	mydata>>n;
	for( m=1 ; m<=n ; m++)
	{

	int row=0;
	int k=0,val=0,i=0,j=0;
	int ko[8];

	mydata>>row;
	int arr[4][4]={0};
for( i=0 ; i<4 ;  i++)
{
for( j=0 ; j<4 ; j++)
{
	mydata>>arr[i][j];
	
	if(i+1==row)
	{
	ko[j]=arr[i][j];
	}
}
}



mydata>>row;
for( i=0 ; i<4 ;  i++)
{
for( j=0 ; j<4 ; j++)
{
	mydata>>arr[i][j];
	
	if(i+1==row)
	{
	ko[j+4]=arr[i][j];
	}
}
}

sort(ko,ko+8);

for(int i=0 ; i<7; i++)
{
	if(ko[i]==ko[i+1]){k++;val=ko[i];}
}
if(k==1)myfile<<"Case #"<<m<<": "<<val;
else if(k==0)myfile<<"Case #"<<m<<": Volunteer cheated!";
else myfile<<"Case #"<<m<<": Bad magician!";
myfile<<"\n";
}
}


