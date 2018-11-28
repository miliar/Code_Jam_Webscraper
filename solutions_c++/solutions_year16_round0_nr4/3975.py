#include<iostream>
#include<fstream>
using namespace std;
int main(){
	ofstream output("output.txt");
	ifstream input("input.txt");
int t;int c,k, s;
input>>t>>k>>c>>s;
for(int i=1;i<=t;i++)
{
	output<<"case #"<<i<<": ";
	for(int g=1;g<=k;g++)
		output<<g<<" ";
	output<<endl;
input>>k>>c>>s;
}
input.close();
output.close();
}