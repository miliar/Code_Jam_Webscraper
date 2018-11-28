#include <fstream>

int main()
{
    using namespace std;

    ifstream input("input.txt");
    ofstream output("output.txt");

    output.setf(std::ios::fixed, std::ios::floatfield);
    output.precision(8);

    unsigned int case_count;
    input >> case_count;

    for(unsigned int i = 0; i < case_count; ++i)
    {
        double farm_price, farm_rate, win_count;
        input >> farm_price >> farm_rate >> win_count;

        double current_rate = 2.0d;
        double total_time = 0.0d;

        while(win_count/current_rate >
               (win_count)/(current_rate + farm_rate) + farm_price/current_rate)
        {
            total_time += farm_price/current_rate;
            current_rate += farm_rate;
        }
        total_time += win_count/current_rate;

        output << "Case #" << i+1 << ": " << total_time << '\n';
    }
}
