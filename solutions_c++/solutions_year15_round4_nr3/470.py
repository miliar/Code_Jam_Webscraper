#include <iostream>
#include <vector>
#include <cstdio>
#include <set>
#include <set>
#include <map>
#include <fstream>
#include <algorithm>
#include <map>
#include <unordered_map>
#include <queue>
#include <sstream>


using namespace std;

int t;
int n;
vector<string> v[21];
unordered_map<string, int> angol;
unordered_map<string, int> francia;

bool mi[21];

int main()
{
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    cin >> t;

    for (int ttt=1;ttt<=t;ttt++) {
        angol.clear();
        francia.clear();
        cout << "Case #" << ttt<<": ";

        cin >> n;
        string str;
        getline(cin, str);
        for (int i=0;i<n;i++) v[i].clear();

        for (int i=0;i<n;i++) {
            getline(cin, str);
            istringstream ss(str);
            string xxx;
            while(ss >> xxx)
            {
                v[i].push_back(xxx);
            }
            mi[i]=false;
        }
        mi[0]=false;
        mi[1]=true;
        for (int j=0;j<n;j++) {
            if (!mi[j]) {
                for (int k=0;k<v[j].size();k++) angol[v[j][k]]++;
            }
            else {
                for (int k=0;k<v[j].size();k++) francia[v[j][k]]++;
            }
        }
        int mini=1000000;
        for (long long szam=0; szam<(1<<(n-2)); szam++) {
            int ccc=0;
            long long ss=szam;
            for (int j=2;j<n;j++) {
                if ((ss%2==0) && mi[j]) {
                    for (int k=0;k<v[j].size();k++) angol[v[j][k]]++;
                    for (int k=0;k<v[j].size();k++) {
                        francia[v[j][k]]--;
                        if (francia[v[j][k]]==0) francia.erase(v[j][k]);
                    }
                }
                if ((ss%2==1) && !mi[j]) {
                    for (int k=0;k<v[j].size();k++) francia[v[j][k]]++;
                    for (int k=0;k<v[j].size();k++) {
                        angol[v[j][k]]--;
                        if (angol[v[j][k]]==0) angol.erase(v[j][k]);
                    }
                }



                if (ss%2==0) mi[j]=false;
                else mi[j]=true;
                ss/=2;
            }

            for (unordered_map<string, int>::iterator it=francia.begin();it!=francia.end();it++) {
                if (angol.find(it->first)!=angol.end()) {
                    ccc++;
                }
            }
            mini=min(mini, ccc);
        }
        cout << mini<<endl;
    }


    return 0;
}
