#include <cctype>
#include <cmath>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <map>
#include <string>
#include <vector>
using namespace std;

int max(int a, int b)
{
    return a>b ? a : b;
}

int main(int argc, char* argv[])
{
    string fname = "A-small-attempt0";
    ifstream fin((fname + ".in").c_str());
    ofstream fout((fname + ".out").c_str());
    
    int T; //Number of cases
    fin >> T;
    
    for(int Case=1; Case<=T; Case++)
    {
        //read input
        int N;
        fin >> N;
        
        vector<string> lines;
        //int max_length = 0;
        for(int i=1; i<= N; i++)
        {
            string line;
            fin >> line;
            // cerr << i << ": " << line << endl;
            
            //max_length = max(line.size(), max_length);
            lines.push_back(line);
        }
        
        //solve problem
        //group character sequences then average
        struct group
        {
            char ch;
            int count;
        };
        
        vector< vector<group> > groups;
        for(string line : lines)
        {
            vector<group> gs;
            group g;
            g.ch = line[0];
            g.count = 0;
            for(char ch : line)
            {
                if(ch == g.ch)
                {
                    g.count++;
                }
                if(ch != g.ch)
                {
                    gs.push_back(g);
                    g.ch = ch;
                    g.count = 1;
                }
            }
            gs.push_back(g);
            groups.push_back(gs);
        }
        
        int num_moves = 0;
        for(int i=0; i < N-1; i++)
        {
            if(groups[i].size() != groups[i+1].size())
            {
                num_moves = -1;
                break;
            }
            
            for(int j=0; j<groups[i].size(); j++)
            {
                if(groups[i][j].ch != groups[i+1][j].ch)
                {
                    num_moves = -1;
                    break;
                }
            }
            
            if(num_moves == -1) break;
        }
        
        if(num_moves != -1)
        {
            for(int j=0; j < groups[0].size(); j++)
            {
                int sum = 0;
                for(int i=0; i < N; i++)
                {
                    sum += groups[i][j].count;
                }
                
                int average = sum/N;
                // cerr << groups[0][j].ch << ": " << sum << " / " << N << " = " << average << endl;
                
                for(int i=0; i < N; i++)
                {
                    num_moves += abs(average - groups[i][j].count);
                }
            }
        }
        
        //fancy formatting
        fout << "Case #" << Case << ": ";
        
        //output results
        if(num_moves == -1)
            fout << "Fegla Won" << endl;
        else
            fout << num_moves << endl;
    }
    
    return 0;
}
