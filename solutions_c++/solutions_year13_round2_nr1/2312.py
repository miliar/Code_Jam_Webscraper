#include <algorithm>  
#include <iostream>  
#include <iomanip>  
#include <fstream>  
#include <sstream>  
#include <string>  
#include <list>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
using namespace std;  

#define FOR(i,a,b) for(long i=(a);i<(b);++i)  
#define REP(i,n) FOR(i,0,n)  

int getStepsToReach(int a, int m)
{
    int r = 0;
    if((a==m) and (a>1)) return 1; 
    while(a<=m and (a>1))
    {
        a+= (a-1);
        ++r;
    }
    return r;
}

int main(int argc, char** argv)
{
    ifstream in;
    in.open(argv[1],ios::in);
    ofstream out;
    out.open(argv[2],ios::out);
    int N = 0;
    in>>N;
    cout << " Total  " << N <<endl;
    REP(caseN,N)
    {
        cout<<"solving case "<<caseN+1<<endl;
        int64_t a,n;
        in >> a >> n;


        vector<int64_t> mote;
        REP(mi,n)
        {
            int64_t t;
            in >> t;
            mote.push_back(t);
        }
        sort(mote.begin(),mote.end());

        int result = 0;
        REP(i,n)
        {
            cout <<" Iter " << i << " curr = " << a << " To eat == " << mote[i] << "\t\t";
            if(a > mote[i])
            {
                a+= mote[i];
                cout <<" Ate up \n";
                continue;
            }
            
            int stepsToReach = getStepsToReach(a,mote[i]);
            int numberLeft = n - i ;

                cout <<" steps = " << stepsToReach << " left = " << numberLeft;
            if((stepsToReach == 0) or (a<=1) or (numberLeft <= stepsToReach))
            {
                result += numberLeft;
                cout << "  Result finalized " << result <<endl;
                break;
            }
            else
            {
                for(int k = 0; k < stepsToReach; ++k)
                {
                    a+= (a-1);
                }
                if(a>mote[i])
                    a+=mote[i];
                else
                {
                    cout << "weird issue\n";
                    exit(1);
                }
                result += stepsToReach;
                cout << "  Result becomes " << result <<endl;
            }
        }
                
        out << "Case #"<<caseN+1<<": " << result << endl;

    }
        
    in.close();
    out.close();
    return 0;
}
