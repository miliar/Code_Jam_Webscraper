#include <iostream>
using namespace std;
int main()
{
	int T;
	cin >> T;
	for(int c=1;c<=T;c++)
	{
		int totalTillNow=0;
		int added=0;
		int maxShyness;
		cout << "Case #"<<c<<": ";
		cin >> maxShyness;
		
		string inp;
		cin >> inp;

		for(int i=0;i<inp.size();i++)
		{
			while(totalTillNow<i)
			{
				totalTillNow++;
				added++;
			}
			totalTillNow+=inp[i]-'0';
		}
		cout << added << endl;
	}
	return 0;
}
