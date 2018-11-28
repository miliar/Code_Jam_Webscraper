//1a

#include <iostream>
#include <cstdio>
#include <cmath>
#include <map>
#include <vector>
#include <list>
#include <algorithm>

#define whileinf while(true)
#define vitr(v,i) for((i) = (v).begin();(i) != (v).end();++i)


using namespace std;

int main(){

    //variable decleration here
    int T,l;
    string s,opt;

 //   freopen("A-large.in","r",stdin);
  //  freopen("a.out","w",stdout);

    cin >> T;

    //do the logic here
    cin.ignore();
    for(int i=1;i<=T;i++){
        cin >> s;
        l = s.length();
        opt = s[0];
        for (int j=1;j<l;j++){
            if(s[j] >= opt[0])
                opt = s[j] + opt;
            else
                opt = opt + s[j];
        }

        cout <<"Case #"<<i<<": " << opt << endl;
    }

    return 0;
}
