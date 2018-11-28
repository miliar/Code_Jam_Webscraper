#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <forward_list>
#include <array>
#include <iterator>
#include <algorithm>
#include <set>
#include <unordered_set>
#include <map>
#include <unordered_map>
#include <queue>
#include <stack>
#include <limits>

using namespace std;

int find_product(vector<vector<int> > &table, int product, int next) {
    int sign = 1;
    if (product < 0) {
        product = -product;
        sign = -1;
    }
    return table[product][next] * sign;
}

int find_product_backward(vector<vector<int> > &table, int product, int next) {
    int sign = 1;
    if (product < 0) {
        product = -product;
        sign = -1;
    }
    return table[next][product] * sign;
}    

int main(void) {
    ifstream ifs("/home/amor/Downloads/PI.txt");
    ofstream ofs("/home/amor/Downloads/PO.txt");
    vector<vector<int> > table = {{0,0,0,0,0},
                                  {0,1,2,3,4},
                                  {0,2,-1,4,-3},
                                  {0,3,-4,-1,2},
                                  {0,4,3,-2,-1}};
    unordered_map<char, int> mapping;
    mapping['i'] = 2, mapping['j'] = 3, mapping['k'] = 4;
    int nb_cases = 0;
    ifs >> nb_cases;
    for (int i = 1; i <= nb_cases; ++i) {
        int base_size = 0;
        int repeat = 1;
        ifs >> base_size;
        //ofs << "base_size = " << base_size << endl;
        ifs >> repeat;
        //ofs << "repeat = " << repeat << endl;
        string base;
        ifs >> base;
        int base_val = 1;
        for (int j = 0; j < base_size; ++j)
            base_val = find_product(table, base_val, mapping[base[j]]);
        // ofs << "base_val = " << base_val << endl;
        int n = repeat % 4;
        // ofs<< "n = " << n << endl;
        int all_val = 1;
        for (int j = 0; j < n; ++j) {
            int sign = 1;
            if (all_val < 0) {
                all_val = -all_val;
                sign *= -1;
            }
            if (base_val < 0)
                all_val = table[all_val][-base_val] * sign * (-1);
            else
                all_val = table[all_val][base_val] * sign;
        }
        // ofs << "all_val = " << all_val << endl;
        if (all_val != -1) {
            ofs << "Case #" << i << ": NO" << endl;
            continue;
        }
        // Find the first possible index with value i.
        int front_val = 1, front_pos = -1;;
        for (int j = 0; j < min(repeat, 4) * base_size; ++j) {
            front_val = find_product(table, front_val, mapping[base[j % base_size]]);
            if (front_val == 2) {
                front_pos = j;
                break;
            }
        }
        // ofs << "front_pos = " << front_pos << endl;
        if (front_pos == -1) {
            ofs << "Case #" << i << ": NO" << endl;
            continue;
        }
        // Find the last possible index with value j.
        int back_val = 1, back_pos = -1;
        for (long long j = repeat * base_size - 1; j >= repeat * base_size - min(repeat, 4) * base_size && j >= front_pos + 2; --j) {
            back_val = find_product_backward(table, back_val, mapping[base[j % base_size]]);
            if (back_val == 4) {
                back_pos = j;
                break;
            }
        }
        // ofs << "back_pos = " << back_pos << endl;
        if (back_pos == -1)
            ofs << "Case #" << i << ": NO" << endl;
        else
            ofs << "Case #" << i << ": YES" << endl;
    }
    ifs.close();
    ofs.close();
    return EXIT_SUCCESS;
}



