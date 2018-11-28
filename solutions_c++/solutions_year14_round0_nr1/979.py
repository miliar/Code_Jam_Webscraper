#include <iostream>
#include <queue>
#include <cmath>
#include <iterator>
#include <algorithm>
#include <fstream>
#include <set>
#include <sstream>
using namespace std;





int main()
{
    ios_base::sync_with_stdio(false);
    ifstream in("input.txt");
    ofstream out("output.txt");
    #define cin in
    #define cout out
    int nb_cas;
    cin>>nb_cas;
    for(int cas=1;cas<=nb_cas;cas++)
    {
        cout<<"Case #"<<cas<<": ";
        int first;
        cin>>first;
        first--;
        vector<bool> possible(16,true);
        for(int c=0;c<4;c++)
        {
            for(int c2=0;c2<4;c2++)
            {
                int z;
                cin>>z;
                if(c!=first) possible[z-1]=false;
            }
        }
        cin>>first;
        first--;
        for(int c=0;c<4;c++)
        {
            for(int c2=0;c2<4;c2++)
            {
                int z;
                cin>>z;
                if(c!=first) possible[z-1]=false;
            }
        }
        int count = 0;
        int rep = 0;
        for(int c=0;c<possible.size();c++)
        {
            if(possible[c]) {rep = c+1;count++;}
        }
        if(count == 1)
        {
            cout<<rep<<endl;
        }
        else if(count == 0)
        {
            cout<<"Volunteer cheated!"<<endl;
        }
        else
        {
            cout<<"Bad magician!"<<endl;
        }
    }
}
