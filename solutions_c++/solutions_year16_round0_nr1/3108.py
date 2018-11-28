#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <cstring>
using namespace std;


vector <int> past;
int hit[10];

int main(int argc, char* argv[])
{
	string input;
	fstream fin;
	fin.open(argv[1], ios::in);
	getline(fin, input);

	stringstream ss;
	int now_count;
	int counter = 0;
	bool end = false;
	int hit_count = 0;
	stringstream sss;
	string tos;
	while(getline(fin, input))
	{
		memset(hit, 0, sizeof(hit));
		++counter;
		ss<<input;
		ss>>now_count;
		ss.str("");
		ss.clear();
		end = false;
		hit_count = 0;
		int plus_base = now_count;
		past.clear();
		int trans;
		while(end==false)
		{
			hit_count = 0;
	//		cout<<now_count<<endl;
	//		for(int i = 0; i < 10; ++i)
	//			cout<<hit[i]<<" ";
	//		cout<<endl;
			if(find(past.begin(),past.end(),now_count) != past.end())
			{
				cout<<"Case #"<<counter<<": "<<"INSOMNIA"<<endl;
		//		cout<<now_count<<endl;
				end = true;
			}
			else{
				past.push_back(now_count);
				sss<<now_count;
				sss>>tos;
				sss.str("");
				sss.clear();
				for(int i = 0; i < tos.size(); ++i)
				{
					sss<<tos[i];
					sss>>trans;
					sss.str("");
					sss.clear();
		//			cout<<"trans"<<trans<<endl;
					hit[trans]++;
				}
				for(int i = 0; i < 10; ++i)
				{
					if(hit[i]!=0)
						++hit_count;
				}
				if(hit_count==10)
				{
					cout<<"Case #"<<counter<<": "<<now_count<<endl;
					end = true;
				}
				else
					now_count += plus_base;
			}
		}			
		
	}
	return 0;
}
