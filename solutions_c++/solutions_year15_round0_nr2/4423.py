#!/usr/bin/env cppsh
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <iterator>
#include <vector>
#include <sstream>
#include <cmath>
#include <queue>



typedef std::map<int, int> State;
void print(State& state)
{
    for (State::iterator it = state.begin(); it != state.end(); ++it)
    {
        std::cout << it->first << ":" << it->second << " ";
    }
    std::cout << std::endl;
}

struct Node
{
    State state;
    int cost;

    Node(int c = 0): cost(c) { }
    Node(const State& s, int c): state(s), cost(c) { }

    bool terminal() const
    {
        return state.empty();
    }

    int maxValue() const
    {
        return state.rbegin()->first;
    }

    int reps() const
    {
        return state.rbegin()->second;
    }

    std::vector<Node> adjacent() const
    {
        std::vector<Node> res(1, Node(cost + maxValue()));
        if (maxValue() < 4)
            return res;

        double val = sqrt(maxValue());
        int splits = val;
        if (val != int(val))
            ++splits;
        for (int i = 2; i <= splits; ++i)
        {
            val = (double)maxValue() / i;
            int divisor = maxValue() / i;
            if (val != int(val))
                ++divisor;
            int factor = maxValue() / divisor;
            int remainder = maxValue() % divisor;
            int splitCost = reps() * factor;
            if (remainder == 0)
                splitCost -= reps();
            State nextState(state);
            nextState.erase(maxValue());
            nextState[divisor] += reps() * factor;
            if (remainder)
                nextState[remainder] += reps();
            Node neighbor(nextState, cost + splitCost);
            //print(nextState);
            //std::cout << neighbor.cost << std::endl;
            res.push_back(neighbor);
        }
        return res;
    }

    friend bool operator< (const Node& a, const Node& b)
    {
        return a.cost > b.cost;
    }
};

int solve(Node& state)
{
    if (state.state.empty())
        return 0;

    int res = state.maxValue();
    if (res < 4)
        return res;

    std::priority_queue<Node> Q;
    Q.push(state);
    while (!Q.empty())
    {
        Node node = Q.top();
        Q.pop();
        //std::cout << "current state: " << std::endl;
        //print(node.state);
        //std::cout << node.cost << std::endl;
        if (node.terminal())
        {
            return node.cost;
        }
        else
        {
            std::vector<Node> neighbors = node.adjacent();
            for (Node& node : neighbors)
            {
                Q.push(node);
            }
        }
    }

    return res;
}

int main(int argc, char* argv[])
{
    std::string str;
    std::getline(std::cin, str);
    const int N = atoi(str.c_str());
    std::vector<int> res;
    for (int i = 0; i < N; ++i)
    {
        std::getline(std::cin, str); // skip diner count
        std::getline(std::cin, str);
        std::stringstream ss(str);
        State initial;
        int val;
        while (ss >> val)
        {
            initial[val]++;
        }
        Node state(initial, 0);
        res.push_back(solve(state));
    }
    for (int i = 0; i < res.size(); ++i)
    {
        std::cout << "Case #" << (i+1) << ": " << res[i] << std::endl;
    }
    return 0;
}
