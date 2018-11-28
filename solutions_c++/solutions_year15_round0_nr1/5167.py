#include<iostream>
#include<fstream>
#include<assert.h>
#include <sstream>

int findNumFriendsRequired(std::string& aProblemString)
{
    int friends_required = 0;
    std::stringstream prob_str(aProblemString);
    int max_shy_index = -1;
    prob_str >> max_shy_index;
    char temp;
    prob_str.get(temp);//expel space
    int cur_standing_people = 0;
    int inp_data[max_shy_index +1];
    for (int index=0; index<= max_shy_index; index++)
    {
        prob_str.get(temp);
        inp_data[index] = temp - '0';

        if (cur_standing_people < index)
        {
            int deficiency = index - cur_standing_people;
            for (int def_i=0; def_i< index; def_i++)
            {
                if (deficiency == 0)
                {
                    break;
                }
                int cur_cap = 9 - inp_data[def_i];
                if (cur_cap > deficiency)
                {
                    friends_required += deficiency;
                    inp_data[def_i] += deficiency;
                    cur_standing_people += deficiency;
                    deficiency = 0;
                }
                else
                {
                    friends_required += cur_cap;
                    inp_data[def_i] += cur_cap;
                    assert(inp_data[def_i] <= 9);
                    cur_standing_people += cur_cap;
                    deficiency -= cur_cap;
                }
                assert(deficiency >=0);
            }
        }
        cur_standing_people += inp_data[index];
    }
    return friends_required;
}

int main(int argc, char* argv[])
{
    using namespace std;

    if (argc > 1)
    {
        std::ifstream input_data(argv[1]);
        std::ofstream output_file(std::string("out_")+argv[1]);
        int num_probs = -1;
        std::string line;

        if (input_data.is_open())
        {
            int line_count = 0;
            while(getline(input_data, line))
            {
                if (num_probs == -1)
                {
                    num_probs = atoi(line.c_str());
                }
                else
                {
                    int num_friends_req = findNumFriendsRequired(line);
                    output_file<<"Case #"<<line_count<<": "<<num_friends_req<<std::endl;
                }
                line_count++;
            }
        }
        else
        {
            std::cerr<<"Cannot open input file: "<<argv[1]<<std::endl;
        }
    }
    else
    {
        std::cerr<<"File path to input data is mandatory input!"<<std::endl;
    }

}
