#include <iostream>

#include <fstream>
#include <string>

#include "iostream"
#include "stdlib.h"
#include "stdio.h"
#include "boost/date_time.hpp"
#include <cstdio>
#include <ctime>
#include "boost/regex.hpp"
#include <boost/algorithm/string/compare.hpp>
#include <boost/algorithm/string/join.hpp>
#include <boost/algorithm/string/regex.hpp>
#include <boost/algorithm/string/split.hpp>
#include <boost/algorithm/string.hpp>
#include <boost/range/irange.hpp>
#include "boost/thread.hpp"
#include <fstream>
#include <string>
#include <cerrno>
#include <sys/types.h>
#include <iso646.h>
#include <boost/asio.hpp>
#include <boost/optional.hpp>
#include <boost/optional/optional_io.hpp>
#include <cerrno>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <boost/algorithm/string/join.hpp>
#include <boost/range/adaptor/transformed.hpp>
#include <stack>

using namespace std;

using boost::optional;
using namespace std;
using boost::lexical_cast;
using boost::irange;
using boost::posix_time::ptime;
using boost::thread;


class State{
public:
    int N;
    State(){};
    State(const string & s){
        N = lexical_cast<int> (s);
    };
    set<int> seen;

};


deque<int> extract(int number){
    deque<int> sd;

    while (number > 0)
    {
        int digit = number%10;
        number /= 10;
        sd.push_back(digit);
    }
    return sd;
};


string search(State & state0){

    if (state0.N == 0){
        return "INSOMNIA";
    }

    int i = 1;
    while (state0.seen.size() != 10) {
        auto sd = extract(state0.N * i);
        while (!sd.empty()) {
            state0.seen.insert(sd.front());
            sd.pop_front();
        };
        i++;
    };
    return lexical_cast<string>(state0.N * (i-1));
};



int main()
{
    ifstream file("/Users/vivanov/ClionProjects/code_jam2016/t.txt");
    string s;
    vector<State> states;
    int i = 0;
    while (getline(file, s))
    {

        if (i==0){
            states = vector<State>(lexical_cast<int>(s));
        }
        else {
            auto state = State(s);
            states[i-1] = State(state);
        }
        i++;
    };
    ofstream o("/Users/vivanov/ClionProjects/code_jam2016/o.txt");
    int k = 1;
    for (auto & state: states){
        o << "Case #" << k << ": " << search(state) << endl;
        k++;
    }

    return 0;
}

