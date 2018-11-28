#include <fstream>
#include <algorithm>
#include <string>

// Well this is a mess.

enum class Outcome
{
    X,
    O,
    Unfinished,
    Draw
};

enum class LineResult
{
    X,
    O,
    None
};

LineResult solveLine(char* grid, int a, int b, int c, int d)
{
    char values[] = { grid[a], grid[b], grid[c], grid[d] };

    if(std::any_of(values, values + sizeof(values), [](char x){ return x == '.';}))
    {
        return LineResult::None;
    }

    if(std::all_of(values, values + sizeof(values), [](char x){ return x != 'O'; }))
    {
        return LineResult::X;
    }

    if(std::all_of(values, values + sizeof(values), [](char x){ return x != 'X'; }))
    {
        return LineResult::O;
    }

    return LineResult::None;
}

Outcome solve(char* grid)
{
    for(int col = 0; col < 4; ++col )
    {
        auto result = solveLine(grid, col, col + 4, col + 8, col + 12);
        if(result != LineResult::None)
        {
            switch(result)
            {
            case LineResult::X:
                return Outcome::X;
            case LineResult::O:
                return Outcome::O;
            }
        }
    }

    for(int row = 0; row < 4; ++row )
    {
        auto result = solveLine(grid, row * 4, row * 4 + 1, row * 4 + 2, row * 4 + 3);
        if(result != LineResult::None)
        {
            switch(result)
            {
            case LineResult::X:
                return Outcome::X;
            case LineResult::O:
                return Outcome::O;
            }
        }
    }

    {
        auto result = solveLine(grid, 0, 5, 10, 15);
        if(result != LineResult::None)
        {
            switch(result)
            {
            case LineResult::X:
                return Outcome::X;
            case LineResult::O:
                return Outcome::O;
            }
        }
    }

    {
        auto result = solveLine(grid, 3, 6, 9, 12);
        if(result != LineResult::None)
        {
            switch(result)
            {
            case LineResult::X:
                return Outcome::X;
            case LineResult::O:
                return Outcome::O;
            }
        }
    }

    if(std::any_of(grid, grid + 16, [](char x){ return x == '.'; }))
    {
        return Outcome::Unfinished;
    }
    
    return Outcome::Draw;
}

std::ostream& operator << (std::ostream& stream, Outcome outcome)
{
    switch(outcome)
    {
    case Outcome::X:
        stream << "X won";
        break;
    case Outcome::O:
        stream << "O won";
        break;
    case Outcome::Draw:
        stream << "Draw";
        break;
    case Outcome::Unfinished:
        stream << "Game has not completed";
        break;
    }
    return stream;
}

int main()
{
    std::ifstream input("A-small-attempt0.in");
    std::ofstream output("A-small-attempt0.out");

    int count = 0;
    input >> count;

    for( int i = 0; i < count; ++i )
    {
        char grid[16];
        for(int j = 0; j < 16; ++j )
        {
            input >> grid[j];
        }

        output << "Case #" << i + 1 << ": " << solve(grid) << '\n';
    }

    return 0;
}