#include <iostream>
#include <fstream>
#include <set>
#include <algorithm>
#include <iterator>

#define cin in
#define cout out

using namespace std;
ifstream in("input.txt");
ofstream out("output.txt");


int main() 
{
    int n;
    cin>>n;
    for(int I = 1; I <= n; ++I)
    {
        set<long> s1;
        set<long> s2;

        int b[5][5];
        int a[5][5];
        int r;
        cin >> r;
        for(int i = 1; i <= 4; ++i)
            for(int j = 1; j <= 4; ++j)
                cin >> a[i][j];
        for(int i = 1; i <= 4; ++i)
            s1.insert(a[r][i]);
        cin >> r;
        for(int i = 1; i <= 4; ++i)
            for(int j = 1; j <= 4; ++j)
                cin >> b[i][j];
        for(int i = 1; i <= 4; ++i)
            s2.insert(b[r][i]);
        
        set<int> intersect;
        set_intersection(s1.begin(), s1.end(), s2.begin(), s2.end(), inserter(intersect,intersect.begin()));
        
      
        cout << "Case #" << I << ": ";
        if(intersect.size() == 0)
            cout << "Volunteer cheated!";
        if(intersect.size() == 1)
            cout << *(intersect.begin());
        if(intersect.size() > 1)
            cout << "Bad magician!";
        cout << endl;
    }
}