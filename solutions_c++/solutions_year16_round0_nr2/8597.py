#include <iostream> 
#include <string>
#include <list>
#include <sstream> 
#include <vector>

using namespace std;
void PrintList(vector<int> lst_side)
{
	for(int i = 0; i < lst_side.size(); i++)
	{
		cout<<lst_side.at(i)<<" " ;
	}
	cout<<endl;
}

void flip(int position, vector<int> &lst_side)
{
	int side;
	vector<int> tmp_side;
	for(int i = position; i > 0; i--)
	{
		if(lst_side.at(i-1) == 1)
			side = 0;
		else
			side = 1;
		tmp_side.push_back(side);
	}
	for(int i = 0; i < position; i++)
	{
		lst_side[i] = tmp_side.at(i);
	}
}

void main(){
	int N, count;
	string str, word;
	vector<int> lst_side;
	cin >> N;
	for(int i=0; i < N; i++){
		while(getline(cin, str))
		{
			if(str != "")
				break;
		}
		//cout<<"String : "<<str<<endl;
		lst_side.clear();
		for(int j=0; j < str.size(); j++)
		{
			if(str[j] == '+')
				lst_side.push_back(1);
			else
				lst_side.push_back(0);
		}
		//PrintList(lst_side);
		//flip(4, lst_side);
		//PrintList(lst_side);
		count = 0;
		for(int j = lst_side.size(); j > 0; j--)
		{
			if(lst_side.at(j-1) == 1)
				continue;
			
			if(lst_side.front() == 0)
			{
				flip(j, lst_side);
				count++;
				//PrintList(lst_side);
			}
			else
			{
				for(int k = j; k > 0; k--)
				{
					if(lst_side.at(k-1) == 0)
						continue;
					flip(k, lst_side);
					count++;
					//PrintList(lst_side);
					break;
				}
				flip(j, lst_side);
				count++;
				//PrintList(lst_side);
			}
			
		}
		cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
}

