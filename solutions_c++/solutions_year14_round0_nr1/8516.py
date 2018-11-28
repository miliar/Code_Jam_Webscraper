#include <iostream>

void print_result(int a[4], int b[4])
{
    int card = -1;
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            if (a[i] == b[j])
            {
                if (card != -1)
                {
                    std::cout << "Bad magician!" << std::endl;
                    return;
                }
                card = a[i];
            }

    if (card != -1)
        std::cout << card << std::endl;
    else
        std::cout << "Volunteer cheated!" << std::endl;

}

int main()
{
    int T; std::cin >> T; std::cin.ignore();

    for (int i = 1; i <= T; ++i)
    {
        int first_answer; std::cin >> first_answer; std::cin.ignore();
        int first[4][4];
        for (int j = 0; j < 4; ++j)
        {
            std::cin >> first[j][0] >> first[j][1] >> first[j][2] >> first[j][3];
            std::cin.ignore();
        }
        int second_answer; std::cin >> second_answer; std::cin.ignore();
        int second[4][4];
        for (int j = 0; j < 4; ++j)
        {
            std::cin >> second[j][0] >> second[j][1] >> second[j][2] >> second[j][3];
            std::cin.ignore();
        }

        std::cout << "Case #" << i << ": ";
        print_result(first[first_answer - 1], second[second_answer - 1]);
    }
}
