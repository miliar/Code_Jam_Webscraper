#include <basic.h>

struct V
{
    int sign;
    char c;
    V (int sign, char c)
        : sign(sign)
        , c(c)
    {}
    V operator*(V const& rhs)
    {
        int newSign = sign * rhs.sign;
        if (rhs.c == '1')
        {
            return V(newSign, c);
        }
        if (c == rhs.c)
        {
            return V(-newSign, '1');
        }

        switch(c)
        {
            case '1':
                return V(newSign, rhs.c);
            case 'i':
                if (rhs.c == 'j')
                {
                    return V(newSign, 'k');
                }
                else
                {
                    return V(-newSign, 'j');
                }
            case 'j':
                if (rhs.c == 'i')
                {
                    return V(-newSign, 'k');
                }
                else
                {
                    return V(newSign, 'i');
                }
            case 'k':
                if (rhs.c == 'i')
                {
                    return V(newSign, 'j');
                }
                else
                {
                    return V(-newSign, 'i');
                }
        }
    }
};

bool operator==(V const& lhs, V const& rhs)
{
    return lhs.sign == rhs.sign && lhs.c == rhs.c;
}
bool operator!=(V const& lhs, V const& rhs)
{
    return !(lhs == rhs);
}

std::ostream & operator<<(std::ostream & os, V const& rhs)
{
    if (rhs.sign == -1)
    {
        os << '-';
    }
    os << rhs.c;
    return os;
}

V I(1, 'i');
V J(1, 'j');
V K(1, 'k');

int main(int argc, char * argv[])
{
    int T;
    std::cin >> T;
    for (size_t t = 0; t != T; ++t)
    {
        std::cout << "Case #" << t + 1 << ": ";
        int L, X;
        std::cin >> L >> X;
        while (X >= 16)
        {
            X -= 4;
        }

        std::string str;
        std::cin >> str;
        std::ostringstream oss;
        for (size_t x = 0; x != X; ++x)
        {
            oss << str;
        }
        str = oss.str();

        bool yes(false);
        V ci(1, '1');
        for (size_t i = 0; !yes && i != str.size() - 2; ++i)
        {
            ci = ci * V(1, str[i]);
            if (ci != I)
            {
                continue;
            }
            V ck(1, '1');
            for (size_t k = i + 1; k != str.size(); ++k)
            {
                ck = ck * V(1, str[k]);
            }
            V cj(1, '1');
            for (size_t j = i + 1; !yes && j != str.size() - 1; ++j)
            {
                cj = cj * V(1, str[j]);
                ck = ck * V(1, str[j]);
                if (cj == J && ck == K)
                {
                    yes = true;
                }
                //std::cout << ci << ' ' << cj << ' ' << ck << std::endl;
            }
        }
        if (yes)
        {
            std::cout << "YES" << std::endl;
        }
        else
        {
            std::cout << "NO" << std::endl;
        }
    }
    return 0;
}

