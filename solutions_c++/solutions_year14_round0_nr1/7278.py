#include <iostream>
#include <vector>

std::vector<int> row()
{
    int r = 0;
    std::cin >> r;
    std::vector<int> v;
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j)
        {
            int x = 0;
            std::cin >> x;
            if (i == r - 1)
                v.push_back(x);
        }
    return v;
}

int main()
{
    int T;
    std::cin >> T;
    for (int i = 0; i < T; ++i)
    {
        std::vector<int> a = row();
        std::vector<int> b = row();
        int x = 0;
        for (int i = 0; i < a.size(); ++i)
            for (int j = 0; j < b.size(); ++j)
                if (a[i] == b[j])
                {
                    if (x < 1)
                        x = a[i];
                    else
                        x = -1;
                }
        if (x > 0)
            std::cout << "Case #" << i + 1 << ": " << x << std::endl;
        else if (x < 0)
            std::cout << "Case #" << i + 1 << ": " << "Bad magician!" << std::endl;
        else
            std::cout << "Case #" << i + 1 << ": " << "Volunteer cheated!" << std::endl;
    }
}
