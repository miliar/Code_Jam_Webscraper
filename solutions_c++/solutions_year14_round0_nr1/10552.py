#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;

int main(int argc, char *argv[])
{
    int T;
    cin >> T;
    int r1, r2;
    vector<vector<int> > grid1(4, vector<int>(4,0));
    vector<vector<int> > grid2(4, vector<int>(4,0));
    for(int t=1;t<=T;++t)
    {
        cin >> r1;
        --r1;
        for(int i=0;i<4;++i)
            for(int j=0;j<4;++j)
                cin >> grid1[i][j];
        cin >> r2;
        --r2;
        for(int i=0;i<4;++i)
            for(int j=0;j<4;++j)
                cin >> grid2[i][j];

        vector<int> elems(17,0);
        for(int i=0;i<4;++i)
            ++elems[grid1[r1][i]];
        for(int i=0;i<4;++i)
            ++elems[grid2[r2][i]];
        int ans = 0;
        int cont = 0;
        for(int i=1;i<=16;++i)
        {
            if(elems[i] == 2)
            {
                cont+=1;
                ans = i;
            }
        }
        if(cont == 1)
        {
            cout << "Case #"<<t<<": "<< ans << endl;
        }else if(cont>1)
        {
            cout << "Case #"<<t<<": Bad magician!"<<endl;
        }else
        {
            cout << "Case #"<<t<<": Volunteer cheated!"<<endl;
        }

    }
    return EXIT_SUCCESS;
}

