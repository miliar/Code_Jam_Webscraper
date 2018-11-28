#include <iostream>
#include <string>
#include <fstream>
#include <stack>
#include <vector>
#include <algorithm>
using namespace std;

vector <string>toreverse;
vector <char> s1;
int main(int argc, char* argv[])
{
	string input;
	fstream fin;
	fin.open(argv[1], ios::in);
	getline(fin, input);
	
	bool end = false;
	int smile = 0;
	int flit = 0;
	int last = 0;
	int counter = 0;
	while(getline(fin, input))
	{
		++counter;
		flit = 0;
		last= 0;
		bool pitch = false;
		end = false;
//		reverse(input.begin(), input.end());
//		for(int i = 0; i < input.size(); ++i)
//			s1.push(input[i]);
		while(end==false)
		{
			smile = 0;
			pitch = false;
			for(int i = 0; i < input.size(); ++i)
			{
				//cout<<"inputi"<<input[i]<<" "<<endl;
				if(input[i]=='+')
					smile++;
				if(input[0]!=input[i] && pitch==false)
				{
					last = i - 1;
					pitch = true;
				}
				if(pitch==false)
					last = input.size()-1;	
			}
//			cout<<"counter: "<<counter<<", last: "<<last<<", smile:"<<smile<<endl;
	//		for(int i = 0; i < input.size(); ++i)
	//			cout<<input[i]<<" ";
	//		cout<<endl;
			if(smile==input.size())
				end = true;
			else
			{	
				for(int i = 0; i <=last; ++i)
				{
					if(input[i]=='+')
					{
						input[i]='-';
					}
					else if(input[i]=='-')
					{
				//		cout<<"before: "<<input[i]<<" ";
						input[i]='+';
				//		cout<<"after: "<<input[i]<<" "<<endl;
					}
					//cout<<"input0"<<input[0]<<endl;
				}
				flit++;
				reverse(input.begin(), input.begin()+last+1);
			}
		}
		cout<<"Case #"<<counter<<": "<<flit<<endl;
	}
	return 0;
}
