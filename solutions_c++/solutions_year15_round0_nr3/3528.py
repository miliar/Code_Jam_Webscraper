#include <iostream>
#include <fstream>
#include <string>
#include <set>
using namespace std;


int table[4][4] = {
    {1,  2,  3,  4},
    {2, -1,  4, -3},
    {3, -4, -1,  2},
    {4,  3, -2, -1}
};

int nums[10000];
int L;

inline int reduce_left(int i, int j)
{
    return (i > 0 ? table[i - 1][nums[j % L] - 1] : -table[-i - 1][nums[j % L] - 1]);
}

inline int reduce_right(int i, int j)
{
    return (i > 0 ? table[nums[j % L] - 1][i - 1] : -table[nums[j % L] - 1][-i - 1]);
}


int main(int argc, char * argv[])
{
    if (argc != 3) {
        cout << "Usage: " << argv[0] << " <filein> <fileout>" << endl;
        return 0;
    }
    
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);
    
    int T, t;
    int X, v, i;
    set<int> left_is, right_is;
    set<int>::iterator it;
    string strin;
    
    
    fin >> T;
    
    for (t = 1; t <= T; t++) {
        fin >> L >> X;
        
        fin >> strin;
        
        for (i = 0; i < L; i++)
            nums[i] = strin[i] - 'i' + 2;
        
        
        left_is.clear();
        right_is.clear();
        
        v = 1;
        
        for (i = 0; i < L*X; i++) {
            v = reduce_left(v, i);
            
            if (v == 2)
                left_is.insert(i+1);
        }
        
        v = 1;
        
        for (i = L*X - 1; i >= 0; i--) {
            v = reduce_right(v, i);
            
            if (v == 4)
                right_is.insert(i);
        }
        
        
        for (it = left_is.begin(); it != left_is.end(); it++) {
            v = 1;
            
            for (i = *it; i < L*X; i++) {
                v = reduce_left(v, i);
                
                if (v == 3 && right_is.count(i+1))
                    break;
            }
            
            if (i < L*X)
                break;
        }
        
        fout << "Case #" << t << ": " << (it != left_is.end() ? "YES" : "NO") << endl;
    }
    
    fin.close();
    fout.close();
    
    return 0;
}
