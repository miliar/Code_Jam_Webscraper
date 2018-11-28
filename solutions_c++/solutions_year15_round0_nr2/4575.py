#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

int digtoint(char c)
{
    switch(c)
    {
        case '1':
            return(1);
        case '2':
            return(2);
                case '3':
            return(3);
                    case '4':
            return(4);
                    case '5':
            return(5);
                    case '6':
            return(6);
                    case '7':
            return(7);
                    case '8':
            return(8);
                    case '9':
            return(9);
                    case '0':
            return(0);

    }
    return -1;
}


int cost(vector<int> steps,vector<int> ps)
{
    if(*max_element(ps.begin(),ps.end())<=3)
        return *max_element(ps.begin(),ps.end());
    else
    {
        auto n=steps.size();
        for(auto i=0; i<n;i++)
        {
            int s=steps[i];
            auto maxpos=max_element(ps.begin(),ps.end());
            int maxval=*maxpos;
            if(maxval-s<s)
                return 10;
            int pn1=maxval-s;
            int pn2=s;
            ps.erase(maxpos);
            ps.push_back(pn1);
            ps.push_back(pn2);
        }
        return n+*max_element(ps.begin(),ps.end());
    }
}

vector<vector<int>> genseqs(int smax,int n)
{
//generates all seqs of length <=n with with entries from 1 to smax
    vector<vector<int>> seqs;
    for(auto i=1;i<=smax;i++)
    {
        vector<int> adn{i};
        seqs.push_back(adn);
    }
    for(auto i=2;i<=n;i++)
    {
        int sz=seqs.size();
        for(int k=0;k<sz;k++)
        {
            if(seqs[k].size()==i-1)
            {

                for(int j=1;j<=smax;j++)
                {
                    vector<int> vec{seqs[k]};
                    vec.push_back(j);
                    seqs.push_back(vec);
                }
            }

        }
    }
    return seqs;
}

int mincost(vector<int> ps)
{
    if(*max_element(ps.begin(),ps.end())<=3)
        return *max_element(ps.begin(),ps.end());
    else
    {
        int smax=(int)((*max_element(ps.begin(),ps.end()))/2);
        auto seqs=genseqs(smax,*max_element(ps.begin(),ps.end())-1);
        int min_cost=*max_element(ps.begin(),ps.end());
        for(auto seq:seqs)
        {
            min_cost=min(min_cost,cost(seq,ps));
        }
        return min_cost;
    }
}

int main()
{
    ifstream in("in.in");
    ofstream out("out.txt");
    string line;
    getline(in,line);
    //cout<<line<<"combuccha";
    int T=stoi(line.c_str());
    //cout<<"t="<<T;
    vector<int> ps;
    int D;
    int pos;
    int len;
    int mincst;
    int newpos;
    for(auto i=1; i<=T; i++)
    {
        ps.clear();
        getline(in,line);
        D=stoi(line);
        getline(in,line);
        ps.push_back(digtoint(line[0]));
        pos=line.find_first_of(' ');
        for(int i=2; i<=D;i++)
        {
            newpos=line.find_first_of(' ',pos+1);
            ps.push_back(digtoint(line[pos+1]));
            pos=newpos;
        }
        out<<"Case #"<<i<<": "<<mincost(ps)<<endl;
    }
}
