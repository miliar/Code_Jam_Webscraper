#include <iostream>
#include <string>
#include <vector>

struct TestCase
{
    int test_case_num;
    int max_shyness;
    std::vector<int> num_people_with_shyness;
    TestCase (int n): test_case_num(n) {}
};

void read_test_case (TestCase & tc)
{
    std::string audience;

    std::cin >> tc.max_shyness;
    std::cin >> audience;

    for (int i = 0; i <= tc.max_shyness; ++i)
        tc.num_people_with_shyness.push_back(audience[i] - '0');
}

void solve (const TestCase & tc)
{
    int num_friends = 0, total = 0;

    for (int i = 0; i <= tc.max_shyness; total += tc.num_people_with_shyness[i], ++i)
    {
        if (total < i)
        {
            num_friends += i - total;
            total = i;
        }
    }

    std::cout << "Case #" << tc.test_case_num << ": " << num_friends << std::endl;
}

int main (int argc, char * argv[])
{
    int T = 0;

    std::cin >> T;

    for (int i = 0; i < T; ++i)
    {
        TestCase tc(i + 1);
        read_test_case(tc);
        solve(tc);
    }

    return 0;
}
