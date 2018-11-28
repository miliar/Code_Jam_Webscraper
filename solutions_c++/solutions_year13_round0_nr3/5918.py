#include <iostream>
#include <vector>
#include <math.h>
#include <fstream>

using namespace std;

int ok(int num)
{
    vector <int> vv;
    while(num)
        vv.push_back(num % 10),
        num /= 10;
    for (int i = 0; i < vv.size() / 2; i++)
        if (vv[i] != vv[vv.size() - 1 - i])
            return 0;
    return 1;
}
int main()
{
    ifstream cin("in.txt");
    ofstream cout("out.txt");
    int p;
    cin>>p;
    for (int T = 0; T < p; T++)
    {
        int L, R, c = 0;
        cin>> L >> R;
        for (int i = L; i <= R; i++)
        {
            int j = sqrt(i*1.0);
            if (i != j*j) continue;
            if (ok(i) && ok(j))
                c++;
        }
        cout<<"Case #"<<T+1<<": "<<c<<endl;
    }
    return 0;
}
