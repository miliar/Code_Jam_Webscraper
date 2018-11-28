#include <iostream>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <algorithm>
#include <cassert>
using namespace std;


class Quat
{
public:
    enum Value
    {
        I, J, K, One
    };

    bool neg;
    Value v;
    
public:
    Quat() : neg(false), v(One)
    { }
    Quat(Value v) : neg(false), v(v)
    { }

    Quat(bool neg, Value v) : neg(neg), v(v)
    { }

    Quat& operator*=(const Quat& q)
    {
        if (q.neg)
            neg = !neg;

        switch(v)
        {
        case One:
            v = q.v;
            break;
        case I:
            switch(q.v)
            {
            case One: v = I;   break;
            case I:   v = One; neg = !neg; break;
            case J:   v = K;   break;
            case K:   v = J;   neg = !neg; break;
            }
            break;
        case J:
            switch(q.v)
            {
            case One: v = J;   break;
            case I:   v = K;   neg = !neg; break;
            case J:   v = One; neg = !neg; break;
            case K:   v = I;   break;
            }
            break;
        case K:
            switch(q.v)
            {
            case One: v = K;   break;
            case I:   v = J;   break;
            case J:   v = I;   neg = !neg; break;
            case K:   v = One; neg = !neg; break;
            }
            break;
        }

        return *this;
    }

    Quat operator*(const Quat& q)
    {
        Quat r(*this);
        r *= q;
        return r;
    }

    bool operator==(const Quat& q) const
    {
        return neg == q.neg && v == q.v;
    }

    Quat inverse() const
    {
        if (v == One)
            return Quat(neg, v);
        else
            return Quat(!neg, v);
    }
};

ostream& operator<<(ostream& out, const Quat& q)
{
    if (q.neg) out << '-';
    if (q.v == Quat::One) out << '1';
    if (q.v == Quat::I) out << 'i';
    if (q.v == Quat::J) out << 'j';
    if (q.v == Quat::K) out << 'k';
    return out;
}

const Quat One(Quat::One);
const Quat I(Quat::I);
const Quat J(Quat::J);
const Quat K(Quat::K);

class Solve
{
public:
    void solve()
    {
        size_t L, X; cin >> L >> X;
        vector<Quat> ls;
        
        for (size_t i = 0; i < L; ++i)
        {
            char c; cin >> c;
            if(c == 'i')
                ls.emplace_back(I);
            else if(c == 'j')
                ls.emplace_back(J);
            else if(c == 'k')
                ls.emplace_back(K);
            else
                assert(false);
        }

        vector<Quat> s;

        for (size_t i = 0; i < X; ++i)
        {
            copy(begin(ls), end(ls), back_inserter(s));
        }
        
        Quat left;

        for (size_t i = 0; i < L * X - 2; ++i)
        {
            left *= s[i];

            if (left == I)
            {
                Quat middle;
                Quat right;

                for (size_t j = i+1; j < L * X; ++j)
                {
                    right *= s[j];
                }

                for (size_t j = i+1; j < L * X - 1; ++j)
                {
                    middle *= s[j];
                    right = s[j].inverse() * right;

                    if (middle == J && right == K)
                    {
                        cout << "YES"; return;
                    }
                }
            }
        }

        cout << "NO";
    }
};

int main()
{
	size_t n;
	std::cin >> n;
	while(std::cin.get() != '\n');
	for(size_t i=1; i <= n; i++)
	{
		std::cout << "Case #" << i << ": ";
        Solve s;
		s.solve();
		std::cout << std::endl;
	}
}
