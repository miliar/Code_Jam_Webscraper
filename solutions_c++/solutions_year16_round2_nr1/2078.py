#include <string>
#include <fstream>
#include <iostream>
using namespace std;

int get0(int ch[26])
{
    int count = ch[25];
    ch[25] -= count;
    ch[4] -= count;
    ch[17] -= count;
    ch[14] -= count;
    
    return count;
}

int get1(int ch[26])
{
    int count = ch[14];
    ch[14] -= count;
    ch[13] -= count;
    ch[4] -= count;
    
    return count;
}

int get2(int ch[26])
{
    int count = ch[22];
    ch[19] -= count;
    ch[22] -= count;
    ch[14] -= count;
    
    return count;
}

int get3(int ch[26])
{
    int count = ch[7];
    ch[19] -= count;
    ch[7] -= count;
    ch[17] -= count;
    ch[4] -= count;
    ch[4] -= count;
    
    return count;
}

int get4(int ch[26])
{
    int count = ch[20];
    ch[5] -= count;
    ch[14] -= count;
    ch[20] -= count;
    ch[17] -= count;
    
    return count;
}

int get5(int ch[26])
{
    int count = ch[5];
    ch[5] -= count;
    ch[8] -= count;
    ch[21] -= count;
    ch[4] -= count;
    
    return count;
}

int get6(int ch[26])
{
    int count = ch[23];
    ch[18] -= count;
    ch[8] -= count;
    ch[23] -= count;
    
    return count;
}

int get7(int ch[26])
{
    int count = ch[18];
    ch[18] -= count;
    ch[4] -= count;
    ch[21] -= count;
    ch[4] -= count;
    ch[13] -= count;
    
    return count;
}

int get8(int ch[26])
{
    int count = ch[6];
    ch[4] -= count;
    ch[8] -= count;
    ch[6] -= count;
    ch[7] -= count;
    ch[19] -= count;
    
    return count;
}

int get9(int ch[26])
{
    int count = ch[8];
    ch[13] -= count;
    ch[8] -= count;
    ch[13] -= count;
    ch[4] -= count;
    
    return count;
}

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("Aout.txt");
    
    int T;
    fin >> T;
    for(int t =1; t <= T; ++t)
    {
        int ch[26], ans[10];
        for(int i = 0; i < 26; ++i)
            ch[i] = 0;
        for(int i = 0; i < 10; ++i)
            ans[i] = 0;
            
        string s;
        fin >> s;
        
        for(int i = 0; i < s.length(); ++i)
            ++ch[s[i] - 'A'];
            
        ans[0] += get0(ch);
        ans[2] += get2(ch);
        ans[4] += get4(ch);
        ans[6] += get6(ch);
        ans[8] += get8(ch);
        ans[3] += get3(ch);
        ans[5] += get5(ch);
        ans[7] += get7(ch);
        ans[1] += get1(ch);
        ans[9] += get9(ch);
        
        fout << "Case #" << t << ": ";
        for(int i = 0; i < 10; ++i)
            for(int j = 0; j < ans[i]; ++j)
                fout << i;
        fout << endl;
    }
    

    return 0;    
}
