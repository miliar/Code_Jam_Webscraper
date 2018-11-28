/*
 * A. Magic Trick.cpp
 *
 *  Created on: Apr 12, 2014
 *      Author: Abdallah Okasha
 */
#include <bits/stdc++.h>
using namespace std;
int T,c1,c2,k=0;
int main ()
{
    freopen ("A-small-attempt10.in","r",stdin);
    freopen ("output.txt","w",stdout);
    cin >> T;
    while (T--)
    {
        k++;
        cin >> c1;
        int v1[9][9],v2[9][9];
        for (int i=0; i<4; i++)
            for (int j=0; j<4; j++)
                cin >> v1[i][j];
        cin >> c2;
        for (int i=0; i<4; i++)
            for (int j=0; j<4; j++)
                cin >> v2[i][j];
        vector<int>v;
        for (int i=0; i<4; i++)
        {
            for (int j=0; j<4; j++)
                if (v1[c1-1][i]==v2[c2-1][j])
                    v.push_back(v1[c1-1][i]);
        }
        if ((int)v.size()==1)cout << "Case #" << k << ": " << v[0] << "\n";//Bad magician!
        if ((int)v.size()>1)cout << "Case #" << k << ": Bad magician!\n";
        if ((int)v.size()==0)cout << "Case #" << k << ": Volunteer cheated!\n";
    }
    return 0;
}
