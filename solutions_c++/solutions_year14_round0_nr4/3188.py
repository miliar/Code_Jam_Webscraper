#include <fstream>
#include <vector>
#include <iterator>
#include <algorithm>
#include <functional>

template <typename Iterator>
unsigned int play_war(Iterator naomi_begin, Iterator naomi_end, Iterator ken_begin, Iterator ken_end)
{
    using namespace std;
    using std::placeholders::_1;

    sort(naomi_begin, naomi_end);
    sort(ken_begin, ken_end);

    auto naomi_current = naomi_begin;

    unsigned int score = 0;

    while(naomi_current != naomi_end)
    {
        auto ken_current = find_if(ken_begin, ken_end, bind(greater<double>(), _1, *naomi_current));
        if(ken_current == ken_end)
        {
            ken_current = ken_begin;
            ++score;
        }

        rotate(ken_current, ken_current+1, ken_end);
        --ken_end;

        ++naomi_current;
    }

    return score;
}

template <typename Iterator>
unsigned int play_deceitful_war(Iterator naomi_begin, Iterator naomi_end, Iterator ken_begin, Iterator ken_end)
{
    using namespace std;
    using std::placeholders::_1;

    sort(naomi_begin, naomi_end);
    sort(ken_begin, ken_end, greater_equal<double>());

    auto naomi_current = naomi_begin;

    unsigned int score = 0;

    while(distance(naomi_current, naomi_end) > 0)
    {
        auto ken_current = find_if(ken_begin, ken_end, bind(less<double>(), _1, *naomi_current));
        if(ken_current == ken_end)
        {
            ++ken_begin;
        }
        else
        {
            rotate(ken_current, ken_current+1, ken_end);
            --ken_end;
            ++score;
        }

        ++naomi_current;
    }

    return score;
}

int main()
{
    using namespace std;

    ifstream input("input.txt");
    ofstream output("output.txt");

    unsigned int case_count;
    input >> case_count;

    for(unsigned int i = 0; i < case_count; ++i)
    {
        unsigned int block_count;
        input >> block_count;

        vector<double> naomi(block_count), ken(block_count);

        copy_n(istream_iterator<double>(input), block_count, naomi.begin());
        copy_n(istream_iterator<double>(input), block_count, ken.begin());

        output << "Case #" << i+1 << ": ";
        output << play_deceitful_war(naomi.begin(), naomi.end(), ken.begin(), ken.end()) << ' ';
        output << play_war(naomi.begin(), naomi.end(), ken.begin(), ken.end()) << '\n';
    }
}
