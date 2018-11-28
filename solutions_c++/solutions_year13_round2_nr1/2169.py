#include <iostream>
#include <limits.h>
#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;
bool Compare (int i,int j) { return (i>j); }
int Solve(vector <int> Mots, int A)
{
    if(Mots.empty())
        return 0;
    if(A>Mots.back())
    {
            A+=Mots.back();
            Mots.pop_back();
            return Solve(Mots,A);
    }
    else if(A==1)
    {
        Mots.pop_back();
        return 1+Solve(Mots,A);
    }
    else
    {
        vector <int> Mots1(Mots);
        vector <int> Mots2(Mots);
        Mots1.push_back(A-1);
        Mots2.pop_back();
        return 1+min(Solve(Mots1,A),Solve(Mots2,A));
    }
}
int main()
{
    ifstream input("input.txt");
    ofstream output("output.txt");
    int T;
    input>>T;
     vector <int> Mots;
     cout<<T<<endl;
    for(int i=0;i<T;i++)
    {
        cout<<"i= "<<i<<endl;
        Mots.clear();
        int A,N;
        input>>A>>N;
        cout<<A<<" "<<N<<endl;
        for(int i=0;i<N;i++)
        {
            int x;
            input>>x;
            Mots.push_back(x);
        }

        sort(Mots.begin(),Mots.end(),Compare);
        for(int i=0;i<Mots.size();i++)
        {
            cout<<Mots[i]<<" ";
        }
        cout<<endl;
        output<<"Case #"<<i+1<<": "<<Solve(Mots,A)<<endl;
    }
    return 0;
}
