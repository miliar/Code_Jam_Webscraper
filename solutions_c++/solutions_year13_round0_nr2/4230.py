#include <iostream>
#include <algorithm>

template <typename T>
struct Board {
    size_t width;
    size_t height;
    T* board;

    Board(size_t w, size_t h) :
        width(w),
        height(h),
        board(new T[w*h])
    { }

    Board(Board const& other) :
        width(other.width),
        height(other.height),
        board(new T[width*height])
    {
        std::copy_n(other.board, width*height, this->board);
    }

    ~Board() {
        delete[] board;
    }

    T* operator [] (size_t row)
    {
        return board + (row*width);
    }
    
    T const* operator [] (size_t row) const
    {
        return board + (row*width);
    }

    size_t numCells() const
    {
        return width * height;
    }

};


template <typename T>
std::istream& operator>>(std::istream& is, Board<T>& b)
{
    for (size_t i = 0; i < b.numCells(); ++i)
    {
        int s;
        is >> s;
        b.board[i] = s;
    }

    return is;
}

template <typename T>
std::ostream& operator<<(std::ostream& os, Board<T>& b)
{
    for (size_t i = 0; i < b.height; ++i)
    {
        for (size_t j = 0; j < b.width; ++j)
        {
            os << static_cast<int>(b[i][j]) << " ";
        }
        os << std::endl;
    }

    return os;
}

bool isRowWithinBounds(Board<char> const& b, char limit, size_t row)
{
    for (size_t i = 0; i < b.width; ++i)
    {
        if (b[row][i] > limit)
        {
            return false;
        }
    }

    return true;
}

bool isColWithinBounds(Board<char> const& b, char limit, size_t col)
{
    for (size_t i = 0; i < b.height; ++i)
    {
        if (b[i][col] > limit)
        {
            return false;
        }
    }

    return true;
}

/**
 * Check whther the particular cell in the yard could be produced
 */
bool isCellValid(Board<char> const& b, size_t row, size_t col)
{
    return isRowWithinBounds(b, b[row][col], row) ||
           isColWithinBounds(b, b[row][col], col);
}

bool isBoardValid(Board<char> const& b)
{

    for (size_t i = 0; i < b.height; ++i)
    {
        for (size_t j = 0; j < b.width; ++j)
        {
            if (!isCellValid(b, i, j))
            {
                return false;
            }
        }
    }

    return true;
}

std::string answer(bool a)
{
    if (a)
    {
        return "YES";
    }

    return "NO";
}


int main(int argc, char const *argv[])
{
    (void) argc;
    (void) argv;

    // io efficiency
    std::ios_base::sync_with_stdio(false);
    std::cin.tie(0);

    size_t numExamples;
    std::cin >> numExamples;

    for (size_t example = 0; example < numExamples; ++example)
    {
        size_t width;
        size_t height;
        std::cin >> height >> width;

        Board<char> b(width, height);

        std::cin >> b;

        //std::cout << b;
        std::cout << "Case #" << (example+1) << ": " << answer(isBoardValid(b));
        std::cout << std::endl;
    }

    return 0;
}
