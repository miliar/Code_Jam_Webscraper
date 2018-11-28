#include <iostream>
#include <fstream>
#include <cassert>
#include <string>

const char Good = '+';
const char Bad = '-';

// turn a pancake over
void flip(std::string& pancakes, size_t index)
{
    pancakes[index] = (pancakes[index] == Good) ? Bad : Good;
}

// flip an entire stack
void flip(std::string& pancakes, size_t first, size_t last)
{
    while (first < last)
    {
        std::swap(pancakes[first], pancakes[last]);
        flip(pancakes, first);
        flip(pancakes, last);
        ++first;
        --last;
    }
    
    if (first == last)
        flip(pancakes, first);
}

size_t find_min_flips(std::string pancakes)
{
    if (pancakes.empty())
        return 0;
    
    // index the last bad pancake in the stack, those after are never touched
    size_t last = pancakes.size() - 1;
    for(size_t flips = 0; true; ++flips)
    {
        while(pancakes[last] == Good)
        {
            if (last == 0)   // all good!
                return flips;
            
            --last;
        }
        
        // last element in the first run of pancakes
        size_t front = 0;
        for(; front != last && pancakes[front] == pancakes[front + 1]; ++front);
        
        if (pancakes[front] == Good)
            flip(pancakes, 0, front);
        else if (pancakes[front] == Bad)
            flip(pancakes, 0, last);
    }
}

int main()
{
    std::ifstream input;
    input.open("/Users/stammerj/playground/jam/pancakes/large0", std::ifstream::in);
    assert(input.good());
 
    size_t cases;
    input >> cases;
    for (size_t i = 0; i < cases; ++i)
    {
        std::string pancakes;
        input >> pancakes;
        std::cout << "Case #" << (i + 1) << ": " << find_min_flips(pancakes) << std::endl;
    }
    
    return EXIT_SUCCESS;
}