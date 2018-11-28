#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

string canmake(vector<vector<int> >& heights, vector<int>& maxrowheights, vector<int>& maxcolheights)
{
    int numcols = heights[0].size();
    int numrows = heights.size();
    vector<bool> isokrow(numcols,false);
    vector<vector<bool> > isok(numrows,isokrow);
    int numok = 0;
    for(int row = 0; row < numrows; row++)
    {
        for(int col = 0; col < numcols; col++)
        {
            if(isok[row][col] == false)
            {
                if(heights[row][col] == maxrowheights[row])
                {
                    isok[row][col] = true;
                    numok++;
                }
                else if(heights[row][col] == maxcolheights[col])
                {
                    isok[row][col] = true;
                    numok++;
                }
            }
        }
    }
    if(numok == numrows*numcols) return "YES";
    return "NO";
}

int main()
{
    ifstream lawnfile("B-large.in");
    ofstream answers("largelawnanswer.txt");

    int numlawns;
    lawnfile >> numlawns;
    lawnfile.ignore(255,'\n');
    vector<vector<int> > heights;
    vector<int> lawnrow;
    vector<int> maxrowheights;
    vector<int> maxcolheights;
    int numcols, numrows, temp;

    for(int lawn=1; lawn <= numlawns; lawn++)
    {
        heights.clear();
        lawnrow.clear();
        maxrowheights.clear();
        maxcolheights.clear();
        lawnfile >> numrows >> numcols;
        lawnfile.ignore(255,'\n');
        for(int i=0; i < numcols; i++) maxcolheights.push_back(0);
        for(int i=0; i < numrows; i++) maxrowheights.push_back(0);
        for(int row = 0; row < numrows; row++)
        {
            for(int col = 0; col < numcols; col++)
            {
                lawnfile >> temp;
                lawnrow.push_back(temp);
                if(temp > maxrowheights[row]) maxrowheights[row] = temp;
                if(temp > maxcolheights[col]) maxcolheights[col] = temp;
            }
            lawnfile.ignore(255,'\n');
            heights.push_back(lawnrow);
            lawnrow.clear();
        }
        answers << "Case #" << lawn << ": " << canmake(heights,maxrowheights,maxcolheights);
        if(lawn != numlawns) answers << endl;
    }
    return 0;
}
