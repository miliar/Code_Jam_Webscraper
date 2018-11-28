#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

long long getgeosum(int base, int complexity, int start)
{
    long long ans = 1;
    for(int i = start, j = 0; i < (complexity+start); ++i, ++j)
    {
        ans += i * pow(static_cast<double>(base), static_cast<double>(j));
    }
	return ans;
}


int main()
{
	char T;
	cin >> T;
    int K = 0;
    int C = 0;
    int S = 0;
    vector<long long> answer;
	for(int i = 0; i < T; ++i)
	{
		while (!answer.empty())
		{
            answer.pop_back();
		}
        cin >> K >> C >> S;
        int minans = ceil(static_cast<double>(K)/static_cast<double>(C));
        if(K == S) // check all
        {
            for(int j = 0; j < S; ++j)
            {
                answer.push_back(j+1);
            }
        }
        else if(minans <= S)
        {
            int base = K;
            int complexity = C;
            long long ans = 0;
            for(int j = 0; j < minans; ++j)
            {
                ans = getgeosum(base, complexity, j);
                answer.push_back(ans);
            }
        }

        cout << "Case # " << i+1 << ": ";
        int len = answer.size();
        if(answer.empty())
		{
            cout << "IMPOSSIBLE" << endl;
		}
        else
        {
            for(int k = 0; k < len; ++k)
            {
                cout << answer.at(k);
                if(k < len-1)
				{
                    cout << " ";
				}
            }
            cout << endl;
        }
        if(i+1 == T) return 0;
	}

    return 0;
}
