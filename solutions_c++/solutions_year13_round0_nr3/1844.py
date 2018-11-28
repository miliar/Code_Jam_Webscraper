#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

bool pal(long long int i)
{
    std::string s = std::to_string(i);
    if( equal(s.begin(), s.begin() + s.size()/2, s.rbegin()) )
         return 1;
     else
         return 0;

}

int main()
{
    ifstream Cin("inp.in");
    ofstream Cout("op.in");

    long long int i,a,sqres;
    vector < long long int > vec;

    for(i=0;i<=10000000;i++)
    {
        if(pal(i))
        {
            sqres = i*i;
            if(pal(sqres))
            {
                vec.push_back(sqres);
         //       cout << sqres<<"\n";
            }
        }
    }

    long long int tc,A,B,res,j;Cin>>tc;
    for(i=0;i<tc;i++)
    {
        Cin>>A>>B;
        res=0;
        for(j=0;j<vec.size();j++)
        {
            if(vec[j]>=A && vec[j]<=B) res++;
        }
        Cout <<"Case #"<<i+1<<": "<<res<<"\n";
    }







}
