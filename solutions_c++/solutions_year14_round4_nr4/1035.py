#include <algorithm>
#include <iostream>
#include <vector>
#include <string>
#include <map>


struct TrieNode {
    std::map<char, TrieNode> children;
};


void AddString(TrieNode* root, const std::string& string)
{
    for (char c : string) {
        root = &root->children[c];
    }
}


int Cost(const TrieNode& root)
{
    int result = 1;
    for (auto& child : root.children) {
        result += Cost(child.second);
    }
    return result;
}


int Cost(const std::vector<std::string>& strings, int N, const std::vector<int>& plan)
{
    std::vector<TrieNode> roots(N);
    for (size_t i = 0; i < strings.size(); ++i) {
        AddString(&roots.at(plan.at(i)), strings.at(i));
    }
    int result = 0;
    for (const auto& root : roots) {
        if (root.children.empty()) {
            return -1;
        }
        result += Cost(root);
    }
    return result;
}


bool Next(int N, std::vector<int>& plan)
{
    auto it = plan.begin();
    while (it != plan.end() && *it == N - 1) {
        *it = 0;
        ++it;
    }
    if (it == plan.end()) {
        return false;
    }
    ++*it;
    return true;
}


std::pair<int, int> Solve(int N, const std::vector<std::string>& input)
{
    std::vector<int> plan(input.size(), 0);

    int best_cost = Cost(input, N, plan);
    int best_count = 1;

    while (Next(N, plan)) {
        int cost = Cost(input, N, plan);
        if (cost > best_cost) {
            best_cost = cost;
            best_count = 1;
        } else if (cost == best_cost) {
            ++best_count;
        }
    }
    return {best_cost, best_count};
}



int main()
{
    int number_of_cases;
    std::cin >> number_of_cases;
    for (int case_no = 1; case_no <= number_of_cases; ++case_no) {
        int number_of_items, N;
        std::cin >> number_of_items >> N;
        std::vector<std::string> items(number_of_items);
        for (auto& item : items) {
            std::cin >> item;
        }
        const auto result = Solve(N, items);
        std::cout << "Case #" << case_no << ": " << result.first << ' ' << result.second << '\n';
    }
    return 0;
}

