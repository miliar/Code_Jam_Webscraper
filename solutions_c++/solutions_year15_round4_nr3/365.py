#include <iostream>
#include <set>
#include <sstream>
#include <vector>
#include <string>
#include <iterator>
#include <limits>

using namespace std;

int N;

vector<set<string> > allLines;

int GetCost(const set<string> &setToAdd, const set<string> &addedToSet, const set<string> &otherSet)
{
    int count = 0;
    std::set<string>::const_iterator it;
    for (it = setToAdd.begin(); it != setToAdd.end(); ++it)
    {
        // In other, but not in added to
        if (otherSet.find(*it) != otherSet.end() 
            && addedToSet.find(*it) == addedToSet.end())
            ++count;
    }
    
    return count;
}

void AddToSet(int pos, set<string> toAddTo, const set<string> &otherSet, int currentCost, int &lowestCost);

void GetBest(int pos, const set<string> &setForOneLang, const set<string> &setForOtherLang, int currentCost, int &lowestCost)
{
    if (currentCost >= lowestCost)
        return;
    else if (pos == N)
    {
        lowestCost = min(lowestCost, currentCost);
        return;
    }
    
    AddToSet(pos, setForOneLang, setForOtherLang, currentCost, lowestCost);
    
    AddToSet(pos, setForOtherLang, setForOneLang, currentCost, lowestCost);
}

void InsertInto(const set<string> &from, set<string> &into)
{
    std::set<string>::const_iterator it;
    for (it = from.begin(); it != from.end(); ++it)
        into.insert(*it);
}

void AddToSet(int pos, set<string> toAddTo, const set<string> &otherSet, int currentCost, int &lowestCost)
{
    currentCost += GetCost(allLines[pos], toAddTo, otherSet);
    InsertInto(allLines[pos], toAddTo);
    GetBest(pos + 1, toAddTo, otherSet, currentCost, lowestCost);
}

int main()
{
    int T;
    cin >> T;
    const set<string> emptySet;
    
    for (int t = 1; t <= T; ++t)
    {
        cin >> N;
        cin.ignore();
        allLines.resize(N);
        for (int i = 0; i < N; ++i)
        {
            string line;
            getline(cin, line);
            stringstream ss(line);
            allLines[i].clear();
            allLines[i].insert(istream_iterator<string>(ss), istream_iterator<string>());
        }
        
        int baseCost = GetCost(allLines[1], emptySet, allLines[0]);
        int bestCost = numeric_limits<int>::max();
        GetBest(2, allLines[0], allLines[1], baseCost, bestCost);
        cout << "Case #" << t << ": " << bestCost << '\n';
    }
}