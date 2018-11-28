#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <list>
#include <sstream>
#include <ctime>
#include <queue>
#include <iomanip>
#define DEBUG2

using namespace std;

const long long mod = 1000002013;

struct voyage
{
    long long int dep;
    long long int arr;
    long long int nb;
    voyage(){}
    voyage(int a,int b,int c):dep(a),arr(b),nb(c){}
};


bool comparaison(const voyage &v1,const voyage &v2)
{
    if(v1.dep!=v2.dep) return v1.dep < v2.dep;
    return v1.arr < v2.arr;
}

long long cost(long long int dep,long long int arr,long long int N)
{
    long long int dist = arr-dep;
    return dist * (2 * N - dist + 1) / 2;
}

class bla
{
    public:
    template<typename T>
    bool operator()(const T &p1,const T &p2)
    {
        return p1>p2;
    }
};



int main()
{
#define cin in
#define cout out
    ifstream in("input.txt");
    ofstream out("output.txt");
    int nb_cas;
    cin>>nb_cas;

    for(int cas = 0;cas<nb_cas;cas++)
    {
        cout<<"Case #"<<cas+1<<": ";
        int N,S;
        cin>>N>>S;
        vector<int> v(N);
        for(int c=0;c<N;c++) cin>>v[c];
        sort(v.rbegin(),v.rend());
        int gauche = 0, droite = N;
        while(gauche != droite)
        {
            int mid = (gauche+droite)/2;
            bool val = true;
            for(int c=mid;c<v.size();c++)
            {
                if(v[c]+v[v.size()-1-(c-mid)]>S)
                {
                    val = false;
                    break;
                }
            }
            if(val)
            {
                droite = mid;
            }
            else
            {
                gauche = mid+1;
            }
        }
        cout<<gauche+(v.size()-gauche+1)/2<<endl;
    }


}
