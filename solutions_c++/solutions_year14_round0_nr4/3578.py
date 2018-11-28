#include <algorithm>
#include <iostream>
#include <vector>
#include <functional>
#include <cassert>

int War(std::vector<double>& Nao, std::vector<double>& Ken)
{
    int scoreNao = 0;

    std::vector<double>::iterator kenPlay = Ken.begin();
    for (std::vector<double>::iterator naoPlay = Nao.begin();
         naoPlay != Nao.end(); ++naoPlay)
    {
        if (*kenPlay > *naoPlay)
            ++kenPlay;
        else
            ++scoreNao;
    }

    return scoreNao;
}

int DWar(std::vector<double> Nao, std::vector<double> Ken)
{
    int scoreNao = 0;

    std::vector<double>::iterator kenPlay = Ken.begin();
    std::vector<double>::iterator naoPlay = Nao.begin();
    int trick = 0;
    do
    {
        if (*naoPlay > *kenPlay)
        {
            ++scoreNao;
            ++naoPlay;
            ++kenPlay;
        }
        else
        {
            kenPlay++;
            ++trick;
        }
    } while (naoPlay != (Nao.end() - trick));

    return scoreNao;
}

void Case()
{
    int N;
    std::cin >> N;
    std::vector<double> Nao(N), Ken(N);

    for (int i = 0; i < N; ++i)
    {
        double val;
        std::cin >> val;
        Nao[i]= val;
    }
    for (int i = 0; i < N; ++i)
    {
        double val;
        std::cin >> val;
        Ken[i] = val;
    }
    std::sort(Nao.begin(), Nao.end(), std::greater<double>());
    std::sort(Ken.begin(), Ken.end(), std::greater<double>());

    int dwar = DWar(Nao, Ken);
    int war = War(Nao, Ken);
    assert(dwar <= N);
    assert(war <= N);
    assert(dwar >= war);
    std::cout <<  dwar << " " << war;
}

int main()
{
    int caseCount;
    std::cin >> caseCount;
    for(int i = 1; i <= caseCount; ++i)
    {
        std::cout << "Case #" << i << ": ";
        Case();
        std::cout << std::endl;
    }
    return 0;
}
