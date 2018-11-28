#include <fstream>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int ovation()
{
    ifstream testcase("example.txt");
    ofstream result("result.out");

    int ncases;
    testcase >> ncases;

    for(int c = 0; c < ncases; ++c) {
        int standing = 0;
        int needed = 0;
        int smax;
        testcase >> smax;
        for(int i=0; i<=smax; ++i) {
            char c;
            testcase >> c;
            int nb = c-'0';
            if(i>standing) {
                needed += i-standing;
                standing += i-standing;
            }
            standing += nb;
        }
        result << "Case #" << c+1 << ": " << needed << endl;

    }
}

int ominoes()
{
    ifstream testcase("example.txt");
    ofstream result("result.out");

    int ncases;
    testcase >> ncases;

    for(int c = 0; c < ncases; ++c) {
        int X, R, C;
        testcase >> X >> R >> C;
        if(((R*C)%X) != 0) {
            result << "Case #" << c+1 << ": RICHARD" << endl;
        } else {
            //cerr << X  << " " << R << " " << C << endl;
            switch(X)
            {
                case 1:
                    result << "Case #" << c+1 << ": GABRIEL" << endl;
                    break;

                case 2:
                    result << "Case #" << c+1 << ": GABRIEL" << endl;
                    break;

                case 3:
                    if((R!=1 && C!=1)) {
                        result << "Case #" << c+1 << ": GABRIEL" << endl;
                    } else {
                        result << "Case #" << c+1 << ": RICHARD" << endl;
                    }
                    break;

                case 4:
                    if(R>2 && C>2)
                    {
                        result << "Case #" << c+1 << ": GABRIEL" << endl;

                    } else {
                        result << "Case #" << c+1 << ": RICHARD" << endl;
                    }
                    break;
            }
        }
    }
}

int lastyears()
{
    ifstream testcase("example.txt");
    ofstream result("result.out");

    int ncases;
    testcase >> ncases;

    for(int c = 0; c < ncases; ++c) {
        int D;
        testcase >> D;
        vector<int> pancakes;
        for(int i = 0; i < D ;++i)
        {
            int t;
            testcase >> t;
            pancakes.push_back(t);
        }
        int r = pancakes.size();
        int minutes = 0;
        while(r)
        {
            sort(pancakes.begin(), pancakes.end());
            int count = 0;
            while(pancakes[count]>=pancakes.front()/2 && count<pancakes.size()) ++count;
            if(pancakes.front()/2>count) {
                pancakes.push_back(pancakes.front()/2);
                pancakes[0] -= pancakes.front()/2;
            } else {
                r = 0;
                for(auto i = pancakes.begin(); i!=pancakes.end(); ++i)
                {
                    if(*i>0)
                    {
                        (*i)--;
                    }
                    if(*i>0)
                    {
                        ++r;
                    }
                }
            }
            ++minutes;
        }
        result << "Case #" << c+1 << ": " << minutes << endl;
    }
}

int sheep()
{
    ifstream testcase("example.txt");
    ofstream result("result.out");

    int ncases;
    testcase >> ncases;

    for(int c = 0; c < ncases; ++c) {
        unsigned long long N;
        testcase >> N;
        int digitcount[10];
        for(int i=0; i<10; ++i) {
            digitcount[i] = 0;
        }
        std::string outcome = "INSOMNIA";
        for(int t=0; t<100; ++t) {
            unsigned long long result = N * (t+1);
            do
            {
                digitcount[result%10]++;
                result /= 10;
            } while(result!=0);
            bool done = true;
            for(int i=0; i<10; ++i) {
                if(digitcount[i]==0) {
                    done = false;
                }
            }
            if(done) {
                char buf[256];
                sprintf(buf, "%llu", N*(t+1));
                outcome = buf;
                break;
            }
        }

        result << "Case #" << c+1 << ": " << outcome << endl;
    }
}

string inverted(const std::string& stack)
{
    string result;
    for(auto &c : stack)
    {
        if(c=='+') {
            result += '-';
        } else {
            result += '+';
        }
    }
    return result;
}

int flips(string stack)
{
    for(size_t i=0; i<stack.size(); ++i) {
        if(stack[i]=='-') {
            stack = stack.substr(i+1);
            string itmp = inverted(stack);
            return 1 + flips(itmp);
        }
    }
    return 0;
}

int main()
{
    ifstream testcase("example.txt");
    ofstream result("result.out");

    int ncases;
    testcase >> ncases;

    for(int c = 0; c < ncases; ++c) {
        std::string stack;
        testcase >> stack;
        std::reverse(stack.begin(), stack.end());
        result << "Case #" << c+1 << ": " << flips(stack) << endl;
    }
}
