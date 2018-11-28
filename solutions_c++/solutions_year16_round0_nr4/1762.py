#include <iostream>
#include <fstream>

int main()
{
    // In & out.
    std::ifstream in;
    std::ofstream out;

    // Open files.
    in.open("D-small-attempt0.in");
    out.open("D-small-attempt0.out");

    // Global variables.
    int T, K, C, S;
    in >> T;
    for(int t = 0; t < T; t ++)
    {
        in >> K >> C >> S;
        // In small dataset, S==K
        out << "Case #" << t + 1 << ": ";
        for(int i = 0; i < K; i ++)
        {
            out << i + 1 << " ";
        }
        out << std::endl;
    }

    // Close files.
    out.close();
    in.close();

    return 0;
}
