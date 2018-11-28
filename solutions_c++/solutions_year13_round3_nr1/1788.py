//============================================================================
// Name        : Consonants.cpp
// Author      : Kenji.K
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <cstdlib>
#include <cassert>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <map>
#include <set>
#include <iterator>
#include <stack>
#include <queue>
#include <stdexcept>
#include <algorithm>
#include <boost/program_options.hpp>
#include <boost/foreach.hpp>
#include <boost/algorithm/string.hpp>
#include <boost/phoenix/core.hpp>
#include <boost/phoenix/operator.hpp>
#include <boost/phoenix/statement.hpp>
#include <boost/lexical_cast.hpp>
#include <boost/tuple/tuple.hpp>
//#include <boost/multi_array.hpp>
//#include <boost/rational.hpp>
//#include <boost/tokenizer.hpp>
#include <boost/multiprecision/cpp_int.hpp>
//#include <boost/multiprecision/cpp_dec_float.hpp>

namespace po = boost::program_options;
using boost::phoenix::val;
using boost::phoenix::ref;
using boost::phoenix::cref;
using boost::phoenix::switch_;
using boost::phoenix::case_;
using boost::phoenix::default_;
using boost::phoenix::arg_names::arg1;
using boost::phoenix::arg_names::arg2;
using std::endl;
using std::cout;
using std::cerr;
using std::vector;
using std::string;
using boost::tuple;
using boost::make_tuple;
//using boost::rational;
using boost::multiprecision::cpp_int;

struct P {
    string name;
    int n;
};

/*
struct A {
};
*/

typedef std::vector<P> Ps;
typedef std::vector<cpp_int> As;

/*Prototype of functions*/
int parse_options(int, char*[], po::variables_map&);
void parse_problems(std::istream&, Ps&);
void solve_problems(const Ps&, As&);
void write_answers(const As&, const std::string&);

int main(int ac, char* av[]) {
    po::variables_map vm;
    try {
        if (parse_options(ac, av, vm) != 0)
            exit(0);
        std::ifstream ifs(vm["input"].as<std::string>().c_str());
        Ps plb;
        As ans;
        //parse problems
        try {
            parse_problems(ifs, plb);
        } catch (boost::bad_lexical_cast& e) {
            std::cout << e.what() << std::endl;
            std::cout << "problem parse is failed!" << std::endl;
            throw;
        }
        //solve problems
        solve_problems(plb, ans);
        //output answers
        write_answers(ans, vm["output"].as<std::string>());
    } catch (std::exception& e) {
        std::cerr << e.what() << std::endl;
        return -1;
    } catch (...) {
        std::cerr << "Unexpected Error!" << std::endl;
        return -1;
    }
    return 0;
}

void parse_problems(std::istream& ifs, Ps& probs) {
    using boost::algorithm::split;
    using boost::algorithm::trim_if;
    using boost::algorithm::is_any_of;
    using boost::lexical_cast;

    string buf;
    int num_case = 0;
    if (ifs.good()) {
        getline(ifs, buf);
        trim_if(buf, is_any_of(" \n\r"));
        num_case = lexical_cast<int>(buf);
    }
    cout << num_case << " test cases" << endl;
    for (int i = 0; i < num_case; ++i) {
        getline(ifs, buf);
        vector<string> tmp;
        split(tmp, buf, is_any_of(" \n\r"), boost::algorithm::token_compress_on);
        if (tmp.size() != 2) break;

        P prob;
        prob.name = tmp[0];
        prob.n = lexical_cast<int>(tmp[1]);
        probs.push_back(prob);
    }

    return;
}

void solve_problems(const Ps& probs, As& ans) {
    using namespace boost::multiprecision;
    BOOST_FOREACH(const P& p, probs) {
        cout << p.name << endl;
        int length = p.name.length();
        int n_value(0);
        for (int start = 0; start < length; ++start) {
            for (int end = start + 1; end < length + 1; ++end) {
                string sub = p.name.substr(start, end - start);
                int sub_l = sub.length();
                int cconsonants(0);
                for (int i = 0; i < sub_l; ++i) {
                    if (sub[i] == 'a' || sub[i] == 'e' ||
                        sub[i] == 'i' || sub[i] == 'o' ||
                        sub[i] == 'u'  ) {
                        cconsonants = 0;
                        continue;
                    } else {
                        ++cconsonants;
                        if (cconsonants >= p.n) {
                            ++n_value;
                            break;
                        }
                    }
                }

            }
        }
        ans.push_back(n_value);
    }
    return;
}

void write_answers(const As& ans, const std::string& filename) {
    int num = 0;
    std::ofstream ofs(filename.c_str());
    std::for_each(ans.begin(), ans.end(),
            ofs << cref("Case #")
                << ++val(num)
                << ": "
                << arg1
                << std::endl);
    return;
}

int parse_options(int ac, char* av[], po::variables_map& vm) {
    po::options_description desc("Allowed options");
    desc.add_options()
            ("help,h", "produce help message")
            ("input,i", po::value<std::string>(), "set input file name")
            ("output,o", po::value<std::string>()->default_value("output.txt"), "set output file name")
        ;
    po::positional_options_description pos_op;
    pos_op.add("input", 1).add("output", 1);
    po::store(
            po::command_line_parser(ac, av)
                .options(desc)
                .positional(pos_op)
                .run(),
            vm);
    po::notify(vm);
    if (vm.count("help")) {
        std::cout << desc << std::endl;
        return -1;
    }
    return 0;
}
