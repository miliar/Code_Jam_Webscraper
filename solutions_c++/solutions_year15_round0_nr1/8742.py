#include <iostream>
#include <string>
#include <cstring>
#include <cstdlib>
#include <vector>

using namespace std;

typedef struct req
{
	int num;
	int s_val;
	req():num(0), s_val(0){}	
}req;

req cal_req( const vector<int> &s_list, const int &s_max)
{
	req required;
	int num = 0;
	for(int i=0; i < s_list.size(); i++)
	{
		if(i <= num) 
			num += s_list[i];
			
		else if(i > num)
		{
			required.num++;
			required.s_val = (i>0)?i-1:i;
			num++;
			num += s_list[i];
		}
	}
	return required;
}

int main()
{
	int test_cases, s_max, temp;
	vector<int> s_list;
	string str;
	req required;
	cin >> test_cases;
	
	for(int i = 0; i < test_cases; i++)
	{
		cin >>s_max;
		string str;
		cin>>str;
		for(int j=0; j < str.size(); j++)
		{
			char temp1[2];
			temp1[0] = str.at(j);
			temp1[1] = '\0';
			temp = atoi(temp1);
			s_list.push_back(temp);
		}
		
		required = cal_req(s_list, s_max);
		cout << "Case #"<<i+1<<": "<< required.num << endl;
		s_list.clear();
		str.clear();
	}
	return 0;
}