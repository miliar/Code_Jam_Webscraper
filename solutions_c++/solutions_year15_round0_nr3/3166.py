#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <algorithm>

using namespace std;

map<pair<string, string>, string> multiplication_table;

void PopulateMultiplicationTable(void)
{
    multiplication_table[make_pair("1", "1")] = "1";
    multiplication_table[make_pair("1", "i")] = "i";
    multiplication_table[make_pair("1", "j")] = "j";
    multiplication_table[make_pair("1", "k")] = "k";
    multiplication_table[make_pair("i", "1")] = "i";
    multiplication_table[make_pair("i", "i")] = "-1";
    multiplication_table[make_pair("i", "j")] = "k";
    multiplication_table[make_pair("i", "k")] = "-j";
    multiplication_table[make_pair("j", "1")] = "j";
    multiplication_table[make_pair("j", "i")] = "-k";
    multiplication_table[make_pair("j", "j")] = "-1";
    multiplication_table[make_pair("j", "k")] = "i";
    multiplication_table[make_pair("k", "1")] = "k";
    multiplication_table[make_pair("k", "i")] = "j";
    multiplication_table[make_pair("k", "j")] = "-i";
    multiplication_table[make_pair("k", "k")] = "-1";
    return;
}

string Solve(string& ijk, int X);
string ProductInTheRange(string& ijk, int from, int to);

int main(void)
{
    PopulateMultiplicationTable();

    int T, c = 1;
    cin >> T;
    while (T--) {
        int L, X;
        string ijk;
        cin >> L >> X;
        cin >> ijk;
        cout << "Case #" << c++ << ": " << Solve(ijk, X) << endl;
    }
    return 0;
}

string Solve(string& ijk, int X)
{
    string copy_of_ijk = ijk;
    for (int i = 1; i < X; ++i)
        ijk += copy_of_ijk;
    vector<int> i_locations, k_locations;
    // Get all the "i" product locations from the left
    string product_from_left = "1";
    for (int i = 0; i < ijk.size(); ++i) {
        string tmp;
        tmp = ijk.at(i);
        bool negate = false;
        if (product_from_left.at(0) == '-')
            negate = true;
        if (!negate) {
            product_from_left = multiplication_table[make_pair(product_from_left, tmp)];
        } else {
            product_from_left = product_from_left.at(1);
            product_from_left = multiplication_table[make_pair(product_from_left, tmp)];
            if (product_from_left.at(0) == '-')
                product_from_left = product_from_left.at(1);
            else
                product_from_left = string("-") + product_from_left;
        }
        if (product_from_left == "i") {
            i_locations.push_back(i);
        }
    }
    if (!i_locations.empty()) {
        // Get all the "k" product locations from the right
        string product_from_right = "1";
        for (int k = ijk.size()-1; k > -1; --k) {
            string tmp;
            tmp = ijk.at(k);
            bool negate = false;
            if (product_from_right.at(0) == '-')
                negate = true;
            if (!negate)
                product_from_right = multiplication_table[make_pair(tmp, product_from_right)];
            else {
                product_from_right = product_from_right.at(1);
                product_from_right = multiplication_table[make_pair(tmp, product_from_right)];
                if (product_from_right.at(0) == '-')
                    product_from_right = product_from_right.at(1);
                else
                    product_from_right = string("-") + product_from_right;
            }
            if (product_from_right == "k") {
                k_locations.push_back(k);
            }
        }
        // Check if the product range between any of [i+1 to k-1] equals j
        sort(k_locations.begin(), k_locations.end());
        for (int i = 0; i < i_locations.size(); ++i) {
            string saved_prod = "1";
            bool use_saved_prod = false;
            for (int k = 0; k < k_locations.size(); ++k) {
                if (i_locations.at(i) < k_locations.at(k)) {
                    string is_prod_j;
                    bool negate = false;
                    if (use_saved_prod) {
                        string additional_range_prod = ProductInTheRange(ijk, k_locations.at(k-1), k_locations.at(k)-1);
                        if ((saved_prod.at(0) == '-' && additional_range_prod.at(0) != '-') ||
                            (saved_prod.at(0) != '-' && additional_range_prod.at(0) == '-'))
                            negate = true;
                        if (saved_prod.at(0) == '-')
                            saved_prod = saved_prod.at(1);
                        if (additional_range_prod.at(0) == '-')
                            additional_range_prod = additional_range_prod.at(1);
                        is_prod_j = multiplication_table[make_pair(saved_prod, additional_range_prod)];
                        if (negate) {
                            if (is_prod_j.at(0) == '-')
                                is_prod_j = is_prod_j.at(1);
                            else
                                is_prod_j = string("-") + is_prod_j;
                        }
                    } else
                        is_prod_j = ProductInTheRange(ijk, i_locations.at(i)+1, k_locations.at(k)-1);

                    if (is_prod_j == "j")
                        return "YES";
                    saved_prod = is_prod_j;
                    use_saved_prod = true;
                }
            }
        }
    }
    return "NO";
}

string ProductInTheRange(string& ijk, int from, int to)
{
    if (from == to) {
        string retval;
        retval = ijk.at(from);
        return retval;
    } else if (from > to) // ik case
        return "1";
    string multiplication = "1";
    for (int i = from; i <= to; ++i) {
        string tmp;
        tmp = ijk.at(i);
        bool negate = false;
        if (multiplication.at(0) == '-')
            negate = true;
        if (!negate)
            multiplication = multiplication_table[make_pair(multiplication, tmp)];
        else {
            multiplication = multiplication.at(1);
            multiplication = multiplication_table[make_pair(multiplication, tmp)];
            if (multiplication.at(0) == '-')
                multiplication = multiplication.at(1);
            else
                multiplication = string("-") + multiplication;
        }
    }
    return multiplication;
}

