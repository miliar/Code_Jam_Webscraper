#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<cstdio>
#include<set>
#include<map>
#include<climits>
#include<cstring>
#include<list>
#include<fstream>
#include<queue>
#include<sstream>
#include<stack>
#include<iomanip>

using namespace std;
typedef long long LL;

LL mod=1e9+7;

int K, C, S;

int main()
{

    ios_base::sync_with_stdio(false);
    cin.tie(0);


    ifstream cin("D-small-attempt0.in");
    ofstream cout("file.txt");

    int T;
    cin>>T;

    for(int I=0; I<T; I++)
    {
       cin>>K>>C>>S;

       cout<<"Case #"<<I+1<<": ";

       LL temp= pow(K, C-1);

       LL st=1;

       for(int i=0; i<K; i++)
       {
           cout<<st<<' ';
           st+=temp;
       }

       cout<<'\n';

    }
}

