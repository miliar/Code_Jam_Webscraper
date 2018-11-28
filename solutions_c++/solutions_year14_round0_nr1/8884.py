#include <iostream>
#include <fstream>
#include <vector>

void solution(int test, const std::vector<int>& first, const std::vector<int>& second, std::ofstream& stream)
{
    int k = 0;
    int ans;
    for (int i = 0; i < 4; ++i)
    for (int j = 0; j < 4; ++j)
    if (first[i] == second[j]) {
        k++;
        ans = first[i];
    }
    
    stream << "Case #" << test << ": ";

    if (k == 0)
        stream << "Volunteer cheated!";
    else
    if (k == 1)
        stream << ans;
    else
        stream << "Bad magician!";
    stream << std::endl;
}

int main()
{
    std::ifstream file_in("A-small-attempt0.in");
    std::ofstream file_out("A-small-attempt0.out");

    int test;
    file_in >> test;
    for (int t = 0; t < test; ++t) {
        int y;
        file_in >> y;
        y--;
        std::vector<int> first;
        for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j) {
            int t;
            file_in >> t;
            if (i == y)
                first.push_back(t);
        }

        int x;
        file_in >> x;
        x--;
        std::vector<int> second;
        for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j) {
            int t;
            file_in >> t;
            if (i == x)
                second.push_back(t);
        }
        solution(t + 1, first, second, file_out);
    }
}
