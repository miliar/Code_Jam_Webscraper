#include <iostream>
#include <cstdio>
#include <fstream>

using namespace std;

int main()
{
    freopen("a.in","r", stdin);
    freopen("a.out","w",stdout);
    int T;
    cin>>T;
    for(int ii = 1; ii <= T; ++ii){
        int bla;
        string sir;
        cin>>bla;
        cin>>sir;
        int nr = 0, total = 0;
        for(int i = 0; i < sir.size(); ++i){
            int cate = sir[i] - '0';
            if(cate == 0) continue;
            int lipsa = 0;
            if(nr < i)
                lipsa = i - nr;
            total += lipsa;
            nr += lipsa + cate;
        }
        cout<<"Case #"<<ii<<": "<<total<<endl;

    }

    return 0;
}
