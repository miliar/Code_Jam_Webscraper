#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <algorithm>
#include <set>

using GoldIndexSet = std::set<int>;
using Golds = std::vector<GoldIndexSet>;

// gold index to other components
using Graph = std::map<int, std::set<int>>;


bool search(Graph& graph, Golds golds, int s, std::set<int>& result)
{
    int amount_visited = 0;
    std::map<int, bool> visited;
    int current = 0;
    for(;;)
    {
        amount_visited += 1;
        visited[current] = true;

        if(amount_visited == golds.size())
        {
            break;
        }

        bool found = false;
        for(auto x : golds[current])
        {
            int newCurrent = current;
            for(auto y : graph[x])
            {
                if(!visited[y])
                {
                    newCurrent = y;
                    break;
                }
            }
            if(newCurrent != current)
            {
                current = newCurrent;
                result.emplace(x);
                found = true;
                break;
            }
        }

        if(!found && amount_visited != s)
        {
            bool found = false;
            // pick thing in golds
            for(int i = 0; i < golds.size(); ++i)
            {
                if(!visited[i])
                {
                    current = i;
                    found = true;
                    break;
                }
            }

            if(found)
                break;
        }

    }

    return true;
}

int main()
{
    int t;
    std::cin >> t;

    std::map<std::string, int> cache;

    for(int i = 0; i < t; ++i)
    {
        int k, c, s;
        std::cin >> k >> c >> s;

        std::cout << "Case #" << i + 1 << ": ";

        if(k == 1)
        {
            std::cout << 1 << '\n';
            continue;
        }

        if(c == 1 && s != 1)
        {
            for(int i = 0; i < k; ++i)
            {
                std::cout << i + 1 << ' ';
            }
            std::cout << std::endl;
            continue;
        }

        if(c > 2)
        {
            c = 2;
        }

        std::string str;
        str.resize(k, 'L');

        Graph graph;
        Golds golds;
        for(int i = 0; i < str.size(); ++i)
        {
            str[i] = 'G';

            std::string res = str;
            for(int i = 0; i < c - 1; ++i)
            {
                std::string temp;
                for(auto x : res)
                {
                    if(x == 'L')
                    {
                        temp += str;
                    }
                    else
                    {
                        for(int i = 0; i < k; ++i)
                            temp += 'G';
                    }
                }

                res = temp;
            }

            GoldIndexSet g;
            int j = 0;
            for(auto ch : res)
            {
                if(ch == 'G')
                {
                    graph[j].emplace(i);
                    g.emplace(j);
                }

                ++j;
            }
            golds.emplace_back(g);

            str[i] = 'L';
        }

        std::set<int> result;
        if(search(graph, golds, s, result) && !result.empty())
        {
            for(auto x : result)
            {
                std::cout << x + 1 << ' ';
            }
        }
        else
        {
            std::cout << "IMPOSSIBLE";
        }

        std::cout << std::endl;
    }
}
