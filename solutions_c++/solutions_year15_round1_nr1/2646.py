#include<iostream>
#include<fstream>
#include<vector>
#include<algorithm>

typedef std::pair<int,int> ii;
typedef std::vector <int> vi;
typedef std::vector <vi> vvi;
typedef std::vector <ii> vii;

int n_test_case;
vvi cases;
vii results;

int solvea(vi c);
int solveb(vi c);

int main()
{
    std::ifstream input("input.in");
    if(!input.eof())
    {
        input>>n_test_case;
        for(int i = 0; i < n_test_case; i++)
        {
            vi c;
            int n;
            input>>n;

            for(int j = 0; j < n; j++)
            {
                int m;
                input>>m;
                c.push_back(m);
            }
            cases.push_back(c);
        }
    }
    input.close();

    for(int i = 0; i < n_test_case; i++)
    {
        ii a;
        a.first = solvea(cases[i]);
        a.second = solveb(cases[i]);
        results.push_back(a);
    }

    std::ofstream output("output.txt");
    for(int i = 0; i < n_test_case; i++) output<<"Case #"<<i+1<<": "<<results[i].first<<" "<<results[i].second<<std::endl;
    output.close();
    return 0;
}

int solvea(vi c)
{
    int a = 0;
    for(int i = 0; i < c.size() -1; i++) if(c[i] > c[i+1]) a+=(c[i]-c[i+1]);
    return a;
}
int solveb(vi c)
{
    int a = 0;
    int x = 0;

    for(int i = 0; i < c.size() -1; i++) if(c[i] - c[i+1] > x) x = c[i] - c[i+1];

    for(int i = 0; i < c.size() -1; i++) a += std::min(c[i], x);
    return a;
}
