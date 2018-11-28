#include<iostream>

void Case()
{
    unsigned int A,B,K;
    std::cin >> A >> B >> K;
    int count;
    for (unsigned int i = 0; i < A; ++i)
        for (unsigned int j = 0; j < B; ++j)
            count += (i & j) < K;
    std::cout << count;
}

int main()
{
    int caseCount = 0;

    std::cin >> caseCount;
    for (int i = 1; i <= caseCount; ++i)
    {
        std::cout << "Case #" << i << ": ";
        Case();
        std::cout << std::endl;
    }
}
