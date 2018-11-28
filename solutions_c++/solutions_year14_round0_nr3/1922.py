#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>

enum class CellState
{
    Unknown = 0,

    Mine = 1,

    Opened = 2,

    Clicked = 3,

    Hazard = 4,

    HazardOpened = 5
};

struct TestCase
{
    int rows;
    int columns;
    int mines;
};

struct Solution
{
    CellState** field;

    int rows;

    int columns;

    int leftRows;

    int leftColumns;

    int leftMines;

    bool result;
};

std::vector<TestCase> ReadCases(std::istream& stream)
{
    int totalCases;
    std::vector<TestCase> result;

    stream >> totalCases;

    for (int i = 0; i < totalCases; i++)
    {
        TestCase testCase;

        stream >> testCase.rows >> testCase.columns >> testCase.mines;

        result.push_back(testCase);
    }

    return result;
}

void PrintSolution(Solution& s)
{
    for (int r = 0; r < s.rows; r++)
    {
        for (int c = 0; c < s.columns; c++)
        {
            if (s.field[r][c] == CellState::Clicked)
            {
                std::cout << "c";
            }
            else if (s.field[r][c] == CellState::Mine)
            {
                std::cout << "*";
            }
/*
            else if (s.field[r][c] == CellState::Hazard)
            {
                std::cout << "H";
            }
            else if (s.field[r][c] == CellState::HazardOpened)
            {
                std::cout << "h";
            }
*/
            else
            {
                std::cout << ".";
            }
        }

        std::cout << std::endl;
    }
}

void ReduceProblemByMines(Solution& s)
{
    while (s.leftMines > 0)
    {
        if (s.leftRows > s.leftColumns)
        {
            if (s.leftMines < s.leftColumns)
            {
                return;
            }

            s.leftRows--;
            s.leftMines -= s.leftColumns;

            for (int i = 0; i < s.leftColumns; i++)
            {
                s.field[s.leftRows][i] = CellState::Mine;
            }
        }
        else
        {
            if (s.leftMines < s.leftRows)
            {
                return;
            }

            s.leftColumns--;
            s.leftMines -= s.leftRows;

            for (int i = 0; i < s.leftRows; i++)
            {
                s.field[i][s.leftColumns] = CellState::Mine;
            }
        }
    }
}

bool TryOpenCell(Solution& s, int r, int c)
{
    if ((r >= 0) && (r < s.rows) && (c >= 0) && (c < s.columns))
    {
        if (s.field[r][c] == CellState::Unknown)
        {
            s.field[r][c] = CellState::Opened;
            return true;
        }
        else if (s.field[r][c] == CellState::Hazard)
        {
            s.field[r][c] = CellState::HazardOpened;
            return true;
        }

    }

    return false;
}

void TryMarkHazard(Solution& s, int r, int c)
{
    if ((r >= 0) && (r < s.rows) && (c >= 0) && (c < s.columns))
    {
        if (s.field[r][c] == CellState::Unknown)
        {
            s.field[r][c] = CellState::Hazard;
        }
    }
}

bool IsMine(Solution& s, int r, int c)
{
    if ((r >= 0) && (r < s.rows) && (c >= 0) && (c < s.columns))
    {
        return (s.field[r][c] == CellState::Mine);
    }

    return false;
}

void Unmark(Solution& s)
{
    for (int r = 0; r < s.rows; r++)
    {
        for (int c = 0; c < s.columns; c++)
        {
            if ((s.field[r][c] == CellState::Opened) || (s.field[r][c] == CellState::Hazard) || (s.field[r][c] == CellState::HazardOpened))
            {
                s.field[r][c] = CellState::Unknown;
            }
        }
    }
}

bool CheckSolution(Solution& s)
{
    for (int r = 0; r < s.rows; r++)
    {
        for (int c = 0; c < s.columns; c++)
        {
            if (s.field[r][c] == CellState::Mine)
            {
                TryMarkHazard(s, r - 1, c - 1);
                TryMarkHazard(s, r - 1, c);
                TryMarkHazard(s, r - 1, c + 1);
                TryMarkHazard(s, r, c - 1);
                TryMarkHazard(s, r, c + 1);
                TryMarkHazard(s, r + 1, c - 1);
                TryMarkHazard(s, r + 1, c);
                TryMarkHazard(s, r + 1, c + 1);
            }
        }
    }

//    PrintSolution(s);

    bool changed;
    do
    {
        changed = false;
        for (int r = 0; r < s.leftRows; r++)
        {
            for (int c = 0; c < s.leftColumns; c++)
            {
                if ((s.field[r][c] == CellState::Clicked) || (s.field[r][c] == CellState::Opened))
                {
                    // This cell is near bomb.
                    if (
                        IsMine(s, r - 1, c - 1) ||
                        IsMine(s, r - 1, c) ||
                        IsMine(s, r - 1, c + 1) ||
                        IsMine(s, r, c - 1) ||
                        IsMine(s, r, c + 1) ||
                        IsMine(s, r + 1, c - 1) ||
                        IsMine(s, r + 1, c) ||
                        IsMine(s, r + 1, c + 1))
                    {
                        continue;
                    }

                    changed = TryOpenCell(s, r - 1, c - 1) || changed;
                    changed = TryOpenCell(s, r - 1, c) || changed;
                    changed = TryOpenCell(s, r - 1, c + 1) || changed;
                    changed = TryOpenCell(s, r, c - 1) || changed;
                    changed = TryOpenCell(s, r, c + 1) || changed;
                    changed = TryOpenCell(s, r + 1, c - 1) || changed;
                    changed = TryOpenCell(s, r + 1, c) || changed;
                    changed = TryOpenCell(s, r + 1, c + 1) || changed;
                }
            }
        }
    }
    while (changed);

    for (int r = 0; r < s.leftRows; r++)
    {
        for (int c = 0; c < s.leftColumns; c++)
        {
            if ((s.field[r][c] == CellState::Unknown) || (s.field[r][c] == CellState::Hazard))
            {
                Unmark(s);
                return false;
            }
        }
    }

//    PrintSolution(s);

    return true;
}

bool SelectNextCell(Solution& s, int& r, int& c)
{
    if (c == s.leftColumns - 1)
    {
        if (r == s.leftRows - 1)
        {
            return false;
        }

        r++;
        c = 0;
        return true;
    }

    c++;
    return true;
}

bool Step(Solution& s, int r, int c, bool haveClicked)
{
    // Try to mark current cell as clicked.
    if (!haveClicked && (s.field[r][c] == CellState::Unknown))
    {
        s.field[r][c] = CellState::Clicked;

        if (s.leftMines == 0)
        {
            if (CheckSolution(s))
            {
                return true;
            }
        }

        int nextR = r;
        int nextC = c;

        if (SelectNextCell(s, nextR, nextC))
        {
            if (Step(s, nextR, nextC, true))
            {
                return true;
            }
        }

        s.field[r][c] = CellState::Unknown;
    }

    // Try to mark current cell as mine.
    if ((s.leftMines > 0) && (s.field[r][c] == CellState::Unknown))
    {
        s.field[r][c] = CellState::Mine;
        s.leftMines--;

        if (haveClicked && (s.leftMines == 0))
        {
            if (CheckSolution(s))
            {
                return true;
            }
        }

        int nextR = r;
        int nextC = c;

        if (SelectNextCell(s, nextR, nextC))
        {
            if (Step(s, nextR, nextC, haveClicked))
            {
                return true;
            }
        }

        s.leftMines++;
        s.field[r][c] = CellState::Unknown;
    }

    // Try to leave current cell unknown.
    int nextR = r;
    int nextC = c;

    if (SelectNextCell(s, nextR, nextC))
    {
        if (Step(s, nextR, nextC, haveClicked))
        {
            return true;
        }
    }

    return false;
}

bool ExhaustiveSearch(Solution& s)
{
    return Step(s, 0, 0, false);
}

bool MarkAllUnknownOpen(Solution& s)
{
    for (int r = 0; r < s.leftRows; r++)
    {
        for (int c = 0; c < s.leftColumns; c++)
        {
            if (s.field[r][c] == CellState::Unknown)
            {
                s.field[r][c] = CellState::Opened;
            }
        }
    }
}

Solution* Solve(const TestCase& testCase)
{
    auto s = new Solution();

    s->field = new CellState*[testCase.rows];
    for (int i = 0; i < testCase.rows; i++)
    {
        s->field[i] = new CellState[testCase.columns];
        for (int j = 0; j < testCase.columns; j++)
        {
            s->field[i][j] = CellState::Unknown;
        }
    }

    s->leftColumns = testCase.columns;
    s->rows = testCase.rows;
    s->columns = testCase.columns;
    s->leftRows = testCase.rows;
    s->leftMines = testCase.mines;

    ReduceProblemByMines(*s);

    if (((s->leftColumns <= 4) && (s->leftRows <= 4)) ||
        (s->leftColumns <= 2) || (s->leftRows <= 2))
    {
        s->result = ExhaustiveSearch(*s);
        return s;
    }

    s->field[0][0] = CellState::Clicked;
    s->result = true;


    if ((s->leftColumns >= s->leftRows) && (s->leftColumns >= s->leftMines + 2))
    {
        for (int i = 0; i < s->leftMines; i++)
        {
            s->field[s->leftRows-1][i] = CellState::Mine;
        }

        MarkAllUnknownOpen(*s);

        return s;
    }

    if ((s->leftRows > s->leftColumns) && (s->leftRows >= s->leftMines + 2))
    {
        for (int i = 0; i < s->leftMines; i++)
        {
            s->field[i][s->leftColumns-1] = CellState::Mine;
        }

        MarkAllUnknownOpen(*s);

        return s;
    }

    int mineHalf = s->leftMines/2;
    for (int i = 0; i < mineHalf; i++)
    {
        s->field[s->leftRows-1][i] = CellState::Mine;
        s->leftMines--;
    }

    for (int i = 0; i < s->leftMines; i++)
    {
        s->field[i][s->leftColumns-1] = CellState::Mine;
    }

    s->leftMines = 0;
    MarkAllUnknownOpen(*s);

    return s;
}

int main(int argc, char* argv[])
{
    std::vector<TestCase> cases;

    if (argc == 1)
    {
        cases = ReadCases(std::cin);
    }
    else if (argc == 2)
    {
        std::ifstream stream(argv[1]);
        if (!stream.good())
        {
            return 1;
        }

        cases = ReadCases(stream);
    }
    else
    {
        return 1;
    }

    for (int i = 0; i < cases.size(); i++)
    {
        std::cout << "Case #" << (i + 1) << ": " << std::endl;

        auto sol = Solve(cases[i]);

        if (!sol->result)
        {
            std::cout << "Impossible" << std::endl;;
        }
        else
        {
            PrintSolution(*sol);
        }
    }
}

