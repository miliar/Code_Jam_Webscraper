#include <bits/stdc++.h>

using namespace std;

const int asleep = 1023;

void addNum(int number, int &awake)
{
    while (number)
    {
        awake |= 1 << (number % 10);
        number /= 10;
    }
}

bool solve(const int &n, unsigned long long &answer)
{
    if (n == 0) return false;
    int awake = 0;
    answer = n;
    addNum(n, awake);
    while (awake != asleep)
    {
        answer += n;
        addNum(answer, awake);
    }
    return true;
}

int main()
{
    //freopen("A.in", "r", stdin);
    int t, n;
    unsigned long long answer;
    cin >> t;
    //freopen("A.out", "w", stdout);
    for (int i = 0; i < t; i++)
    {
        cin >> n;
        cout << "Case #" << i + 1 << ": ";
        if (solve(n, answer))
            cout << answer << endl;
        else cout << "INSOMNIA\n";
    }
    //fclose(stdout);
	//fclose(stdin);
	return 0;
}
