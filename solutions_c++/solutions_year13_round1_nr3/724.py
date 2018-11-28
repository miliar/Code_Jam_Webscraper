#include <iostream>
#include <vector>
#include <algorithm>
#include <fstream>
#include <sstream>
#include <istream>
#include <algorithm>
#include <queue>
#include <cmath>
#include <map>
#include <list>
#include <cstdio>
#include <set>
#include <iomanip>
#include <stack>
#include <ctime>
#include <climits>
#include <iterator>

#define LOCAL
#ifdef ONLINE_JUDGE
#define COUT(s)
#undef LOCAL
#endif

#define cin in

#ifdef LOCAL
#define COUT(s) cout<<"-----"<<s<<"-----"<<endl;
#endif

using namespace std;

bool possible(int n,vector<int> &contient,int indice)
{
    if(n==1)   return true;
    if(indice>=contient.size()) return false;
    return possible(n,contient,indice+1)||(n%contient[indice]==0&&possible(n/contient[indice],contient,indice+1));
}


int main(int argc,char **argv)
{
    ifstream in("input.txt");
    ofstream out("output.txt");

    int nb_cas;
    cin>>nb_cas;
    for(int c=1;c<=nb_cas;c++)
    {
        out<<"Case #"<<c<<": "<<endl;
        int R,N,M,K;
        cin>>R>>N>>M>>K;
        cout<<R<<" "<<N<<" "<<M<<" "<<K<<endl;
        for(int c=0;c<R;c++)
        {
            vector<int> v(K);
            for(int c2=0;c2<K;c2++)
            {
                cin>>v[c2];
            }
            sort(v.begin(),v.end());
            vector<bool> possibles(M+1,true);
            possibles[0]=possibles[2]=false;
            vector<int> choix;
            for(int c2=2;c2<=M;c2++)
                choix.push_back(c2);
            cout<<choix.size()<<endl;
            for(int c2=0;c2<pow((double)choix.size(),N);c2++)
            {
                cout<<c2<<endl;
                int temp=c2;
                vector<int> contient;
                while(temp!=0)
                {
                    contient.push_back(choix[temp%choix.size()]);
                    cout<<contient.back()<<" ";
                    temp/=choix.size();
                }
                cout<<endl;
                if(contient.size()!=N)
                    continue;
                for(int c3=0;c3<K;c3++)
                {
                    if(!possible(v[c3],contient,0))
                        goto nop;
                }
                for(int c3=0;c3<N;c3++)
                {
                    out<<contient[c3];

                }
                break;
                nop:;
                if(c2+1==pow((double)choix.size(),N))
                {
                    for(int c3=0;c3<N;c3++)
                        out<<2;
                }
            }
            out<<endl;
        }
    }
}
