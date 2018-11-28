#include <iostream>
#include <vector>
#include <string>
#include <fstream>
using namespace std;
int main(int argc, char const *argv[])
{
	int t,n;
	long num,min;
	string s;
	cin>>t;
	ofstream myfile;
    myfile.open ("output.txt");
	for (int i = 0; i < t; ++i)
	{
		num=0;min=0;
		cin>>n>>s;
		
		num+=static_cast<long>(s[0]-48);

		for (int j = 1; j < n+1; ++j)
		{
			if(num<j){
				min+=(j-num);
				num+=(j-num);
				//cout<<j<<"  "<<num<<endl;
			}
			num+=static_cast<long>(s[j]-48);
			//cout<<num<<endl;
		}
		myfile<<"Case #"<<i+1<<": "<<min<<endl;
	}
	return 0;
}