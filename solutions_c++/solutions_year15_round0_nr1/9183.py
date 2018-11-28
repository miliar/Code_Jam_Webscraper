#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;

int main()
{
    freopen("output.txt","w",stdout);
    freopen("input.txt","r",stdin);
    int T;
    cin >> T;
    // cout << "T: " << T << endl;

	int S;
    for (int iteration = 0; iteration < T; ++iteration)
    {
    	cin >> S;
    	cout << "Case #" << (iteration + 1) << ": ";
		string number;
		cin >> number;
		// cout << "\t";
		int parados = 0;
		int agregados = 0;
		for (int s_i = 0; s_i < number.length(); ++s_i)
		{
			// cout << s_i << " > " << parados << " + " << agregados << endl;
			if(s_i > parados + agregados) {
				// cout << s_i - parados - agregados << endl;
				agregados += s_i - parados - agregados;
			}
			// cout << number[ s_i ] << endl;
			parados += number[ s_i ] - 48;
			// cout << endl;
		}
		cout << agregados;
		cout << endl;
    }

    // cout<<"write in file";
    return 0;
}