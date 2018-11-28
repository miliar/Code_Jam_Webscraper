#include <iostream>
#include <fstream>
#include <vector>
#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
using namespace std;
int check(vector<float> naomi1, vector<float> ken1);
int warmove(vector<float> naomi, vector<float> ken);
int main()
{
    ifstream input;
    input.open("large.txt");
    ofstream output;
    output.open("largeo.txt");
    int t;
    input>>t;
    for (int cse=1;cse<=t;cse++)
    {
        int n;
        input>>n;
        vector <float> naomi;
        vector <float> ken;
        vector <float> naomi1;
        vector <float> ken1;
        int wscore=0;
        int dscore=0;
        int i;
        for(i=0;i<n;i++)
        {
            float z;
            input>>z;
            naomi.push_back(z);
            naomi1.push_back(z);
        }
        for(i=0;i<n;i++)
        {
            float z;
            input>>z;
            ken.push_back(z);
            ken1.push_back(z);
        }
        sort(naomi.begin(),naomi.end());
        sort(naomi1.begin(),naomi1.end());
        sort(ken.begin(),ken.end());
        sort(ken1.begin(),ken1.end());
        i=0;
        while(check(naomi1,ken1)!=1&&i<n)
        {
            naomi1.erase(naomi1.begin());

            i++;
        }


        dscore=naomi1.size();

        i=0;
        while(i<n)
        {
            if (naomi[0]>ken[ken.size()-1])
            {
                wscore++;
            }
            int x=warmove(naomi,ken);
            if(x==-1)
            {
                naomi.erase(naomi.begin());
                ken.erase(ken.begin());
            }
            else
            {
                naomi.erase(naomi.begin());
                ken.erase(ken.begin()+x);
            }


            i++;
        }

        cout<<wscore<<" ";
        cout<<dscore<<endl;
        output<<"Case #"<<cse<<": "<<dscore<<" "<<wscore<<endl;



    }
    return 0;
}
int warmove(vector<float> naomi, vector<float> ken)
{
    if (naomi[0]>ken[ken.size()-1])
    {
        return -1;

    }
    int i=0;
    while(i<naomi.size())
    {


    if(naomi[0]<ken[i])
    {
        return i;
    }
    i++;
    }

}
int check(vector<float> naomi1, vector<float> ken1)
{

    for (int i=0;i<naomi1.size();i++)
    {
        if(naomi1[i]<ken1[i])
        {
            return 0;
        }
    }
    return 1;

}
