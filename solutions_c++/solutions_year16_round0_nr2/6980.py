#include <cstdlib>
#include <iostream>
#include "set"

using namespace std;

int main(int argc, char *argv[])
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int T;
    cin >> T;

	int y;
	string s;
	bool Good;
    for (int T_i=0; T_i<T;T_i++){
        cin >> s;
        
        if (s[0]=='+') Good=true; else Good =false;
        y=0;
        for (int x=1; x<s.length();x++){
            if (s[x-1]!=s[x]) {
               y++;
               Good = !Good;
            }
        }
        
        if (!Good) y++;
        
        
        cout << "Case #" << T_i+1 << ": " << y << endl;
    }
    return EXIT_SUCCESS;
}
