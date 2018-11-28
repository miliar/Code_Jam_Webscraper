#include <iostream>
#include <vector>
#include <array>
#include <cmath>

std::vector<std::string> read_strings(int how_many)
{
    std::vector<std::string> result;
    result.reserve(how_many);
    for (int i = 0; i < how_many; i++)
    {
        std::string s;
        std::getline(std::cin, s);
        result.push_back(s);
    }
    return result;
}

std::string remove_duplicates(std::string s)
{
    char prev;
    bool first = true;
    std::string s_new;
    for (char c : s)
    {
        if (first || c != prev)
        {
            s_new.push_back(c);
            prev = c;
        }
        first = false;
    }
    return s_new;     
}

bool is_possible(std::vector<std::string> strings)
{
    for (std::string& s : strings)
        s = remove_duplicates(s);
    for (int i = 1; i < (int)strings.size(); i++)
    {
        if (strings[i] != strings[0])
            return false;
    }
    return true;
}


std::vector<int> get_counters(const std::string& s)
{
    std::vector<int> result;
    char prev;
    bool first = true;
    int counter = 0;
    for (char c : s)
    {
        if (first || c == prev)
        {
            counter++;
        }
        else
        {
            result.push_back(counter);
            counter = 1;
        }
        prev = c;
        first = false;
    }
    result.push_back(counter);
    return result; 
}

std::vector<std::vector<int> > get_counters(const std::vector<std::string>& strings)
{
    std::vector<std::vector<int> > result;
    for (const std::string& s : strings)
    {
        std::vector<int> elem = get_counters(s);
        result.push_back(elem);
    }
    return result;
}

std::vector<int> get_averages(const std::vector<std::vector<int> >& counters)
{
    const int n = counters[0].size();
    std::vector<int> result(n);
    for (int i = 0; i < n; i++)
    {
        int accum = 0;
        for (const std::vector<int>& counter : counters)
        {
            accum += counter[i];
        }
        result[i] = (int)floor( (double)accum / counters.size() );
    }
    return result;
}

std::vector<int> get_differences(const std::vector<int>& counter, const std::vector<int>& averages)
{
    std::vector<int> result(counter.size());
    for (int i = 0; i < (int)counter.size(); i++)
    {
        result[i] = abs(counter[i] - averages[i]);
    }
    return result;
}

std::vector<std::vector<int> > get_differences(const std::vector<std::vector<int> >& counters, const std::vector<int>& averages)
{
    std::vector<std::vector<int> > result;
    for (const std::vector<int>& counter : counters)
    {
        result.push_back(get_differences(counter, averages));
    }
    return result;
}

int get_total_steps(const std::vector<std::vector<int> >& differences)
{
    int accum = 0;
    for (const std::vector<int>& row : differences)
    {
        for (int elem : row)
        {
            accum += elem;
        }
    }
    return accum;
}

int main()
{

    // Read the number of test cases
    int no_test_cases;
    std::cin >> no_test_cases;
    std::cin.ignore(1, '\n');
    
    // Debug
    //std::cout << no_test_cases << std::endl;
    
    for (int i = 1; i <= no_test_cases; i++)
    {
    
        // Read number of strings
        int no_strings;
        std::cin >> no_strings;
        std::cin.ignore(1, '\n');
        
        // Debug
        //std::cout << no_strings << std::endl;
        
        std::vector<std::string> strings = read_strings(no_strings);
        
        // Debug
        //for (std::string& s : strings)
        //{
        //    std::cout << s << std::endl;
        //}
    
        std::cout << "Case #" << i << ": ";
    
        const bool possible = is_possible(strings);
        // Debug
        //std::cout << possible << std::endl;
        if (!possible)
        {
            std::cout << "Fegla Won" << std::endl;
        }
        else
        {
            const std::vector<std::vector<int> > counters = get_counters(strings);
            const std::vector<int> averages = get_averages(counters);
            const std::vector<std::vector<int> > differences = get_differences(counters, averages);
            const int total_steps = get_total_steps(differences);
            std::cout << total_steps << std::endl;
        }
                    
    }
    
    return 0;
    
}
