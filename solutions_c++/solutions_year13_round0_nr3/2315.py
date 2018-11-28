#include <iostream>
#include <sstream>
#include <math.h>
#include <fstream>

#include <vector>
#include <map>
#include <set>

using namespace std;

bool palindrome (string &number)
{
    bool palindrome = true;
    for (int i = 0; i < number.size(); i++)
    {
        if (number[i] != number[number.size() - 1 - i]) palindrome = false;
    }
    return palindrome;
}

int main(int argc, char const *argv[])
{
    ifstream ifs(argv[1]);
    ofstream ofs("result");
    int ncases;
    ifs >> ncases;

    vector<uint64_t> palindromes;
    palindromes.push_back(1);
    palindromes.push_back(4);
    palindromes.push_back(9);
    palindromes.push_back(121);
    palindromes.push_back(484);
    palindromes.push_back(10201);
    palindromes.push_back(12321);
    palindromes.push_back(14641);
    palindromes.push_back(40804);
    palindromes.push_back(44944);
    palindromes.push_back(1002001);
    palindromes.push_back(1234321);
    palindromes.push_back(4008004);
    palindromes.push_back(100020001);
    palindromes.push_back(102030201);
    palindromes.push_back(104060401);
    palindromes.push_back(121242121);
    palindromes.push_back(123454321);
    palindromes.push_back(125686521);
    palindromes.push_back(400080004);
    palindromes.push_back(404090404);
    palindromes.push_back(10000200001);
    palindromes.push_back(10221412201);
    palindromes.push_back(12102420121);
    palindromes.push_back(12345654321);
    palindromes.push_back(40000800004);
    palindromes.push_back(1000002000001);
    palindromes.push_back(1002003002001);
    palindromes.push_back(1004006004001);
    palindromes.push_back(1020304030201);
    palindromes.push_back(1022325232201);
    palindromes.push_back(1024348434201);
    palindromes.push_back(1210024200121);
    palindromes.push_back(1212225222121);
    palindromes.push_back(1214428244121);
    palindromes.push_back(1232346432321);
    palindromes.push_back(1234567654321);
    palindromes.push_back(4000008000004);
    palindromes.push_back(4004009004004);
    cout << palindromes.size();

    for (int casenum = 1; casenum < ncases+1; ++casenum)
    {
        int count = 0;
        uint64_t lo;
        uint64_t hi;
        ifs >> lo;
        ifs >> hi;
        for (int i = 0; i < palindromes.size(); i++)
        {
            if (lo <= palindromes[i] && hi >= palindromes[i]) count++;
        }

        cout << "Case #" << casenum << ": " << count << endl;
        ofs << "Case #" << casenum << ": " << count << endl;
    }

//    uint64_t last = (uint64_t) 100000000000000;

//    uint64_t in = 0;
//    do
//    {
//        ifs_squares >> in;
//        cout << in << endl;
//        ostringstream convert;
//        ostringstream convertRoot;
//        convert << in;
//        string number;
//        string root_number;
//        number = convert.str();
//        convertRoot << sqrt(in);
//        root_number = convertRoot.str();
//        if (palindrome(number) && palindrome(root_number))
//        {
//            ofs << number << " " << root_number << endl;
//        }
//    } while (in != last);

    return 0;
}
