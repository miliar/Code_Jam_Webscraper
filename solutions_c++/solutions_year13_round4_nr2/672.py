// 1B_1.cpp : Defines the entry polong long for the console application.
//

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int main(int argc, char* argv[])
{
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
    long long count_of_games;
    cin >> count_of_games;
    for (long long l = 1; l <= count_of_games; ++l)
    {
        long long n, p;
        cin >> n >> p;
        long long max_gamer = 1;
        for (int i = 0; i < n; ++i)
            max_gamer *= 2;
        max_gamer--;
        long long count_of_gamers = max_gamer + 1;
        while (count_of_gamers > p)
        {
            count_of_gamers /= 2;
            max_gamer &= max_gamer - 1;
        }
        long long min_gamer = 0;
        count_of_gamers = 1;
        for (int i = 0; i < n; ++i)
            count_of_gamers *= 2;
        p = count_of_gamers - p;
        while (count_of_gamers / 2 > p)
        {
            count_of_gamers /= 2;
            min_gamer = 2 * (min_gamer + 1);
        }
        count_of_gamers = 1;        
        for (int i = 0; i < n; ++i)
            count_of_gamers *= 2;
        --count_of_gamers;
        if (min_gamer > count_of_gamers)
            min_gamer = count_of_gamers;
        cout << "Case #" << l << ": " << min_gamer << ' ' << max_gamer << endl;
    }
	return 0;
}

