#include <iostream> 
#include <string>
#include <list>
#include <sstream> 
#include <vector>

using namespace std;
void main(){
	int N;
	string str;
	bool is_inserted;
	list<char> v_str;
	cin >> N;
	for (int i=0; i < N; i++)
	{
		cin >> str;
		v_str.clear();
		for(int j=0; j < str.size(); j++)
		{
			//cout<<str[j];
			if(v_str.size() == 0)
			{
				v_str.push_back(str[0]);
				continue;
			}
			is_inserted = false;
			for(list<char>::iterator it=v_str.begin(); it != v_str.end(); it++)
			{				
				if((int)str[j] < (int)*it)
				{
					v_str.push_back(str[j]);
					is_inserted = true;
					break;
				}				
			}
			if(!is_inserted)
				v_str.push_front(str[j]);
		}
		cout<<"Case #"<<i+1<<": ";
		for(list<char>::iterator it=v_str.begin(); it != v_str.end(); it++)
		{	
			cout<<*it;
		}
		cout<<endl;
	}
}