#include <bits/stdc++.h>

using namespace std;

int solve(const string &pancakes)
{
    int answer = 0;
    for (int i = 1; i < pancakes.size(); i++)
        if (pancakes[i] != pancakes[i - 1]) answer++;
    if (pancakes[pancakes.size() - 1] == '-') answer++;
    return answer;
}

int main()
{
    //freopen("B.in", "r", stdin);
    int t;
    string input;
    cin >> t;
    //freopen("B.out", "w", stdout);
    for (int i = 0; i < t; i++)
    {
        cin >> input;
        cout << "Case #" << i + 1 << ": " << solve(input) << endl;
    }
    //fclose(stdout);
	//fclose(stdin);
	return 0;
}
