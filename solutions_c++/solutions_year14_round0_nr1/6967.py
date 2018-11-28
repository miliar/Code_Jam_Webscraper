#include <iostream>
#include <set>
#include <vector>
#include <fstream>
#include <algorithm>

typedef std::set<unsigned int> Row;
typedef std::vector<Row> Arrangement;

Arrangement readArrangement (std::ifstream& stream)
{
    Arrangement arr;
    for (int j = 0; j < 4; ++j)
    {
        Row r;
        int a, b, c, d;
        stream >> a >> b >> c >> d;
        r.insert(a);
        r.insert(b);
        r.insert(c);
        r.insert(d);
        arr.push_back(r);
    }
    return arr;
}

void validateTestCase(std::ifstream& stream, std::ofstream& out, int num)
{
    int fa;
    stream >> fa;
    Arrangement f_arr = readArrangement(stream);
    int sa;
    stream >> sa;
    Arrangement s_arr = readArrangement(stream);

    std::set<int> inter;
    std::set_intersection(f_arr[fa-1].begin(), f_arr[fa-1].end(),s_arr[sa-1].begin(), s_arr[sa-1].end(),
            std::inserter( inter, inter.begin() ));

    if (inter.size() == 0)
        out << "Case #" << num << ": Volunteer cheated!" << std::endl;
    else if (inter.size() == 1)
        out << "Case #" << num << ": " << *inter.begin() << std::endl;
    else
        out << "Case #" << num << ": Bad magician!" << std::endl;
}

int main()
{
    std::ifstream read("A-small-attempt0.in");
    int test_cases;
    read >> test_cases;

    std::ofstream outfile;
    outfile.open ("output.out");

    for (int i = 1; i <= test_cases; ++i)
        validateTestCase(read, outfile, i);

    outfile.close();
    return 0;
}
