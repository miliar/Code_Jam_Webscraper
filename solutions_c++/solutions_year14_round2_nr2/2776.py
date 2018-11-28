#include<iostream>
#include<fstream>
using namespace std;
int main()
{
int test, a,b,k,d,i,j,count,m=1;
	cin>>test;
	ofstream fout;
fout.open("example.txt");
while(test--)
{	count=0;
	cin>>a>>b>>k;
	for(i=0;i<a;i++)
	for(j=0;j<b;j++)
	if((i&j)<k) count++;
	
	fout<<"Case #"<<m<<": "<<count<<endl;
	m++;
}
fout.close();
return 0;
}//main
