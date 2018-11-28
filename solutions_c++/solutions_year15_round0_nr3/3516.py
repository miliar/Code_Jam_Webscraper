#include<iostream>
#include<fstream>
#include<assert.h>
#include <sstream>
#include <vector>

int getPartResult(std::vector<int>& aTempResult, std::string& aPattern, int (*aLookUpTable)[5][5], int aNegIndex)
{
    assert(aNegIndex < aPattern.size());
    if (aTempResult.size() <= aNegIndex)
    {
        for(int index = aTempResult.size(); index <= aNegIndex; index++)
        {
            int neg_index = aPattern.size() -1 - index;
            assert(neg_index >= 0);
            assert(neg_index < aPattern.size());
            int cur_elem = aPattern[neg_index] - 'i' +2;
            if (index == 0)
            {
                aTempResult.push_back(cur_elem);
            }
            else
            {
                assert(aTempResult.size() > index-1);
                int pre_res = aTempResult[index-1];
                bool pre_neg = false;
                if (pre_res <0 )
                {
                    pre_neg = true;
                    pre_res = -1* pre_res;
                }
                int cur_res =((*aLookUpTable)[cur_elem][pre_res]);
                if (pre_neg)
                {
                    cur_res = -1* cur_res;
                }
                aTempResult.push_back(cur_res);
            }
        }
    }
    assert(aNegIndex < aTempResult.size());
    return aTempResult[aNegIndex];
}

int splitPossible(int aPatternSize, int aPatternRepCount, std::ifstream& aPattern, int (*aLookUpTable)[5][5])
{
    std::vector<int> int_result;
    std::string pattern;
    getline(aPattern, pattern);

    std::vector<std::pair< int, int> > index_stack;
    int cur_val = 1;
    bool cur_val_neg = false;
    int new_val = 0;
    int cur_stack_elem = 2;
    int patt_index = 0;
    int loop_result = -1;
    for(int pat_rep_index = 1; pat_rep_index <= aPatternRepCount; )
    {
        for(  ;patt_index< aPatternSize; )
        {
            if (index_stack.size() == 2)
            {
                int sec_part_res = getPartResult(int_result, pattern, aLookUpTable, aPatternSize-1-patt_index);
                bool sec_neg = false;
                if(sec_part_res < 0 )
                {
                    sec_neg = true;
                    sec_part_res = -1* sec_part_res;
                }
                cur_val = (*aLookUpTable)[cur_val][sec_part_res];
                if (sec_neg)
                {
                    cur_val = -1*cur_val;
                }
                if (cur_val < 0)
                {
                    cur_val_neg = !cur_val_neg;
                    cur_val = -1* cur_val;
                }
                patt_index = aPatternSize-1;
            }
            else{
                new_val = pattern[patt_index] -'i' +2;
                assert (new_val > 0);
                cur_val = (*aLookUpTable)[cur_val][new_val];
                if (cur_val < 0)
                {
                    cur_val_neg = !cur_val_neg;
                    cur_val = -1* cur_val;
                }
                if (cur_val == cur_stack_elem && !cur_val_neg)
                {
                    if (index_stack.size() < 2)
                    {
                        index_stack.push_back(std::make_pair(pat_rep_index, patt_index));
                        cur_val = 1;
                        cur_val_neg = false;
                        cur_stack_elem++;
                    }
                }
            }


            if ((patt_index == (aPatternSize -1)) &&(pat_rep_index == aPatternRepCount))
            {
                if (index_stack.size() == 2)
                {
                    if (!cur_val_neg && cur_val == cur_stack_elem)
                    {
                        index_stack.push_back(std::make_pair(pat_rep_index, patt_index));
                        cur_val = 1;
                        cur_val_neg = false;
                        cur_stack_elem++;
                        break;
                    }
                }
            }
            patt_index++;
       }
        if (index_stack.size() == 3)
        {
            break;
        }
        if(pat_rep_index == aPatternRepCount)
        {
            if (index_stack.size() > 0)
            {
                std::pair<int, int> val = index_stack.back();
                index_stack.pop_back();
                pat_rep_index = val.first-1;
                patt_index = val.second+1; 
                cur_stack_elem--;
                cur_val = cur_stack_elem;
                cur_val_neg = false;
            }

        }
        else
        {
            patt_index = 0;
        }
        pat_rep_index++;
    }
    if (index_stack.size() == 3)
    {
        /*
        std::cout<<index_stack[0].second<<"-"<<index_stack[0].first<<" : "
            <<index_stack[1].second<<"-"<<index_stack[1].first<< " : "
            <<index_stack[2].second<<"-"<<index_stack[2].first<<std::endl;
            */
        return true;
    }
    else
    {
        return false;
    }
}

int main(int argc, char* argv[])
{
    using namespace std;
    int look_up_table[5][5] =  
    {0, 1, 2, 3, 4,
    1, 1, 2, 3, 4,
    2, 2, -1, 4, -3,
    3, 3, -4, -1, 2,
    4, 4, 3, -2, -1}; 

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
            int size_pattern = -1;
            int pattern_repet_count = -1;
            while(getline(input_data, line))
            {
                std::stringstream prob_vars(line);
                prob_vars >> size_pattern >> pattern_repet_count;
                bool split_possibility = splitPossible(size_pattern, pattern_repet_count, input_data, &look_up_table);
                if (split_possibility)
                {
                    output_file<<"Case #"<<prob_id<<": "<<"YES"<<std::endl;
                }
                else
                {
                    output_file<<"Case #"<<prob_id<<": "<<"NO"<<std::endl;
                }
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
