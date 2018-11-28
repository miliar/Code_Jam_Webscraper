#include <iostream>
#include <cstdlib>
#include <climits>
#include <algorithm>
#include <cstring>
#include <cmath>
#include <vector>
#include <set>
#include <map>
#include <iterator>
#include <string>
#include <fstream>

using namespace std;

typedef long long int64;

#define mp make_pair
#define pb push_back
#define ms0(x) memset(x,0,sizeof(x));
#define ms1(x) memset(x,-1,sizeof(x));

#define mod 1
#define EPS 1e-8

//------------------------------------------------------------------------//

string str;

int main(){
    ifstream fin;
    ofstream fout;

    fin.open("in.txt");
    fout.open("out.txt");

    int tst;
    fin >> tst;

    for(int t=1;t<=tst;t++){
        int n;
        fin >> n >> str;
        int cnt=0;
        int ret=0;
        for(int i=0;i<=n;i++){
            if(cnt>=i){
                cnt+= (int)(str[i]-'0');
            }else{
                ret= ret+ (i-cnt);
                cnt+= (i-cnt);
                cnt+= (int)(str[i]-'0');
            }
        }

        fout << "Case #" << t << ": " << ret << endl;
        str.clear();
    }
    fin.close();
    fout.close();
    return 0;
}
