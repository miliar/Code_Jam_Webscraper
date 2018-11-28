#include <fstream>
#include <iostream>
#include <string>
#include <vector>

void FlipPancakes(int End, std::vector<bool> &Pancakes)
{
    for (int i = 0; i < End; i++)
        Pancakes[i] = !Pancakes[i];
}

bool ArePancakesHappy(std::vector<bool> &Pancakes)
{
    for (auto b : Pancakes)
        if (!b)
            return false;

    return true;
}

void main()
{
    int T = 0, Flips = 0;
    std::string S;
    std::vector<bool> Pancakes;

    std::ifstream inputFile("input.in");
    std::ofstream outputFile("output.out", std::ofstream::out | std::ofstream::trunc);

    if (inputFile.is_open() && outputFile.is_open())
    {
        while (inputFile >> T)
        {
            inputFile.ignore();

            for (int i = 0; i < T; i++)
            {
                std::getline(inputFile, S);
                Pancakes.clear();
                Flips = 0;

                if (S.size() == 0)
                {
                    outputFile << "Case #" << i + 1 << ": " << Flips << std::endl;
                    continue;
                }

                for (int i = 0; i < S.size(); i++)
                    Pancakes.push_back(S[i] == '+');

                bool AllOnOneSide;

                while (true)
                {
                    AllOnOneSide = true;

                    if (Pancakes.size() > 1)
                    {
                        for (int i = 1; i < Pancakes.size(); i++)
                        {
                            if (Pancakes[i] != Pancakes[i - 1])
                            {
                                AllOnOneSide = false;
                                FlipPancakes(i, Pancakes);
                                Flips++;
                                break;
                            }
                        }
                    }
                    else
                    {
                        if (!Pancakes[0])
                        {
                            Flips++;
                            Pancakes[0] = true;
                        }

                        break;
                    }

                    if (AllOnOneSide)
                    {
                        if (!ArePancakesHappy(Pancakes))
                        {
                            Flips++;
                            FlipPancakes(int(Pancakes.size()), Pancakes);
                        }

                        break;
                    }
                }

                outputFile << "Case #" << i + 1 << ": " << Flips << std::endl;
            }
        }

        inputFile.close();
        outputFile.close();
    }
}