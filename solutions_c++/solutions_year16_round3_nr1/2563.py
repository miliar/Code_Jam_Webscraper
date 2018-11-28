#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <fstream>
#define maxSegSize 3000000

using namespace std;

int main(){
    ios_base::sync_with_stdio(false);

    ifstream fin;
    fin.open("in.txt", ios_base::in);
    ofstream fout;
    fout.open("out.txt", ios_base::out);

    int t, T;
    fin>>T;
    for(t=0;t<T;t++){

        int n;
        fin>>n;

        vector<pair<int, int>> s(n);
        int i;
        for(i=0;i<n;i++){
            pair<int, int> p;
            fin>>p.first;
            p.second = i;
            s[i] = p;
        }
        fout<<"Case #"<<t+1<<": ";
        sort(s.begin(), s.end());

        if(s.size()%2!=0){
            while(s[0].first!=0){
                if(s[n-1].first!=s[n-2].first) {
                    fout << (char) ('A' + s[0].second) << (char) ('A' + s[n - 1].second) << " ";
                    s[n - 1].first--;
                    s[0].first--;
                }
                else{
                    fout << (char) ('A' + s[0].second)<<" ";
                    s[0].first--;
                }
                sort(s.begin(), s.end());
            }
        }

        while(s[n-1].first!=0){
            if(s[n - 1].first == s[n-2].first){
                fout << (char) ('A' + s[n - 1].second) << (char) ('A' + s[n-2].second) << " ";
                s[n - 1].first--;
                s[n-2].first--;
            }
            else{
                fout << (char) ('A' + s[n - 1].second) <<" ";
                s[n - 1].first--;
            }
            sort(s.begin(), s.end());
        }
        fout<<endl;

    }

    fin.close();
    fout.close();

    return 0;
}