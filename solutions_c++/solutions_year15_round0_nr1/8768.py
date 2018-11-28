#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <fstream>
using namespace std;

int main()
{
    fstream in("C:\\Users\\gaoxun\\Downloads\\A-large.in");
    fstream out("C:\\project\\standing_ovation", ios::out);
    int all_audi  = 0;
    in >> all_audi;
    int *maxS = new int[all_audi];
    vector<string> line;
    for(int i = 0; i < all_audi; ++i){
        int s = 0;
        in >> s;
        maxS[i] = s;
        string tmp;
        in >> tmp;
        line.push_back(tmp);
    }
    for(int i = 0; i < all_audi; ++i){
        int s = maxS[i];
        string l = line[i];
        int res = 0;
        int people = 0;
        for(int j = 0; j < l.size(); ++j){
            int stand = l[j] - '0';
            if(stand == 0)
                continue;
            if(j > people){
                res += j - people;
                people = j;
                people += stand;
            }
            else
                people += stand;
        }
        out << "case #" << i + 1 << ": " << res << endl;
    }
}
