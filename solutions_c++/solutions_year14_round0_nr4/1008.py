#include <iostream>
#include <queue>
#include <cmath>
#include <iterator>
#include <algorithm>
#include <fstream>
#include <set>
#include <sstream>
#include <iomanip>
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
    for(int cas = 0; cas < nb_cas; cas++)
    {
        cout<<"Case #"<<cas+1<<": ";
        int N;
        cin>>N;
        vector<double> v1(N),v2(N);
        for(int c=0;c<N;c++) cin>>v1[c];
        for(int c=0;c<N;c++) cin>>v2[c];
        sort(v1.begin(),v1.end());
        sort(v2.begin(),v2.end());
        //cout<<endl;
        //for(int c=0;c<v1.size();c++) cout<<v1[c]<<" ";
        //cout<<endl;
        //for(int c=0;c<v1.size();c++) cout<<v2[c]<<" ";
        //cout<<endl;
        int co1 = 0,co2 = 0;
        int j = 0;
        for(int c=0;c<N;c++)
        {
            for(;j<N&&v2[j]<v1[c];j++) ;
            if(j>=N) co2++;
            j++;
        }
        //reverse(v2.begin(),v2.end());
        for(int c=0;c<=N;c++)
        {
            for(int c2=c;c2<N;c2++)
            {
                if(v2[c2-c]>v1[c2]) goto nop;
            }
            co1 = N-c;
            break;
            nop:;
        }
        cout<<co1<<" "<<co2<<endl;
    }
}
