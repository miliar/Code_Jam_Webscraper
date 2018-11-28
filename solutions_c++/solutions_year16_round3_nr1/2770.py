#include <iostream>
#include <map>
#include <vector>
#include <fstream>

using namespace std;

int main()
{
    ifstream file_reader("large_input.in");
    ofstream file_writer("large_output.txt");//When large freq_party.size()==1000
    int t;
    file_reader >> t;

    for(int c = 1; c<=t; ++c)
    {
        vector<vector<char>> freq_party;
        for(int i = 0; i<=1000; ++i)
            freq_party.push_back({});

        int n;
        file_reader >> n;

        for(int i = 1; i<=n; ++i)
        {
            int freq;
            file_reader >> freq;
            freq_party[freq].push_back((char)('A'+i-1));
        }

        file_writer << "Case #" << c << ": ";
        for(int i = 1000; i>=1; --i)
        {
            if(freq_party[i].size()==0)
                continue;
            if(freq_party[i].size()%2==0)
            {
                for(int j = 0; j<freq_party[i].size(); j+=2)
                {
                    file_writer << freq_party[i][j] << freq_party[i][j+1] << " ";
                    freq_party[i-1].push_back(freq_party[i][j]);
                    freq_party[i-1].push_back(freq_party[i][j+1]);
                }
            }
            else if(i==1)
            {
                file_writer << freq_party[i][0] << " ";
                for(int j = 1; j<freq_party[i].size(); j+=2)
                {
                    file_writer << freq_party[i][j] << freq_party[i][j+1] << " ";
                    freq_party[i-1].push_back(freq_party[i][j]);
                    freq_party[i-1].push_back(freq_party[i][j+1]);
                }
            }
            else
            {
                for(int j = 0; j<freq_party[i].size(); j+=2)
                {
                    if(j==freq_party[i].size()-1)
                    {
                        file_writer << freq_party[i][j] << " ";
                        freq_party[i-1].push_back(freq_party[i][j]);
                        continue;
                    }
                    file_writer << freq_party[i][j] << freq_party[i][j+1] << " ";
                    freq_party[i-1].push_back(freq_party[i][j]);
                    freq_party[i-1].push_back(freq_party[i][j+1]);
                }
            }
        }
        file_writer << endl;
    }
}
