#include<iostream>
#include<fstream>
#include<assert.h>
#include <sstream>
#include <vector>

int evaluateCase1(const std::vector< int >& aIntervalData, int& min_rate)
{
    int int_size = aIntervalData.size();
    int min_eaten = 0;
    min_rate = -1;
    int diff_consec = -1;
    for(int index =0; index < (int_size -1); index++)
    {
        diff_consec = aIntervalData[index] - aIntervalData[index +1];
        if (diff_consec >=0)
        {
            min_eaten += diff_consec;
            if(diff_consec > min_rate)
            {
                min_rate = diff_consec;
            }
        }

    }
    assert(min_eaten >=0);
    return min_eaten;
}


int evaluateCase2(const std::vector< int >& aIntervalData, int aMinRate)
{
    assert(aMinRate >= 0);
    int int_size = aIntervalData.size();
    int min_eaten = 0;
    int cur_eat_cnt = -1;
    for(int index =0; index < (int_size -1); index++)
    {
        if(aIntervalData[index] >= aMinRate)
        {
            cur_eat_cnt = aMinRate;
        }
        else
        {
            cur_eat_cnt = aIntervalData[index];
        }
        assert(aIntervalData[index] - cur_eat_cnt <= aIntervalData[index+1]);
        min_eaten += cur_eat_cnt;
    }
    return min_eaten;
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
            int prob_id = 1;
            getline(input_data, line);
            num_probs = atoi(line.c_str());
            int num_intervals = -1;
            while(getline(input_data, line))
            {
                std::stringstream prob_vars(line);
                prob_vars >> num_intervals;
                std::vector< int > mushroom_count_list;
                getline(input_data, line);
                std::stringstream interval_vars(line);
                int count_elem = -1;
                for(int index =0 ; index < num_intervals; index++)
                {
                    interval_vars >> count_elem;
                    mushroom_count_list.push_back(count_elem);
                }
                int min_rate = -1;
                int case1_min_count = evaluateCase1(mushroom_count_list, min_rate);
                output_file<<"Case #"<<prob_id<<": "<<case1_min_count;
                int case2_min_count = evaluateCase2(mushroom_count_list, min_rate);
                output_file<<" "<<case2_min_count<<std::endl;

                prob_id++;
            }
            assert(num_probs == prob_id -1);
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
