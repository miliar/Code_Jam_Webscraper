#include <iostream>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <algorithm>
using namespace std;


bool multiple(size_t X, size_t C)
{
    return C % X == 0;
}

class Solve
{
public:
    void solve()
    {
        size_t X, R, C;
        cin >> X >> R >> C;

        bool gabriel = false;

        if (R > C) swap(R, C);

        if (X == 1)
        {
            gabriel = true;
        }
        else
        {
            switch (R * C)
            {
            case 1:
                break;
            case 2:
                if (X == 2)
                    gabriel = true;
                break;
            case 3:
                break;
            case 4:
                if (X == 2)
                    gabriel = true;
                break;
            case 5:
                break;
            case 6:
                if (R == 1)
                {
                    if (X == 2)
                        gabriel = true;
                }
                else if (R == 2)
                {
                    if (X == 2 || X == 3)
                        gabriel = true;
                }
                break;
            case 7:
                break;
            case 8:
                if (X == 2)
                    gabriel = true;
                break;
            case 9:
                if (R != 1)
                {
                    if (X == 3)
                        gabriel = true;
                }
                break;
            case 10:
                if (X == 2)
                    gabriel = true;
                break;
            case 11:
                break;
            case 12:
                if (R == 1)
                {
                    if (X == 2)
                        gabriel = true;
                }
                else if (R == 2)
                {
                    if (X == 2 || X == 3 || X == 4)
                        gabriel = true;
                }
                else if (R == 3)
                {
                    if (X == 2 || X == 3 || X == 4)
                    {
                        gabriel = true;
                    }
                }
                break;
            case 13:
                break;
            case 14:
                if (X == 2)
                    gabriel = true;
                break;
            case 15:
                if (R != 1)
                {
                    if (X == 3)
                        gabriel = true;
                }
                break;
            case 16:
                if (R == 1)
                {
                    if (X == 2)
                        gabriel = true;
                }
                else if (R == 2)
                {
                    if (X == 2)
                        gabriel = true;
                }
                else if (R == 4)
                {
                    if (X == 2 || X == 4)
                        gabriel = true;
                }
                break;
            }
        }

        if (gabriel)
            cout << "GABRIEL";
        else
            cout << "RICHARD";
    }
};

int main()
{
	size_t n;
	std::cin >> n;
	while(std::cin.get() != '\n');
	for(size_t i=1; i <= n; i++)
	{
		std::cout << "Case #" << i << ": ";
        Solve s;
		s.solve();
		std::cout << std::endl;
	}
}
