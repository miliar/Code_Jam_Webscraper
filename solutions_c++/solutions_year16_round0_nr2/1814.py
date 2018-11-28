#include <iostream>
#include <fstream>
#include <string>

int flip_count(std::string pancakes);

int main()
{
    // In & out.
    std::ifstream in;
    std::ofstream out;

    // Open files.
    in.open("B-small-attempt0.in");
    out.open("B-small-attempt0.out");

    // Global variables.
    int T;
    std::string pancakes;

    in >> T;
    for(int t = 0; t < T; t ++)
    {
        in >> pancakes;
        out << "Case #" << t + 1 << ": " << flip_count(pancakes) << std::endl;
    }

    // Close files.
    out.close();
    in.close();

    return 0;
}


int flip_count(std::string pancakes)
{
    int flips = 0;

    for(int i = 0; i < pancakes.length()-1; i ++)
    {
        if(pancakes[i] != pancakes[i+1])
        {
            flips ++;
        }
    }

    if(pancakes[pancakes.length()-1] == '-')
    {
        flips ++;
    }

    return flips;
}
