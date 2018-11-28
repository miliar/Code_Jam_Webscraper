#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int main()
{
	ifstream file1("A-small-attempt2.in");
	ofstream file2("output.txt");
	int t=0;
	file1>>t;
	string enter;
	getline(file1,enter);
	for(int i=1;i<=t;i++)
	{
		string arr;
		getline(file1, arr);
		int k=0,j=0, gen=1, flag=0,num=0, deno=0, store=0;

		while((int)arr[j]!=47)
		{	num=10*num + (arr[j]- 48);
		    j++;
		   
		}
		j++;
		while(j<arr.size())
			{
				deno=10*deno + (arr[j] - 48);
			 	j++;
			}
			store=deno;
		float n=(float)num/(float)deno;
		float m=n;
		while(deno>1)
			{if(deno%2==1)
		{
			file2<<"Case #"<<i<<": impossible\n";
			flag++;
			break;
		}
		deno= deno/2;
		
	}
		while((2*n-1)<0 && !flag)
		{
			gen++;
			n=2*n;
		}
		if(gen<=40 && !flag && (n-1)<=(float)(40-gen)/(float)deno)
			file2<<"Case #"<<i<<": "<<gen<<endl;
		if(gen>40 && !flag)
			file2<<"Case #"<<i<<": impossible\n";


}
	return 0;
}