#include <iostream>
#include <queue>
#include <vector>
#include <fstream>

using namespace std;

int canBeat(double value,vector<double> checkTo)
{
    for(int i=checkTo.size()-1;i>=0;i--)
    {
        if(value>checkTo[i])
            return i;
    }
    return -1;
}

int main()
{
    ifstream input("D-large.in");
    ofstream output("resultsLarge.txt");
    int caseNum;
    input>>caseNum;
    for(int j=1;j<=caseNum;j++)
    {
        int blockNum;
        input>>blockNum;
        priority_queue<double> naomiBlocks,kenBlocks;
        vector<double> kenReverseBlocks,naomiReverseBlocks;
        for(int i=0;i<blockNum;i++)
        {
            double temp;
            input>>temp;
            naomiBlocks.push(temp);
        }
        vector<double> temp2;
        for(int i=0;i<blockNum;i++)
        {
            temp2.push_back(naomiBlocks.top());
            naomiBlocks.pop();
        }
        for(int i=0;i<blockNum;i++)
        {
            naomiBlocks.push(temp2[i]);
        }
        for(int i=0;i<blockNum;i++)
        {
            naomiReverseBlocks.push_back(temp2[temp2.size()-1-i]);
        }

        for(int i=0;i<blockNum;i++)
        {
            double temp;
            input>>temp;
            kenBlocks.push(temp);
        }
        vector<double> temp;
        for(int i=0;i<blockNum;i++)
        {
            temp.push_back(kenBlocks.top());
            kenBlocks.pop();
        }
        for(int i=0;i<blockNum;i++)
        {
            kenReverseBlocks.push_back(temp[temp.size()-1-i]);
        }
        for(int i=0;i<blockNum;i++)
        {
            kenBlocks.push(kenReverseBlocks[i]);
        }

        int cheatWins=0;
        int fairWins=0;
        for(int i=0;i<blockNum;i++)
        {
            int canBeatResult=canBeat(naomiBlocks.top(),kenReverseBlocks);
            if(canBeatResult>-1)
            {
                cheatWins++;
                naomiBlocks.pop();
                kenReverseBlocks.erase(kenReverseBlocks.begin()+canBeatResult);
            }
            else if(naomiBlocks.top()>kenReverseBlocks[i])
            {
                cheatWins++;
                naomiBlocks.pop();
            }

            int kenWinResults=canBeat(kenBlocks.top(),naomiReverseBlocks);
            if(kenWinResults>-1)
            {
                fairWins++;
                kenBlocks.pop();
                naomiReverseBlocks.erase(naomiReverseBlocks.begin()+kenWinResults);
            }
        }
        output<<"Case #"<<j<<": "<<cheatWins<<" "<<blockNum-fairWins<<endl;
    }
    return 0;
}
