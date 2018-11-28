#include <iostream>
#include <set>
#include <queue>
#include <stack>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <math.h>
#include <string>
#include <map>
#include <stdlib.h>
#include <sstream>
#include <memory.h>
#include <ctime>
//#include <fstream>
using namespace std;
 
using namespace std;

#define INF 1000000000
#define MP make_pair
#define FILL(a,value) memset(a,value,sizeof(a))
double const PI = acos(-1.0);
double const EPS=1e-7;


int p[1000][1000];

double d[1000][1000];
double d2[1000][1000];

int getIntersection(string& s){
    for (int i=1; i<s.length(); i++){
        bool ok = true;
        for (int j=0; j<s.length()-i; j++){
            if (s[j] != s[i+j]) ok = false;
        }
        if (ok)
            return s.length()-i;
    }
    return 0;
}

int getPref(string& s1, string& s2){

    if (s1.length() > s2.length()) s1.erase(s1.begin());

    for (int i=0; i<s1.length(); i++){
        bool ok = true;
        for (int j=0; j<s1.length()-i; j++){
            if (s1[i+j] != s2[j]) ok=false;
        }
        if (ok) return s1.length()-i;
    }
    return 0;
}

bool isOk(string& s1, string& s2){
    for (int i=0; i<s1.length(); i++){
        bool ok = false;
        for (int j=0; j<s2.length(); j++){
            if (s1[i] == s2[j]) ok=true;

        }
        if (!ok) return false;
    
    }
    return true;
}

void solve(){

 /*   int k, n, m;
    cin>>k>>n>>m;
    string s1;
    cin>>s1;
    string s; 
    cin>>s;
    int p = 1;
    for (int i=0; i<m; i++){
        p *= s1.length();
    }

    int mm = 0;
    double res = 0;

    for (int i=0; i<p; i++){
        int x = i;
        string ss = "";
        for (int j=0; j<m; j++){
            int c = x % s1.length();
            x/=s1.length();

            ss += s1[c];
        }

        int cnt = 0;
        for (int j=0; j<ss.length(); j++){
            if (j + s.length() - 1 >=ss.length()) continue;
            bool ok = true;
            for (int k=0; k<s.length(); k++){
                if (ss[j+k] != s[k]) ok=false;
            }
            cnt+=ok;
        }

        mm= max(mm,cnt);
        res += cnt;

    }

    res = res / (double)p;
    res = mm - res;
    printf("%d %.9f\n",mm, res);*/

    int k, n, m;
    cin>>k>>n>>m;
    string s1;
    cin>>s1;
    string s;
    cin>>s;

    if (!isOk(s, s1)){
        cout<<"0.0"<<endl;
        return;
    }

    int c = getIntersection(s);

    int x = s.length();
    int cnt = 0;
    while(x<=m){
        cnt ++;
        x += s.length()-c;
    }


    for (int i=0; i<=s.length(); i++){
        for (int j=0; j<s1.length(); j++){
            string ss;
            for (int k=0; k<i; k++){
                ss += s[k];
            }

            ss += s1[j];

            int P = getPref(ss, s);

            p[i][j] = P;

        }
    }


    for (int i=0; i<=m; i++){
        for (int j=0; j<=s.length(); j++){
            d[i][j] = 0.0;
            d2[i][j] = 0.0;
        }
    }


    d[0][0] = 0;
    d2[0][0] = 1;

    for (int i=0; i<m; i++){
        for (int j=0; j<=s.length(); j++){
            for (int k=0; k<s1.length(); k++){
                int P = p[j][k];

                d2[i+1][P] += d2[i][j] / (double)s1.length();

                if (P == s.length()) d[i+1][P] += (d[i][j] + d2[i][j])/ (double)s1.length();
                else d[i+1][P] += d[i][j] ;
            }
        }
    }

    double res = 0;
    //for (int j=0; j<=s.length(); j++){
    //    res += d[m][j];
    //}

    for (int i=1; i<=m; i++){
        res += d2[i][s.length()];
    }

    res = cnt - res;

    printf("%.9f\n", res);
    

}

int main(){

	freopen("in.txt","r",stdin);
	freopen("OUTPUT.txt","w",stdout);

	int tt;
	cin>>tt;

	//string str;
	//getline(cin,str);

	for (int t=1; t<=tt; t++){
        if (t==15){
            int k = 0;
        }
		cout<<"Case #"<<t<<": ";
		int time=clock();
		solve();
		cerr<<"\t\tCase #"<<t<<"\t time="<<clock()-time<<endl;
	}

}