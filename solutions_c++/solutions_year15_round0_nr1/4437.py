#include <cstdlib>
#include <iostream>
#include <string>

using namespace std;

int main()
{
    ios::sync_with_stdio(false);
    int T,n,friends,people_standing, temp;
    cin >> T;
    for(int i = 1;i<=T;++i){
        cin >> n;;
        int length = n+1;
        string s;
        cin >> s;
        friends = people_standing = 0; 
        for(int j = 0;j<length;++j){
           temp = s[j] - '0';
           if(people_standing >= j) people_standing+=temp;
           else{
               friends += (j-people_standing);
               people_standing = (j+temp);
           }
        }
        cout << "Case #" << i << ": " << friends << "\n";
    }      
    return 0;
}
