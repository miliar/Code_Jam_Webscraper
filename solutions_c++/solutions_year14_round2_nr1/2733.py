#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <map>
#include <cmath>

std::string order;

// Assuming letter order equal
int calc_dist(const std::string & a, const std::string &b)
{
    std::vector<int> a_count(order.size(), 0);
    std::vector<int> b_count(order.size(), 0);

    int sindex = -1;
    char last = ' ';
    for (int i = 0; i < a.size(); i++)
    {
        if (a[i] != last)
        {
            sindex++;
            last = a[i];
        }

        a_count[sindex]++;
    }


    sindex = -1;
    last = ' ';
    for (int i = 0; i < b.size(); i++)
    {
        if (b[i] != last)
        {
            sindex++;
            last = b[i];
        }

        b_count[sindex]++;
    }

    int dis = 0;

    for (int i = 0; i < a_count.size(); i++)
    {
        dis += abs(a_count[i] - b_count[i]);
    }

    return dis;
}

int main()
{
    int T;

    std::cin >> T;

    for (int idx = 1; idx <= T; idx ++)
    {
        bool possible = true;
        int n, moves = 0;
        std::cin >> n;
        order = std::string();

        std::vector<std::string> values(n);

        // std::map<char, double> average_letter;

        std::vector<double> average_letter;
        for (int i = 0; i < n; i++)
        {
            std::cin >> values[i];
            const std::string & str = values[i];

            if (order.empty())
            {
                char last = ' ';
                for (int j = 0; j < str.size(); j++)
                {
                    if (str[j] != last)
                    {
                        order.push_back(str[j]);
                        average_letter.push_back(1);
                        last = str[j];
                    }
                    else
                    {
                        average_letter.back() += 1;
                    }
                }
            }
            else
            {
                int ord_idx = 0;
                int previous_count = 0;
                std::vector<bool> seen(order.size(), false);
                for (int j = 0; j < str.size(); j++)
                {
                    if (str[j] != order[ord_idx])
                    {
                        if (previous_count == 0)
                        {
                            possible = false;
                            break;
                        }

                        ord_idx++;

                        if (str[j] != order[ord_idx])
                        {
                            possible = false;
                            break;
                        }

                        seen[ord_idx] = true;
                        average_letter[ord_idx] += 1;
                        previous_count = 1;
                    }
                    else
                    {
                        seen[ord_idx] = true;
                        average_letter[ord_idx] += 1;
                        previous_count++;
                    }

                    // average_letter[str[j]] +=1;
                }

                for (int j = 0; j < seen.size(); j++)
                    if (!seen[j]) possible = false;
                if (!possible) break;
            }
        }

        if (possible)
        {
            int letters = 0;
            std::string word("");

            for (int i = 0; i < order.size(); i++)
            {
                average_letter[i] = ceil(average_letter[i]/values.size());
                // std::cout << order[i]  << " " << average_letter[i] << std::endl;
                word += std::string(average_letter[i] , order[i]);
            }
            
            // std::cout << word << std::endl;
            int mindis = 0;

            for (int i  = 0; i < values.size(); i++)
            {
                mindis += calc_dist(values[i], word);
            }

            std::vector<int> sumdis(values.size(), 0);
            for (int i  = 0; i < values.size(); i++)
            {
                for (int j = i + 1; j < values.size(); j++)
                {
                    int dis = calc_dist(values[i], values[j]);

                    sumdis[i] += dis;
                    sumdis[j] += dis;
                }

                if (sumdis[i] < mindis)
                {
                    mindis = sumdis[i];
                }
            }

            std::cout << "Case #"<< idx << ": " << mindis << std::endl;
        }
        else
        {
            std::cout << "Case #"<< idx << ": Fegla Won" << std::endl;
        }
    }

    return 0;
}