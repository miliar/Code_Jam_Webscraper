#include <iostream>
#include <fstream>
using namespace std;
int main()
{
ofstream output;
output.open("output.txt");
ifstream input;
input.open("input.txt");
int T;
input>>T;
for(int i=0;i<T;i++){
int row;
input>>row;
int a[4][4],b[4][4];
for(int j=0;j<4;j++)
    for(int k=0;k<4;k++)
{
input>>a[j][k];
}
int row2;
input>>row2;
for(int j=0;j<4;j++)
	for(int k=0;k<4;k++)
{
input>>b[j][k];
}
int correct=0;
int ans;
for(int j=0;j<4;j++)
{
for(int k=0;k<4;k++)
{
	if(a[row-1][j]==b[row2-1][k])
	{
	correct++;
	ans=a[row-1][j];
	}
}
}
cout<<"Case #"<<i+1<<": ";
if(correct==0)
cout<<"Volunteer cheated!";
else if(correct>1)
cout<<"Bad magician!";
else
cout<<ans;
cout<<endl;

}
input.close();
output.close();
}