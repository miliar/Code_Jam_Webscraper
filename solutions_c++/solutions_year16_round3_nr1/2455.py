#include <iostream>
#include <cmath>
#include <iomanip>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

int main()
{
	int times;
	int loopcount = 1;
	cin >> times;

	while(times--)
	{
		int num,temp,total_num;
		total_num = 0;
		cin >> num;
		vector<int> data;
		vector<char> output;
		vector<int> output_num;
		for(int i = 0; i < num; i++)
		{
			cin >> temp;
			total_num += temp;
			data.push_back(temp);
		}

		int max = 0;
		int max_num = 0;
		vector<int> record;
		while(total_num > 0)
		{
			for(int i = 0; i < data.size(); i++)
			{
				if(data[i] == 0)
					continue;
				if(data[i] > max)
				{
					max = data[i];
					max_num = 1;
					record.clear();
					record.push_back(i);
				}
				else
				{
					if(data[i] == max)
					{
						max_num += 1;
						record.push_back(i);
					}
				}
			}

			if(max_num == 1)
			{
				if(data[record[0]] > 1)
				{
					data[record[0]] -= 2;
					output.push_back(record[0] + 'A');
					output_num.push_back(2);
					total_num -= 2;
				}
				else
				{
					data[record[0]] -= 1;
					output.push_back(record[0] + 'A');
					output_num.push_back(1);
					total_num -= 1;
				}
			}

			else
			{
				if(max_num == 3)
				{
					data[record[0]] -= 1;
					output.push_back(record[0] + 'A');
					output_num.push_back(1);
					total_num -= 1;
				}
				else
				{
					data[record[0]] -= 1;
					data[record[1]] -= 1;
					output.push_back(record[0] + 'A');
					output.push_back(record[1] + 'A');
					output_num.push_back(0);
					output_num.push_back(0);
					total_num -= 2;
				}
				
			}
			max = 0;
			max_num = 0;

		}


		cout << "Case #" << loopcount << ": " ;

		int j = 0;
		for (int i = 0; i < output.size(); i++)
		{
			if(i != 0)
				cout << " ";
			if(output_num[j] == 0)
			{
				cout << output[i] << output[i+1];
				j+= 2;
				i+= 1;
			}
			else
			{
				if(output_num[j] == 1)
				{
					cout << output[i];
					j++;
				}
				else
				{
					cout << output[i] << output[i];
					j++;
				}
			}
		}
		cout << endl;
		loopcount++;


	}



	return 0;
}