#include<iostream>
#include<cmath>
#include<algorithm>

const int max_depth = 40;

int Solve(int P, int Q, int depth)
{
    if (depth > max_depth)
        return -1;
    //std::cerr << depth << ":" << P << "," << Q << "," << 2*(float)P/(float)Q - 1 << ";" <<std::endl;
    float discr = 2*(float)P/(float)Q - 1;
    if (discr == 0)
        return depth;
    else if (discr > 0)
    {
        if (Solve(2*P-Q, Q, depth+1) > 0)
            return depth;
        else
            return -1;
    }
    else
    {
        if (Q % 2 == 0)
            return Solve(P, Q/2, depth+1);
        else
            return Solve(2*P, Q, depth+1);
    }
}

void Case()
{
    int P,Q;
    char dummy;
    std::cin >> P >> dummy >> Q;
    int sol = Solve(P,Q,1);
    if (sol > 0)
        std::cout << sol;
    else
        std::cout << "impossible";
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
