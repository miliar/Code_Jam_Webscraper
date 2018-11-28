#include <iostream>
#include <fstream>

using namespace std;

ofstream fout("output.txt");

int main()
{
    int T;
    cin >> T;	
    for (int t = 0; t < T; ++t)
    {
        int n;
        string audence;
    	cin >> n;
        cin >> audence;
        cout << audence << endl;
        int answer = 0;
        int partSum = 0;

        for (int i = 0; i < audence.size(); ++i)
        {
        	if (partSum < i)
        	{
        		int delta = i - partSum;
           		answer += delta;
           		partSum += delta;
            }
            partSum += audence[i] - '0';
        }
        fout << "Case #" << t + 1 << ": " << answer << endl;
    }

	return 0;
}