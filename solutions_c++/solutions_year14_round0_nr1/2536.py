#include <fstream>
#include <set>
#include <vector>
using namespace std;


int main()
{
    ifstream fin("A-small-attempt0.in");
    ofstream fout("output.txt");
    int T, t, i, j, a, b, n;
    set<int> sets_a[4], sets_b[4];
    vector<int> result(4);
    vector<int>::iterator it;
    
    fin >> T;
    
    for (t = 1; t <= T; t++) {
        for (i = 0; i < 4; i++) {
            sets_a[i].clear();
            sets_b[i].clear();
        }
        
        fin >> a;
        
        for (i = 0; i < 4; i++)
            for (j = 0; j < 4; j++) {
                fin >> n;
                sets_a[i].insert(n);
            }
        
        fin >> b;
        
        for (i = 0; i < 4; i++)
            for (j = 0; j < 4; j++) {
                fin >> n;
                sets_b[i].insert(n);
            }
        
        it = set_intersection(sets_a[a-1].begin(), sets_a[a-1].end(),
                              sets_b[b-1].begin(), sets_b[b-1].end(),
                              result.begin());
        
        fout << "Case #" << t << ": ";
        
        if (it - result.begin() == 1)
            fout << *result.begin();
        else if (it - result.begin() == 0)
            fout << "Volunteer cheated!";
        else
            fout << "Bad magician!";
        
        fout << endl;
    }
    
    fin.close();
    fout.close();
    
    return 0;
}
