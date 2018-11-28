#include <bits/stdc++.h>
using namespace std;

ofstream out("precalc16.txt");
int cnt = 0;

int test(unsigned long long a, int base)
{
    unsigned long long c = 0;
    unsigned long long baseCalc = 1;
    while (a>0)
    {
        c += (a%2) * baseCalc;
        a/=2;
        baseCalc*=base;
    }

    int hue = sqrt(c);
    for (int i=2;i<=hue;i++)
        if (c%i == 0)
            return i;
    return -1;
}

void output(unsigned long long i, const vector<int>& answers)
{
    vector<bool> tmp;
    while (i>0)
    {
        tmp.push_back(i%2);
        i/=2;
    }

    for (int i=tmp.size()-1;i>=0;i--)
    {
        cout<<tmp[i];
        out<<tmp[i];
    }
    for (int i=0;i<answers.size();i++)
    {
        cout<<' '<<answers[i];
        out<<' '<<answers[i];
    }
    cout<<endl;
    out<<endl;

    cnt++;
}

int main()
{

    int t, N, J;
    in>>t>>N>>J;

    out<<"Case #1:"<<endl;

    unsigned long long start = (1 << 15) + 1, end = (1 << 16);
    for (unsigned long long i=start;i<end && cnt<50;i+=2)
    {
        //cout<<i<<endl;
        bool flag = true;
        vector<int> answers;
        for (int j=2;j<=10;j++)
        {
            answers.push_back(test(i, j));
            if (answers[answers.size()-1] == -1)
                flag = false;
        }
        if (flag == true)
            output(i, answers);
    }


    return 0;
}
