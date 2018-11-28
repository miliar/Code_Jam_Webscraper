#include <string>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <list>
#include <iomanip> 

using namespace std;

const double PI = 2 * acos(0);
const double eps = 1e-9;

//#define SMALL
#define LARGE
int main() {
#ifdef SMALL
	freopen("D-small-attempt0.in","rt",stdin);
	freopen("D-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("D-large.in","rt",stdin);
	freopen("D-large.out","wt",stdout);
#endif

	int n, N;

	cin >> N;
    string trash;
    getline(cin, trash);
    
    for (int nn = 1; nn<N+1; ++nn) {
        int resDW = 0;
        int resW = 0;

        vector<double> naomi = {};
        vector<double> kevin = {};

        cin >> n; // nb of blocks
        getline(cin, trash);

        string temp, s;
        getline(cin, temp);

        stringstream ss(temp);
        for (int i = 0; i<n; ++i){
            ss >> s;
            naomi.push_back(stof(s));
        }

        getline(cin, temp);

        stringstream ss2(temp);
        for (int i = 0; i<n; ++i){
            ss2 >> s;
            kevin.push_back(stof(s));
        }
        



        sort(naomi.begin(), naomi.end());
        sort(kevin.begin(), kevin.end());


        //cout << "naomi:";
        //for (int i =0; i<n; ++i){
            //cout << naomi[i] << " ";
        //}
        //cout << endl;

        //cout << "kevin:";
        //for (int i =0; i<n; ++i){
            //cout << kevin[i] << " ";
        //}
        /*cout << endl;*/

        int jk = 0;
        for (int i=0; i<n; ++i) {
            if (naomi[i] > kevin[jk]){
                resDW++;
                jk++;
            } 
        }


        int i = 0, j=0;
        while (i<kevin.size()){
            while (i < kevin.size() && kevin[i] < naomi[j]) {
                i++;
            }
            if (i == kevin.size()-1)
                break;
            i++;
            j++;
        }

        resW = i-j;

        cout<<"Case #" << nn << ": ";
        cout << resDW << " " << resW << endl;
    }
    return 0;
}

