#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <vector>
#include <stack>
#include <utility>
#include <fstream>
#include <iomanip>
#include <algorithm>

using namespace std;

vector <float> Naomi;
vector <float> Ken;

int war()
{
    int win = 0;
    while(!Naomi.empty())
    {
        if(Naomi[Naomi.size()-1] > Ken[Ken.size()-1])
        {
            win++;
            Naomi.pop_back();
            Ken.erase(Ken.begin());
        }
        else
        {
            int i = Ken.size()-1;
            while(i > 0 && Ken[i] > Naomi.size()-1)
            {
                i--;
            }
            Ken.erase(Ken.begin()+i);
            Naomi.pop_back();

        }
    }

    return win;
}

int war2()
{
    int win = 0;
    while(!Naomi.empty())
    {
        if(Naomi[Naomi.size()-1] > Ken[Ken.size()-1])
        {
            win++;
            Naomi.pop_back();
            Ken.pop_back();
        }
        else
        {
            int i = Ken.size()-1;
            while(i > 0 && Ken[i] > Naomi.size()-1)
            {
                i--;
            }
            Ken.erase(Ken.begin()+i);
            Naomi.pop_back();

        }
    }

    return win;
}

int main()
{
    ifstream cin ("in.txt");
   ofstream cout ("out.txt");

    int T = 0;
    cin >> T;

    cout.precision(10);
    cin.precision(10);


    for(int i = 1; i <= T; i++)
    {
        int N;
        cin >> N;
        for(int i = 0; i < N; i++)
        {
            float p;
            cin >> p;
            Naomi.push_back(p);
        }
         for(int i = 0; i < N; i++)
        {
            float p;
            cin >> p;
            Ken.push_back(p);
        }

        sort(Naomi.begin(), Naomi.end());
        sort(Ken.begin(), Ken.end());

        vector <float> temp1;
        vector <float> temp2;
        temp1 = Naomi;
        temp2 = Ken;

        bool flag = true;

        int rep2 = war();

        Naomi = temp1;
        Ken = temp2;

        temp1 = Naomi;
        temp2 = Ken;

        int maxi = max(0, war2());

        Naomi = temp1;
        Ken = temp2;

        while(flag)
        {
            if(Naomi.size() <2)
            {
                flag = false;
            }
            else if(Naomi[0] > Ken[Ken.size()-1] || Naomi[0] > Ken[Ken.size()-2])
            {
                flag = false;
            }
            else
            {
                N--;
                Naomi.erase(Naomi.begin());
                Ken.pop_back();
            }

            temp1 = Naomi;
            temp2 = Ken;

            maxi = max(maxi, war2());

            Naomi = temp1;
            Ken = temp2;
        }

        cout << "Case #" << i << ": " << max(maxi, war2()) <<" " << rep2<< endl;

    }





    return 0;
}
