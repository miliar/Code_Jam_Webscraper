#include <fstream>
#include <set>

void main()
{
    int N = 0, OtherN = 0, T = 0;
    std::set<int> Digits;
    
    std::ifstream inputFile("large.in");
    std::ofstream outputFile("large.out");

    if (inputFile.is_open() && outputFile.is_open())
    {
        while (inputFile >> T)
        {
            for (int i = 0; i < T; i++)
            {
                inputFile >> N;

                if (N == 0)
                {
                    outputFile << "Case #" << i + 1 << ": " << "INSOMNIA" << std::endl;
                    continue;
                }

                OtherN = 0;
                Digits.clear();
                do
                {
                    OtherN += N;
                    for (int n = OtherN; n > 0;)
                    {
                        Digits.insert(n % 10);
                        n = n / 10;
                    }
                } while (Digits.size() < 10);

                outputFile << "Case #" << i + 1 << ": " << OtherN << std::endl;
            }
        }

        inputFile.close();
        outputFile.close();
    }
}