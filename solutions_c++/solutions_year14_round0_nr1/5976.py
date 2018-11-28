#include <fstream>
#include <vector>




int main()
{
    int cards[4][4], test1[4], which = 0;
    std::fstream input("A-small-attempt3.in"), output("output.txt");
    int T = 0, ans1 = 0, ans2 = 0;

    input >> T;
    for (int i = 1; i <= T; ++i)
    {
        which = 0;
        input >> ans1;
        for (int j = 0; j < 4; ++j)
        {
            for (int k = 0; k < 4; ++k)
            {
                input >> cards[j][k];
            }
        }

        for (int j = 0; j<4; ++j)
        {
            test1[j] = cards[ans1-1][j];
        }

        input >> ans2;
        for (int j = 0; j < 4; ++j)
        {
            for (int k = 0; k < 4; ++k)
            {
                input >> cards[j][k];
            }
        }
        for (int j = 0; j<4; ++j)
        {
            for (int k = 0; k < 4; k++)
            {
                if (test1[j] == cards[ans2-1][k] && which == 0)
                {
                    which = test1[j];
                }
                else if (test1[j] == cards[ans2-1][k] && which != 0)
				{
					which = -1;
				}
            }
            if (j == 3 && which == 0)
			{
				which = -2;
			}
        }
        output << "Case #" << i << ": ";
        if (which > 0)
        {
            output << which;
        }
        else if (which == -1)
        {
            output << "Bad magician!";
        }
        else if (which == -2)
        {
            output << "Volunteer cheated!";
        }
        output << std::endl;
    }

    return 0;
}
