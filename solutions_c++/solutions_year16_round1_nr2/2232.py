#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <queue>
#include <stack>
#include <utility>
#include <set>
#include <string>

using namespace std;

int lincol[100][50];
int N;
bool done[100];

bool found;


int chosen[50];
int notChosen[50]; //TODO
pair<int, int> idInv[50];


int res[50];


void gen(int pos)
{
    if (found)
        return;
    if (pos == N)
    {

        //cout << "lol" << endl;
        //for (int i = 0; i < N; i++)
        //    cout << chosen[i] << "==>" <<notChosen[i] << '\t';
        bool ok = true;
        for (int i = 0; ok && i < N; i++)
        {
            if (notChosen[i] == -1)
            {
                for (int j = 0; j < N; j++)
                    res[j] = lincol[chosen[j]][i];

            }
            else
            {

               // cout << "lal" << endl;
                for (int j = 0; j < N; j++)
                {
                    if (lincol[notChosen[i]][j] != lincol[chosen[j]][i])
                    {
                  //      cout << "MAIS" << lincol[notChosen[i]][j] << "=>" << lincol[chosen[i]][j] << endl;
                        return;
                    }
                }
            }
        }

        if (ok)
        {
          //  cout << "COOL" << endl;
            found = true;
        }

    }

    else
    {
        int prev = chosen[pos-1];
        if (idInv[pos].second == -1)
        {
            bool ok = true;
            int i1 = idInv[pos].first;
            for (int i = 0; i < N; i++)
            {
                if (lincol[i1][i] <= lincol[prev][i])
                {
                    return;
                }
            }

            chosen[pos] = idInv[pos].first;
            notChosen[pos] = idInv[pos].second;
            gen(pos+1);
        }
        else
        {
            bool ok = true;
            int i1 = idInv[pos].first;
            for (int i = 0; i < N; i++)
            {
                if (lincol[i1][i] <= lincol[prev][i])
                {
                    ok = false;
                    break;
                }
            }

            if (ok)
            {
                chosen[pos] = i1;
                notChosen[pos] = idInv[pos].second;

                gen(pos+1);

                bool ok2 = true;
                int i2 = idInv[pos].second;
                for (int i = 0; i < N; i++)
                {
                    if (lincol[i2][i] <= lincol[prev][i])
                    {
                        return;
                    }
                }

                    chosen[pos] = i2;
                    notChosen[pos] = idInv[pos].first;
                    gen(pos+1);



            }
            else
            {
                bool ok2 = true;
                int i2 = idInv[pos].second;
                for (int i = 0; i < N; i++)
                {
                    if (lincol[i2][i] <= lincol[prev][i])
                    {
                        ok2 = false;
                        break;
                    }
                }
                if (ok2)
                {
                    chosen[pos] = i2;
                    notChosen[pos] = idInv[pos].first;
                    gen(pos+1);
                }
            }
        }

    }
}




int main()
{
    cin.tie(0);
    ios::sync_with_stdio(false);
    freopen("t.in", "r", stdin);
    freopen("t.out", "w", stdout);


    int nbT;
    cin >> nbT;



    for (int t = 1; t <= nbT; t++)
    {
        cin >> N;

        for (int i = 0; i < 2*N-1; i++)
        {
            done[i] = false;
            for (int j = 0; j < N; j++)
                cin >> lincol[i][j];
        }

        for (int pos = 0; pos < N; pos++)
        {
            int mini = 4000;
            int i1 = -1, i2 = -1;
            for (int i = 0; i < 2*N-1; i++)
            {
                if (done[i])
                    continue;
                if (lincol[i][pos] < mini)
                {
                    mini = lincol[i][pos];
                    i1 = i;
                    i2 = -1;
                }
                else if (lincol[i][pos] == mini)
                    i2 = i;
            }
            done[i1] = true;
            if (i2 != -1)
                done[i2] = true;

            idInv[pos] = make_pair(i1, i2);

            found = false;
            if (idInv[0].second ==-1)
            {
                chosen[0] = idInv[0].first;
                notChosen[0] = -1;
                gen(1);
            }
            else
            {

                chosen[0] = idInv[0].first;
                notChosen[0] = idInv[0].second;
                gen(1);
                if (!found)
                {
                    chosen[0] = idInv[0].second;
                    notChosen[0] = idInv[0].first;
                    gen(1);
                }
            }

        }


       /* for (int i = 0; i < N; i++)
            cout << idInv[i].first << "==>" << idInv[i].second << endl;
*/
        cout << "Case #" << t << ":";
        for (int i = 0; i < N; i++)
            cout << ' '<< res[i] << ' ';
        cout << '\n';
    }


    return 0;
}
