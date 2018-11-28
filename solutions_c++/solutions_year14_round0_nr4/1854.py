#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

typedef vector<double>::iterator double_iter;

int war(vector<double>& naomi,vector<double> ken)
{
    int score(0);
    for(double_iter i = naomi.begin();i != naomi.end();++i)
    {
        double_iter j;
        for(j = ken.begin();j !=ken.end() && *j < *i;++j)
        {

        }
        if(j == ken.end())
        {
            ++score;
            ken.erase(ken.begin());
        }
        else
            ken.erase(j);
    }

    return score;
}

int deceit_war(vector<double>& naomi,vector<double> ken)
{
    int score(0);

    int n(naomi.size());

    for(int i=0;i<n;++i)
    {
        if(naomi[i] > *ken.begin())
        {
            ken.erase(ken.begin());
            ++score;
        }
        else
        {
            ken.pop_back();
        }

    }

    return score;
}

int main()
{
    ifstream in("D-large.in");
    ofstream out("results.txt");

    int n_cases;
    int n_blocks;

    in >> n_cases;

    for(int i=0;i<n_cases;++i)
    {
        in >> n_blocks;


        vector<double> naomi,ken;
        double number;

        for(int j=0;j<n_blocks;++j)
        {
            in >> number;
            naomi.push_back(number);
        }

        for(int j=0;j<n_blocks;++j)
        {
            in >> number;
            ken.push_back(number);
        }

        sort(naomi.begin(),naomi.end());
        sort(ken.begin(),ken.end());

        out << "Case #"<<i+1<<": "<<deceit_war(naomi,ken)<<" "<<war(naomi,ken)<<endl;
    }

    return 0;
}
