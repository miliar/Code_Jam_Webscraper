#include <bits/stdc++.h>

void sosi (std::priority_queue <int> gg, std::vector <int> &answer, int fine)
{
    if (gg.top() <= 1)
        return;
    int mv = gg.top();
    answer.push_back(mv + fine);
    gg.pop();
    for (int i = mv / 2; i >= std::max(1, mv / 2 - 1); --i)
    {
        auto temp = gg;
        temp.push(i);
        temp.push(mv - i);

        sosi(temp, answer, fine + 1);
    }

}

int main (int argc, char *argv[])
{
    std::ios_base::sync_with_stdio(false);
    std::ifstream inputStream("E:\\B-small-attempt4.in");
    std::ofstream outputStream("E:\\ccouta.txt");

    std::size_t numOfTestCases = 0;
    inputStream >> numOfTestCases;

    for (std::size_t ix = 0; ix < numOfTestCases; ++ix)
    {

        std::vector <int> answer;
        int diners = 0;
        inputStream >> diners;
        std::priority_queue <int> donuts;

        for (int dinersIx = 0; dinersIx < diners; ++dinersIx)
        {
            int dinersVal = 0;
            inputStream >> dinersVal;
            donuts.push(dinersVal);
        }


        int fine = 0;
        answer.push_back(donuts.top() + fine);
        sosi(donuts, answer, 0);
        //answer.push_back(donuts.top() + fine + 1);



        outputStream << "Case #" << ix + 1 << ": ";
        outputStream << *std::min_element(answer.begin(), answer.end()) << "\n";
    }

    inputStream.close();
    outputStream.close();
}
