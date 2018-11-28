

#include <fstream>
#include <cstdio>
#include <iostream>

using namespace std;
ifstream fin ("/Users/Andrew/Desktop/untitled folder/gcjA/gcjA/Opis.txt");
ofstream fout("/Users/Andrew/Desktop/untitled folder/gcjA/gcjA/output.txt");
int have[10];
int ans = 0;
int cnt = 0;
int n0;
void go(int n)
{
    if (cnt == 10){
        ans = n - n0;
        return;
    }
    int fake = n;
    while (fake > 0){
        if (have[fake % 10] == -1){
            have[fake % 10] = n;
            cnt++;
        }
        fake /= 10;
    }
    go(n + n0);
}
int main(int argc, const char * argv[]) {

    int tests;
    fin >> tests;
    int t = 0;
    while(++t <= tests){
        
        int n;
        for (int i = 0; i < 10; ++i)
            have[i] = -1;
        fin >> n;
        fout << "Case #" << t << ": ";
        if (n == 0){
            fout << "INSOMNIA\n";
            continue;
        }
        n0 = n;
        cnt = 0;
        go(n);
        fout << ans << endl;
    }
    
    

    return 0;
}
