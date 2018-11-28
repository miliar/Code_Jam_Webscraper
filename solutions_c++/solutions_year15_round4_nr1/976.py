#include <cassert>
#include <fstream>
#include <iostream>
#include <vector>


template <class T>
class Matrix {
public:
    Matrix(int n, int m, const T& default_value = T())
      : size_n_(n)
      , size_m_(m)
      , elements_(n * m, default_value)
    { }

    int SizeN() const
    {
        return size_n_;
    }

    int SizeM() const
    {
        return size_m_;
    }

    const T& operator() (int i, int j) const
    {
        assert (0 <= i && i < size_n_ && 0 <= j && j < size_m_);
        return elements_.at(i * size_m_ + j);
    }

    T& operator() (int i, int j)
    {
        assert (0 <= i && i < size_n_ && 0 <= j && j < size_m_);
        return elements_.at(i * size_m_ + j);
    }
    
private:
    int size_n_;
    int size_m_;
    std::vector<T> elements_;
};


template <class T>
std::ostream& operator<< (std::ostream& ostream, const Matrix<T>& matrix)
{
    std::cout << matrix.SizeN() << ' ' << matrix.SizeM() << '\n';
    for (int i = matrix.SizeN() - 1; i >= 0; --i) {
        for (int j = 0; j < matrix.SizeM(); ++j) {
            ostream << matrix(i, j);
        }
        ostream << '\n';
    }
    return ostream;
}


template <class T>
Matrix<T> Rotate(const Matrix<T>& input)
{
    Matrix<T> result(input.SizeM(), input.SizeN());
    for (int i = 0; i < input.SizeN(); ++i) {
        for (int j = 0; j < input.SizeM(); ++j) {
            result(j, input.SizeN() - 1 - i) = input(i, j);
        }
    }
    return result;
}

template <class T, class Func>
Matrix<T> Map(const Matrix<T>& input, Func func)
{
    Matrix<T> result(input.SizeN(), input.SizeM());
    for (int i = 0; i < input.SizeN(); ++i) {
        for (int j = 0; j < input.SizeM(); ++j) {
            result(i, j) = func(input(i, j));
        }
    }
    return result;
}


enum Action : uint8_t {
    None = 0,
    East = 1,
    North = 2,
    West = 4,
    South = 8
};

int RotateActions(int actions)
{
    return ((actions << 1) | (actions >> 3)) & 0xf;
}

Action RotateAction(Action action)
{
    return (Action) RotateActions((int)action);
}

template <class T>
Matrix<T> RotateActionMap(const Matrix<T>& action_map)
{
    return Map(Rotate(action_map), RotateAction);
}

std::ostream& operator<< (std::ostream& ostream, Action action)
{
    switch (action) {
    case Action::None: return ostream << '.';
    case Action::East: return ostream << '>';
    case Action::North: return ostream << '^';
    case Action::West: return ostream << '<';
    case Action::South: return ostream << 'v';
    }
    throw std::runtime_error("Unknown action type.");
}

Matrix<Action> ReadActionMap(std::istream* istream)
{
    int n, m;
    *istream >> n >> m;
    Matrix<Action> result(n, m);
    std::string line;
    for (int i = n - 1; i >= 0; --i) {
        *istream >> line;
        for (int j = 0; j < m; ++j) {
            switch (line.at(j)) {
            case '.': result(i, j) = Action::None; break;
            case '>': result(i, j) = Action::East; break;
            case '^': result(i, j) = Action::North; break;
            case '<': result(i, j) = Action::West; break;
            case 'v': result(i, j) = Action::South; break;
            default: throw std::runtime_error("Unknown action mark.");
            }
        }
    }
    return result;
}

void UpdateAllowMapSouth(const Matrix<Action>& action_map, Matrix<int>* allow_map)
{
    for (int i = 0; i < action_map.SizeN(); ++i) {
        for (int j = 0; j < action_map.SizeM(); ++j) {
            if (action_map(i, j) != Action::None) {
                (*allow_map)(i, j) &= ~(int) Action::West;
                break;
            }
        }
    }
}


int FixActionMap(Matrix<Action> action_map)
{
    Matrix<int> allow_map(action_map.SizeN(), action_map.SizeM(), 0xf);

    UpdateAllowMapSouth(action_map, &allow_map);
    action_map = Map(Rotate(action_map), RotateAction);
    allow_map = Map(Rotate(allow_map), RotateActions);

    UpdateAllowMapSouth(action_map, &allow_map);
    action_map = Map(Rotate(action_map), RotateAction);
    allow_map = Map(Rotate(allow_map), RotateActions);

    UpdateAllowMapSouth(action_map, &allow_map);
    action_map = Map(Rotate(action_map), RotateAction);
    allow_map = Map(Rotate(allow_map), RotateActions);

    UpdateAllowMapSouth(action_map, &allow_map);
    action_map = Map(Rotate(action_map), RotateAction);
    allow_map = Map(Rotate(allow_map), RotateActions);

    int result = 0;
    for (int i = 0; i < allow_map.SizeN(); ++i) {
        for (int j = 0; j < allow_map.SizeM(); ++j) {
            if (allow_map(i, j) == 0) {
                return -1;
            }
            if (action_map(i, j) != Action::None &&
                (allow_map(i, j) & (int)action_map(i, j)) != (int)action_map(i, j)) {
                result += 1;
            }
        }
    }
    return result;
}


int main()
{
    //std::ifstream ifstream("input.txt");
    std::istream& istream = std::cin;

    int number_of_cases;
    istream >> number_of_cases;
    for (int case_no = 1; case_no <= number_of_cases; ++case_no) {
        const auto action_map = ReadActionMap(&istream);
        const int number_of_changes = FixActionMap(action_map);
        std::cout << "Case #" << case_no << ": ";
        if (number_of_changes < 0) {
            std::cout << "IMPOSSIBLE\n";
        } else {
            std::cout << number_of_changes << '\n';
        }
    }
    return 0;
}
