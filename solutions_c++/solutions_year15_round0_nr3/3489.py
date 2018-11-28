#include<iostream>
#include<queue>
#include<algorithm>
#include<vector>
#include <map>
#include <set>
using namespace std;

#define all(v) (v).begin(), (v).end()
#define rall(v) (v).rbegin(), (v).rend()
#define sz size()
#define pb push_back
#define mp make_pair
#define fr(i, n) for(i=0;i<n;i++)
#define fr2(i, a, n) for(i=a;i<n;i++)
#define mem(a, n) memset(a, n, sizeof(a))
typedef vector<int> VI;
typedef long long LL;
//int m[256][256];
//int s[256][256];
bool sign;
string myreplace(string &s) {
    string a;
    for (int i = 0; i < s.size(); i++) {
        if(s[i] == '1')
            continue;
        if(s[i]=='-') {
        	sign = !sign;
        	continue;
        }    
        a += s[i];
     }
     return a;
}
int main() {
/*    m[1][1] = 1;
    s[1][1] = 1;
    m[1]['i'] = 'i';
    s[1]['i'] = 1;
    m[1]['j'] = 'j';
    s[1]['j'] = 1;
    m[1]['k'] = 'k';
    s[1]['k'] = 1;
    m['i']['i'] = m['j']['j'] = m['k']['k'] = 1;
    s['i']['i'] = s['j']['j'] = s['k']['k'] = 1;
    s['i'][1] = 'i';
    s['i'][1] = 1;
    m['i']['k'] = 'k'; 
    s['i']['k'] = 1;
    m['i'][''] = ' '; 
    s['i'][1] = 1;
*/
    map<string, string> m;
    m["ij"] = "k";
    m["jk"] = "i";
    m["ki"] = "j";
    m["ji"] = "-k";
    m["kj"] = "-i";
    m["ik"] = "-j";
    m["i"] = "i";
    m["j"] = "j";
    m["k"] = "k";
    m["ii"] = m["jj"] = m["kk"] = "-1";
    int tests;
    cin >> tests;
    for (int t = 0; t<tests; t++) {
        int l, n, x;
        cin >> l >> x;
        string s;
        cin >> s;
        string res;
        string tmp;
        for (int i = 0 ; i < x; i++) {
            tmp += s;    
        }
        s = tmp; 
        tmp.clear();
        n = s.size();
        string c = "1";
    	sign = 1;
        bool ii = 0;
        bool jj = 0;
        bool kk = 0;
        int i = 0;
        for(i = 0; i < n; i++) {
            char ch = s[i];
            c += ch;
            
            c = myreplace(c);
            //cout << c << " " << sign << endl;
            if(m.find(c) != m.end()) {
                c = m[c];
                            c = myreplace(c);

           //     cout << "found: " << c << " " << sign << endl;
                
                if(c=="i") {
                    if(sign) {
                        i++;//cout << c << endl;
                        ii = 1;
                        break;
                    }    
                }    
            }  
            
        }
        c = "1";
        sign = 1;
        for(; i < n; i++) {
            char ch = s[i];
            c += ch;
            c = myreplace(c);
              //          cout << c << " " << sign << endl;

            if(m.find(c) != m.end()) {
                c = m[c];
                            c = myreplace(c);
                //cout << "found: " << c << " " << sign << endl;

                if(c=="j") {
                    if(sign) {
                    i++;
                        jj = 1;
                        break;
                    }    
                }    
            }  
            
        }
        c = "1";
        sign = 1;
        for(; i < n; i++) {
            char ch = s[i];
            c += ch;
            c = myreplace(c);
                  //      cout << c << " " << sign << endl;

            if(m.find(c) != m.end()) {
                c = m[c];
                            c = myreplace(c);
                //cout << "found: " << c << " " << sign << endl;

                if(c=="k") {
                    if(sign) {
                    	if(i==n-1)
                        	kk = 1;
                    }    
                }    
            }  
            
        }

        if (i==n && ii && jj && kk)
            res = "YES";
        else
            res = "NO";    
        cout << "Case #" << t + 1 << ": " << res << endl;        
    } 
}


