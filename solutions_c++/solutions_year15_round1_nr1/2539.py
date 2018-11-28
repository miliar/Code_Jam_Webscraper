#include<iostream>
#include<fstream>
#include<cstring>
using namespace std;
int main()
{
	 int t,n,m[10000],i,r,r1,co=0,co1=0,co2=0;
	 ifstream fin;
	fin.open("A-large.in");
	 ofstream fout;
	fout.open("output.txt");
	 fin>>t;
	 while(t--)
	 {
	 	co++;
	 	co1=0;co2=0;
	 	fin>>n;
	 	for(i=0;i<n;i++)
	 	{
	 		fin>>m[i];
		 }
			r=0;
		 for(i=1;i<n;i++)
		 {
		 	r1=m[i-1]-m[i];
		 	if(r1>r)
		 	r=r1;
		 	if(m[i]<m[i-1])
		 	{
		 		co1+=m[i-1]-m[i];
			 }
		 }
		// cout<<"r="<<r<<endl;
		 for(i=0;i<n-1;i++)
		 {
		 	if(m[i]<=r)
		 	{
		 		co2+=m[i];
			 }
			 else
			 {
			 	co2+=r;
			 }
		 }
		 	fout<<"Case #"<<co<<": "<<co1<<" "<<co2<<endl;
		
	 }
}
