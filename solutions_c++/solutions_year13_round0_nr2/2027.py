#include <iostream>
#include <vector>
#include <fstream>
using namespace std;


void dis(vector <int> vec)
{

  return ;
}


void dis(vector< vector <int> > vec,int loc)
{

}

bool pass(vector <int> vec,int ref)
{


    for(int i=0;i<vec.size();i++)
        if(vec[i]>ref){ return false;}

    return true;
}
bool pass(vector < vector <int> > vec,int ref,int loc)
{

    int i;
    for(int i=0;i<vec.size();i++)
    {
        if(vec[i][loc]>ref) {
            return false;}
    }
    return true;

}

string result(vector <  vector <int> > vec)
{


    int i,j;

    for(i=0;i<vec.size();i++)
        for(j=0;j<vec[i].size();j++)
        {
            //cout << "going for"<<i<<" "<<j<<"\n";
            if(!pass(vec[i],vec[i][j]) && !pass(vec,vec[i][j],j))
               { ;return "NO";


            }



            //if(!pass(vec,vec[i][j],j))
              //  return "NO";


        }
    return "YES";

}


int main()
{
    vector <int> oned,empty1d;
    vector < vector <int> > twod,empty2d;
    ifstream Cin("inp.in");
    ofstream Cout("out.in");

    int tc; Cin>>tc;
    int i,j,k,r,c,temp;

    for(i=0;i<tc;i++)
    {

        Cin>>r>>c;
        twod = empty2d; oned = empty1d;
        for(j=0;j<r;j++)
        {
            for(k=0;k<c;k++)
            {
                Cin>>temp;
                oned.push_back(temp);
                if(k==c-1) twod.push_back(oned);

            }
            oned = empty1d;
        }

        Cout<<"Case #"<<i+1<<": "<<result(twod)<<"\n";


    }

}
