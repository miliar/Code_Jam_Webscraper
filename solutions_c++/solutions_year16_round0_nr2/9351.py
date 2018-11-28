

#include <fstream>
#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;
ifstream fin ("/Users/Andrew/Desktop/untitled folder/gcjA/gcjA/Opis.txt");
ofstream fout("/Users/Andrew/Desktop/untitled folder/gcjA/gcjA/output.txt");
int tests;
int solve(string s)
{
    int ans = 0;
    for (int i = 0; i < s.size(); ++i){
        int j;
        j = i;
        while (s[j] == '-' && j < s.size()){
            j++;
        }
        if (j != i){
            j--;
            if (i == 0)
                ans ++;
            else
                ans += 2;
            i = j;
        }
    }
    return ans;
        
}
int main(int argc, const char * argv[]) {
    string s;
    //getline(cin,s);
    int tests;
    fin >> tests;
    int t = 0;
   // cout << "OK\n";

    while(++t <= tests){

        fin >> s;
        fout << "Case #" << t << ": " << solve(s) << endl;
        
    }
    
    

    return 0;
}
