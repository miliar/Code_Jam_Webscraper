// Counting Sheep

#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

bool exists(vector<int> &v, int c)
{
	for(int i = 0; i < v.size(); i++)
	{
		if(c == v.at(i))
			return true;
	}
	return false;
}

int main()
{
	ofstream gp1;
	ifstream gp;
	string src;
	
	gp1.open("output.txt");
	gp.open("input.txt");
	
	int tc;
	gp >> tc;
	getline(gp,src);
	//gp1 << "tcs : " << tc << endl;
	
	for(int tc_cnt = 1; tc_cnt <= tc ; tc_cnt++)
	{
		long int N;
		gp >> N;
		//cout << "tc: " << N << endl;
		vector<int> alpha;
		long int temp = N;
		int last_digit = -1;
		// initialize big array
	if(N != 0) {
		for(int times = 1; alpha.size() < 10; times++)
		{
			temp = times * N;
			last_digit = temp;
			//gp1 << "N: " << temp << endl;
			long int div = temp;
			while(div > 0)
			{
				int res = div%10;
				if(!exists(alpha,res))
				{
					//gp1 << "pushing: " << res << endl;
					alpha.push_back(res);
				}
				div /= 10;
			}
		} 
	}
		alpha.clear();
		if(last_digit == -1)
		{
			gp1 << "Case #" <<  tc_cnt << ": INSOMNIA" << endl;
		}
		else
		{
			gp1 << "Case #" <<  tc_cnt << ": " << last_digit << endl;
		}
	}
	
	gp.close();
	gp1.close();
}