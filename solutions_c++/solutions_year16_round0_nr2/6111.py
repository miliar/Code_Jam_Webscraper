#include <fstream>
#include <cstdio>
#include <algorithm>
#include <vector>
#include <iostream>
#include <set>
#include <iterator>
#include <map>
#include <cmath>
#include <queue>
#include <ctime>

using namespace std;


ifstream in("input.txt");
ofstream out("output.txt");

int t;
string s;

int main(int argc, const char * argv[]) {
    in >> t;
    int it=1;
    while (it<=t){
        out << "Case #" << it << ": ";
        in >> s;
        int ans=0;
        while (true){
            int p=-1;
            for (int i=s.length()-1;i>=0;i--)
                if (s[i]=='-') {
                    p=i;
                    break;
                }
            if (p==-1) break;
            if (s[0]=='+'){
                ans++;
                for (int i=0;i<s.length()-1;i++){
                    if (s[i]=='+') s[i]='-';
                    else break;
                }
            }
            int l=0; int r=p;
            while (l<=r){
                char ch=s[l]; s[l]=s[r]; s[r]=ch;
                l++; r--;
            }
            for (int i=0;i<=p;i++){
                if (s[i]=='-') s[i]='+'; else s[i]='-';
            }
            ans++;
        }
        out << ans << endl;
        it++;
    }
    
    return 0;
}