#include <iostream>

using namespace std;
int main()
{
	int ret = 0,T;
	std::cin >> T;
	std::string plusmin;
	getline(cin,plusmin);
	for(int t = 0;t<T;t++)
	{
		ret = 0;
		getline(cin,plusmin);
		//std::cout << plusmin << endl;
		int j = 0;
		while(j<plusmin.size() && plusmin[j]=='-')
		{
			j++;
		}
		if(j>0) ret++;

		while(j<plusmin.size())
		{
			while(j<plusmin.size() && plusmin[j]=='+')
			{
				j++;
			}
			if(j == plusmin.size()) break;

			while(j<plusmin.size() && plusmin[j]=='-')
			{
				j++;
			}
			ret += 2;

		}
		std::cout << "Case #" << t+1 << ": " << ret << endl;
	}

	return 0;
}