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
    vector<bool> pancakes;
    int moves = 0;
    bool top;
    State(const string & s){
        for (auto & c : s){
            pancakes.push_back(c == '+');
        };
        top = pancakes[0];
    };
    State (){};
    int search(){
        int i = 1;
        while (i < pancakes.size()){
            if (pancakes[i] != top){
                top = pancakes[i];
                moves++;
            };
            i++;
        };
        if (not top){
            moves++;
        };
    }
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
        state.search();
        o << "Case #" << k << ": " << state.moves << endl;
        k++;
    }

    return 0;
}

