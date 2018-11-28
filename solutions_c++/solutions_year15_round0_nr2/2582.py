#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <math.h>

using namespace std;

int d;

ifstream fin("input.txt");
ofstream fout("output.txt");

int find_minimum(vector<int> diners)
{
    int max=*max_element(diners.begin(),diners.end());

    if(max==1 || max==2 || max==3)
        return max;
    else
    {
        int x=max;

        int count=0;

        vector<int> diner1;
        vector<int> diner2;

        for(int i=0;i<diners.size();i++)
        {
            if(diners[i]==max)
            {
                count++;

                int val=ceil(sqrt(max));

                diner1.push_back(val);
                diner1.push_back(max-val);

                if(max%2==1)
                {
                    int val=max/2;

                    diner2.push_back(val);
                    diner2.push_back(val+1);
                }
                else
                {
                    int val=max/2;

                    diner2.push_back(val);
                    diner2.push_back(val);
                }
            }
            else
            {
                diner1.push_back(diners[i]);
                diner2.push_back(diners[i]);
            }
        }

        int y=count+find_minimum(diner1);
        int z=count+find_minimum(diner2);

        if(x<y)
        {
            if(x<z)
                return x;
            else
                return z;
        }
        else
        {
            if(y<z)
                return y;
            else
                return z;
        }
    }

}

int main()
{
    int test;

    fin>>test;

    for(int j=1;j<=test;j++)
    {
        vector<int> diners;

        fin>>d;
        diners.clear();

        for(int i=0;i<d;i++)
        {
            int x;
            fin>>x;

            diners.push_back(x);
        }

        int ans=find_minimum(diners);

        fout<<"Case #"<<j<<": "<<ans<<endl;
    }

    return 0;
}
