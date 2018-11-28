#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <boost/algorithm/string.hpp>

using namespace boost::algorithm;
using namespace std;

void process(const int case_id, const int max_shy, const vector<int>& audiance)
{
    int cur_shy = 0;
    int index = 0;
    int friends = 0;
    for(vector<int>::const_iterator iter = audiance.begin();
        iter != audiance.end();
        ++iter)
    {
        if(index > cur_shy)
        {
            friends += (index - cur_shy);
            cur_shy += (index - cur_shy);
        }
        cur_shy += *iter;
        if(cur_shy >= max_shy)
            break;
        index++;
    }
    std::cout << "Case #" << case_id << ": " << friends << std::endl;
}

int main(int /*argc*/, char** argv)
{
    const string path = argv[1];
    ifstream file(path.c_str());
    string line;
    getline(file, line);
    const int cases = atoi(line.c_str());
    int case_id = 0;
    while(case_id++ < cases)
    {
        getline(file, line);

        vector<string> splitted(2);
        split(splitted, line, boost::is_any_of(" "));
        const int max_shy = atoi(splitted[0].c_str());
        vector<int> audiance;
        const string& part2 = splitted[1];
        for(string::const_iterator iter = part2.begin();
            iter != part2.end();
            ++iter)
        {
            int shy_count = *iter - '0';
            audiance.push_back(shy_count);
        }

        process(case_id, max_shy, audiance);
    }
    return 0;
}
