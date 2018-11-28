#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

string eval(ifstream& in)
{
    int N,M;
    in>>N>>M;
    vector<int> rowMaxes(N,0);
    vector<int> colMaxes(M,0);
    vector<vector<int>> grid(N,vector<int>(M,0));
    for(int r=0;r<N;r++)
    {
        for(int c=0;c<M;c++)
        {
            int v;
            in>>v;
            grid[r][c] = v;
            if(v > rowMaxes[r]) rowMaxes[r] = v;
            if(v > colMaxes[c]) colMaxes[c] = v;
        }
    }
    for(int r=0;r<N;r++)
    {
        for(int c=0;c<M;c++)
        {
            if(grid[r][c] < rowMaxes[r] && grid[r][c] < colMaxes[c]) return "NO";
        }
    }
    return "YES";
}

int main(int argc, char* argv[])
{
    ifstream in("B-large.in");
    ofstream out("out.txt");
    int T;
    in>>T;
    for(int i=0;i<T;i++)
    {
        out<<"Case #"<<i+1<<": "<<eval(in)<<endl;
    }
    in.close();
    out.close();
	return 0;
}
