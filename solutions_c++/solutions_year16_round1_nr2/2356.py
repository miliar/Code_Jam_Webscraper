#include <fstream>
#include <iostream>
#include <queue>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

struct Task
{
    size_t N;
    vector<vector<int>> lists;
};

bool sortVector(const vector<int>& lhs, const vector<int>& rhs)
{
    for (size_t i = 0; i < lhs.size(); ++i) {
        if (lhs[i] < rhs[i]) return true;
        if (lhs[i] > rhs[i]) return false;
    }
    return false;
}

vector<Task> ReadTask(istream& in)
{
    size_t count;
    in >> count;
    vector<Task> tasks;
    while (count-- > 0)
    {
        Task task;
        in >> task.N;
        for (size_t i = 0; i < 2 * task.N - 1; ++i) {
            vector<int> heights;
            for (size_t j = 0; j < task.N; ++j) {
                int h;
                in >> h;
                heights.push_back(h);
            }
            task.lists.push_back(heights);
        }
        std::sort(task.lists.begin(), task.lists.end(), sortVector);
        tasks.push_back(task);
    }
    return tasks;
}

string VerifyGrid(const Task& task, const vector<vector<int>>& grid, vector<bool> usedRows)
{
    int missingRow = -1;
    for (size_t i = 0; i < task.N; ++i) {
        bool found = true;
        for (size_t k = 0; k < task.lists.size(); ++k) {
            if (usedRows[k]) {
                continue;
            }
            for (size_t j = 0; j < task.N; ++j) {
                if (task.lists[k][j] != grid[j][i]) {
                    found = false;
                    break;
                }
            }
            if (found) {
                usedRows[k] = true;
                break;
            }
        }
        if (!found) {
            if (missingRow == -1) {
                missingRow = i;
            }
            else {
                return string();
            }
             
        }
    }
    if (missingRow == -1) {
        missingRow = task.N - 1;
    }
    ostringstream oss;
    for (size_t i = 0; i < task.N; ++i) {
        oss << grid[i][missingRow] << " ";
    }
    return oss.str();
}

string GetMissingList(const Task& task, size_t row, vector<vector<int>> grid, vector<bool> usedRows)
{
    for (size_t i = row; i < task.lists.size(); ++i) {
        usedRows[i] = true;
        grid.push_back(task.lists[i]);
        string missingRow;
        if (grid.size() == task.N) {
            missingRow = VerifyGrid(task, grid, usedRows);
        }
        else {
            missingRow = GetMissingList(task, i + 1, grid, usedRows);
        }
        if (!missingRow.empty()) {
            return missingRow;
        }
        grid.pop_back();
        usedRows[i] = false;
    }
    if (grid.size() == task.N) {
        return VerifyGrid(task, grid, usedRows);
    }
    return string();
}

void DoTask(Task task, ostream& os)
{
    static size_t caseCount = 0;
    os << "Case #" << ++caseCount << ": ";

    vector<bool> usedRows(task.lists.size(), false);
    vector<vector<int>> grid;
    string row = GetMissingList(task, 0, grid, usedRows);
    os << row << std::endl;
}

int main()
{
    vector<Task> tasks = ReadTask(ifstream("input.txt"));
    ofstream ofs("output.txt", std::ios::trunc);
    for (auto task : tasks)
    {
        DoTask(task, ofs);
    }
    return 0;
}
