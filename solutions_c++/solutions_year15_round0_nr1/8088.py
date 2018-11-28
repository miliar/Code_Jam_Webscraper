#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

int solve_case()
{
    string s;
    int M;
    cin >> M >> s;
    int standing = 0,friends = 0;
    for( int i = 0; i < s.size(); i++ ){
        if(s[i]=='0'){
            continue;
        }
        if((standing+friends) < i){
            friends += i - (standing+friends);
        }
        standing += s[i]-'0';
    }
    return friends;
}

int main(int argc, char * argv[])
{
    int T;
    cin >> T;
    for( int cse = 1; cse <= T; ++cse ){
        cout << "Case #" << cse << ": " << solve_case() << endl;
    }
    return 0;
}
