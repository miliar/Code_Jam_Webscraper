#include <iostream>
#include <string>
#include <sstream>
#include <vector>
#include <iterator>

const std::vector<std::string> readCards(void)
{
    int n = 0;;
    std::cin >> n;
    std::string newline;
    std::getline(std::cin, newline);

    std::vector<std::string> tokens;
    for (int row = 1; row <= 4; ++row)
    {
        std::string temp;
        std::getline(std::cin, temp);
        if (row == n)
        {
            std::istringstream iss(temp);
            std::copy(std::istream_iterator<std::string>(iss), std::istream_iterator<std::string>(), std::back_inserter<std::vector<std::string>>(tokens));
        }
    }

    return tokens;
}

int main(int argc, const char *argv[])
{
    int cases = 0;
    std::cin >> cases;

    for (int i = 1; i <= cases; ++i)
    {
        auto firstChoice = readCards();
        auto secondChoice = readCards();
        std::vector<std::string> ans;
        for (int j = 0; j < firstChoice.size(); ++j)
        {
            for (int k = 0; k < secondChoice.size(); ++k)
            {
                if (firstChoice[j] == secondChoice[k])
                {
                    ans.push_back(firstChoice[j]);
                }
            }
        }
        std::cout << "Case #" << i << ": ";
        std::string response;
        switch (ans.size())
        {
            case 0:
                response = "Volunteer cheated!";
                break;
            case 1:
                response = ans[0];
                break;
            default:
                response = "Bad magician!";
                break;
        }
        std::cout << response << std::endl;
    }

    return 0;
}
