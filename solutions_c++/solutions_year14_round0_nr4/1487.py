#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <iomanip>
using namespace std;

//const int NMAX = 10;
//int naomi[NMAX];
//int ken[NMAX];

int deceitwar(vector<double> naomi, vector<double> ken, int N)
{
    sort(naomi.begin(), naomi.end());
    sort(ken.begin(), ken.end());
    int counter=0;
    for(int i=N-1;i>=0;i--)
    {
        if(ken[i]>naomi[i])
        {
            naomi.erase(naomi.begin());
            ken.pop_back();
        }else
        {
            counter++;
            naomi.pop_back();
            ken.pop_back();
        }
    }
    return counter;
}

int war(vector<double> naomi, vector<double> ken, int N)
{
    sort(naomi.begin(), naomi.end());
    sort(ken.begin(), ken.end());
    int counter=N;
    for(int i=(N-1), j=(N-1);i>=0 && j>=0;j--)
    {
        if(ken[i]>naomi[j])
        {
            counter--;
            i--;
        }
    }
    return counter;
}

void print(vector<double> myvector, int N)
{
        for(int j=0;j<N;j++)
        {
            cout << myvector[j] << " ";
        }
        cout << endl;
}

int main()
{
    ifstream fin("war.in");
    ofstream fout("war.out");
    int cases, N, ans1, ans2;
    double tmp;
    vector<double> naomi;
    vector<double> ken;
    fin >> cases;
    for(int i=0;i<cases;i++)
    {
        naomi.clear();
        ken.clear();
        fin >> N;
        for(int j=0;j<N;j++)
        {
            fin >> tmp;
            naomi.push_back(tmp);
        }
        for(int j=0;j<N;j++)
        {
            fin >> tmp;
            ken.push_back(tmp);
        }
        ans1 = deceitwar(naomi,ken,N);
        ans2 = war(naomi, ken, N);
        fout << "Case #" << i+1 << ": " << ans1 << " " << ans2 << endl;
       // cout << "Case #" << i+1 << ": " << ans1 << " " << ans2 << endl;
    }

    return 0;
}
