#include <iostream>
#include <cstdio>
#include <set>
using namespace std;

#define ll                      long long

#define inc(i,a,b)              for(int i=a;i<=b;++i)
#define dec(i,a,b)              for(int i=a;i>=b;--i)

int main() {
    ios::sync_with_stdio(false);
    
    int t; cin >> t; int x = 1;
    while(t--) {
        int r1, r2;
        
        set<int> first, second, soln;
        
        cin >> r1;
        inc(i,1,4) {
            int a, b, c, d;
            cin >> a >> b >> c >> d;
            
            if(i!=r1) continue;
            
            first.insert(a);
            first.insert(b);
            first.insert(c);
            first.insert(d);
        }
        
        cin >> r2;
        inc(i,1,4) {
            int a, b, c, d;
            cin >> a >> b >> c >> d;
            
            if(i!=r2) continue;
            
            second.insert(a);
            second.insert(b);
            second.insert(c);
            second.insert(d);
        }
        
        while(!first.empty() && !second.empty()) {
            int f = *first.begin();
            int s = *second.begin();
            
            if(f==s) {
                soln.insert(f);
                first.erase(first.begin());
                second.erase(second.begin());
            }
            else if(f<s) {
                first.erase(first.begin());
            }
            else {
                second.erase(second.begin());
            }
        }
        
        cout << "Case #" << x << ": ";
        
        if(soln.empty()) {
            cout << "Volunteer cheated!\n";
        }
        else if(soln.size()==1) {
            cout << (*soln.begin()) << "\n";
        }
        else {
            cout << "Bad magician!\n";
        }
        
        x++;
    }
}