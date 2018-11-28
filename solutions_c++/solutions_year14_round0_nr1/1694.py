#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

bool myfunction (int i, int j) {
    return (i==j);
}

int main()
{
    ifstream fin("magic.in");
    ofstream fout("magic.out");
    int cases, counter=0, tmpans1, tmpans2;
    int cards[4][4];
    int compare1[4];
    int compare2[4];
    vector<int> ans;
    fin >> cases;
    for(int i=0;i<cases;i++)
    {
        ans.clear();
        counter=0;
        fin >> tmpans1;
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                fin >> cards[j][k];
                if(j==tmpans1-1)
                {
                    compare1[k]=cards[j][k];
                }
            }
        }
        fin >> tmpans2;
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                fin >> cards[j][k];
                if(j==tmpans2-1)
                {
                    compare2[k]=cards[j][k];
                }
            }
        }
       // sort(compare1, compare1+4);
       // sort(compare2, compare2+4);
        for(int j=0;j<4;j++)
        {
            for(int k=0;k<4;k++)
            {
                if(compare1[j]==compare2[k])
                {
                    ans.push_back(compare1[j]);
                }
            }
        }
        unique(ans.begin(), ans.end(), myfunction);
        counter = ans.size();
        if(counter==0)
        {
            fout << "Case #" << i+1 << ": Volunteer cheated!";
           cout << "Case #" << i+1 << ": Volunteer cheated!";
        }else if(counter==1)
        {
            fout << "Case #" << i+1 << ": " << ans[0];
           cout << "Case #" << i+1 << ": " << ans[0];
        }else
        {
            fout << "Case #" << i+1 << ": Bad magician!";
           cout << "Case #" << i+1 << ": Bad magician!";
        }
        fout << endl;
        cout << endl;
    }
    return 0;
}
