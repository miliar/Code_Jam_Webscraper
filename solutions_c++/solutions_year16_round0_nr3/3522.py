#include <algorithm>
#include <iostream>
#include <iterator>
#include <fstream>
#include <queue>
#include <map>
#include <set>
#include <vector>

using namespace std;

struct Task
{
    int N;
    int J;
};

class PrimeCollection
{
public:
    PrimeCollection(uint64_t maxNumber)
    {
        GeneratePrimes(maxNumber);
    }

    bool IsPrime(uint64_t number)
    {
        for (auto prime : m_primes)
        {
            uint64_t maxP = static_cast<uint64_t>(sqrt(number));
            if (prime > maxP)
            {
                return true;
            }
            if (number % prime == 0)
            {
                return false;
            }
        }
        throw out_of_range("Out of bounds of primes");
    }

    set<uint64_t>* GetDividers(uint64_t number)
    {
        auto i = m_nonPrimeDividers.find(number);
        if (i != m_nonPrimeDividers.end())
        {
            return &(i->second);
        }
        uint64_t maxP = static_cast<uint64_t>(sqrt(number));
        set<uint64_t>* dividers = nullptr;
        for (auto prime : m_primes)
        {
            if (dividers == nullptr && prime > maxP)
            {
                break;
            }
            if (number % prime == 0)
            {
                if (dividers == nullptr)
                {
                    dividers = &(m_nonPrimeDividers.insert(make_pair(number, set<uint64_t>())).first->second);
                }
                dividers->insert(prime);
                do
                {
                    number /= prime;
                    auto i = m_nonPrimeDividers.find(number);
                    if (i != m_nonPrimeDividers.end())
                    {
                        dividers->insert(i->second.begin(), i->second.end());
                        number = 1;
                        break;
                    }
                } while (number % prime == 0);
                if (number == 1)
                {
                    break;
                }
            }
        }
        return dividers;
    }

    friend ostream& operator<<(ostream& os, const PrimeCollection& pc)
    {
        copy(pc.m_primes.begin(), pc.m_primes.end(), ostream_iterator<uint64_t>(os, " "));
        return os;
    }

private:
    void GeneratePrimes(uint64_t maxNumber)
    {
        uint64_t mx = static_cast<uint64_t>(sqrt(maxNumber));
        for (uint64_t p = 13; p < mx; p += 2)
        {
            uint64_t number = p;
            uint64_t maxP = static_cast<uint64_t>(sqrt(number));
            for (auto prime : m_primes)
            {
                if (prime > maxP)
                {
                    m_primes.insert(number);
                    break;
                }
                if (number % prime == 0)
                {
                    break;
                }
            }
        }
    }

private:
    set<uint64_t> m_primes = { 2, 3, 5, 7, 11 };
    map<uint64_t, set<uint64_t>> m_nonPrimeDividers;
};

class Part
{
private:
    bool m_keepMsb;
    bool m_keepLsb;
    vector<int> m_digits;

public:
    Part(int length, bool keepMsb, bool keepLsb)
        : m_keepMsb(keepMsb)
        , m_keepLsb(keepLsb)
    {
        m_digits.resize(length);
        Reset();
    }

    void Reset()
    {
        m_digits.assign(m_digits.size(), 0);
        if (m_keepMsb)
        {
            m_digits.front() = 1;
        }
        if (m_keepLsb)
        {
            m_digits.back() = 1;
        }
    }

    bool Increment()
    {
        int overflowFlag = m_digits.front();
        for (int i = static_cast<int>(m_digits.size()) - 1; i >= 0; --i)
        {
            m_digits[i] = 1 - m_digits[i];
            if (m_digits[i] == 1)
            {
                break;
            }
        }
        if (m_keepLsb)
        {
            m_digits.back() = 1;
        }
        if (overflowFlag == 1 && m_digits.front() == 0)
        {
            return false;
        }
        return true;
    }
    
    uint64_t GetRepresentation(int base)
    {
        uint64_t ret = 0;
        uint64_t multiplier = 1;
        for_each(m_digits.rbegin(), m_digits.rend(),
            [&](auto d)
            {
                ret += multiplier * d;
                multiplier *= base;
            });
        return ret;
    }

    friend ostream& operator<<(ostream& os, const Part& part)
    {
        for (auto n : part.m_digits)
        {
            os << n;
        }
        return os;
    }
};

class Number
{
public:
    Number(int N)
    {
        int length = N;
        if (N > 16)
        {
            length = N / 2;
            m_parts.push_back(Part(length, true, false));
            m_parts.push_back(Part(N - length, false, true));
        }
        else
        {
            m_parts.push_back(Part(length, true, true));
        }
    }

    void FindCoinJams(int J, PrimeCollection& pc, std::ostream& os)
    {
        Part& backPart = m_parts.back();
        while (J > 0)
        {
            vector<uint64_t> numberDiv;
            for (int i = 2; i <= 10; ++i)
            {
                uint64_t repb = backPart.GetRepresentation(i);
                set<uint64_t>* backDividers = pc.GetDividers(repb);
                if (backDividers == nullptr)
                {
                    break;
                }
                if (m_parts.size() == 1)
                {
                    numberDiv.push_back(*backDividers->begin());
                    continue;
                }

                Part& frontPart = m_parts.front();
                frontPart.Reset();
                while (true)
                {
                    uint64_t reph = frontPart.GetRepresentation(i);
                    set<uint64_t>* frontDividers = pc.GetDividers(reph);
                    if (frontDividers != nullptr)
                    {
                        vector<uint64_t> out;
                        set_intersection(backDividers->begin(), backDividers->end(), frontDividers->begin(), frontDividers->end(), std::back_inserter(out));
                        if (!out.empty())
                        {
                            numberDiv.push_back(out.front());
                            break;
                        }
                    }
                    if (!frontPart.Increment())
                    {
                        break;
                    }
                }
            }
            if (numberDiv.size() == 9)
            {
                --J;
                os << *this << " ";
                copy(numberDiv.begin(), numberDiv.end(), ostream_iterator<uint64_t>(os, " "));
                os << endl;
            }
            backPart.Increment();
        }
    }

    void Increment(int partIndex)
    {
        m_parts[partIndex].Increment();
    }

    friend ostream& operator<<(ostream& os, const Number& number)
    {
        for (auto part : number.m_parts)
        {
            os << part;
        }
        return os;
    }

private:
    vector<Part> m_parts;
};

vector<Task> ReadTasks(istream& is)
{
    size_t taskCount;
    is >> taskCount;
    vector<Task> tasks;
    while (taskCount-- > 0)
    {
        int N, J;
        is >> N >> J;
        tasks.push_back(Task{ N, J });
    }
    return move(tasks);
}

int main(int args, char** argv)
{
    ifstream input("input.txt");
    vector<Task> tasks = ReadTasks(input);

    ofstream out("output.txt");

    PrimeCollection primeCollection(static_cast<uint64_t>(111111111111L));
    for (size_t i = 0; i < tasks.size(); ++i)
    {
        Number number(tasks[i].N);
        out << "Case #" << i + 1 << ":" << endl;
        number.FindCoinJams(tasks[i].J, primeCollection, out);
        out << endl;
    }
    return 0;
}
