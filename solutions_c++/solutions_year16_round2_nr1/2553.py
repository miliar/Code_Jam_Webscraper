#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int main(){
int T;
string s;
vector<int> v;
cin >> T;
for (int n=1;n<=T;n++){
    v.clear();
    cin >> s;
    while (s.find("Z")!=string::npos){
        s.erase(s.begin()+s.find("Z"));
        s.erase(s.begin()+s.find("E"));
        s.erase(s.begin()+s.find("R"));
        s.erase(s.begin()+s.find("O"));
        v.push_back(0);
        //cout << "0: " << s << " " << s.find("Z") << endl;
        //cin >> r;
        }
    while (s.find("W")!=string::npos){
        s.erase(s.begin()+s.find("T"));
        s.erase(s.begin()+s.find("W"));
        s.erase(s.begin()+s.find("O"));
        v.push_back(2);
        //cout << "2: " << s << endl;
        //cin >> r;
        }
    while (s.find("U")!=string::npos){
        s.erase(s.begin()+s.find("F"));
        s.erase(s.begin()+s.find("O"));
        s.erase(s.begin()+s.find("U"));
        s.erase(s.begin()+s.find("R"));
        v.push_back(4);
        }
    while (s.find("X")!=string::npos){
        s.erase(s.begin()+s.find("S"));
        s.erase(s.begin()+s.find("I"));
        s.erase(s.begin()+s.find("X"));
        v.push_back(6);
        }
    while (s.find("G")!=string::npos){
        s.erase(s.begin()+s.find("E"));
        s.erase(s.begin()+s.find("I"));
        s.erase(s.begin()+s.find("G"));
        s.erase(s.begin()+s.find("H"));
        s.erase(s.begin()+s.find("T"));
        v.push_back(8);
        }
    while (s.find("O")!=string::npos){
        s.erase(s.begin()+s.find("O"));
        s.erase(s.begin()+s.find("N"));
        s.erase(s.begin()+s.find("E"));
        v.push_back(1);
        }
    while (s.find("H")!=string::npos){
        s.erase(s.begin()+s.find("T"));
        s.erase(s.begin()+s.find("H"));
        s.erase(s.begin()+s.find("R"));
        s.erase(s.begin()+s.find("E"));
        s.erase(s.begin()+s.find("E"));
        v.push_back(3);
        }
    while (s.find("F")!=string::npos){
        s.erase(s.begin()+s.find("F"));
        s.erase(s.begin()+s.find("I"));
        s.erase(s.begin()+s.find("V"));
        s.erase(s.begin()+s.find("E"));
        v.push_back(5);
        }
    while (s.find("S")!=string::npos){
        s.erase(s.begin()+s.find("S"));
        s.erase(s.begin()+s.find("E"));
        s.erase(s.begin()+s.find("V"));
        s.erase(s.begin()+s.find("E"));
        s.erase(s.begin()+s.find("N"));
        v.push_back(7);
        }
    while (s.find("N")!=string::npos){
        s.erase(s.begin()+s.find("N"));
        s.erase(s.begin()+s.find("I"));
        s.erase(s.begin()+s.find("N"));
        s.erase(s.begin()+s.find("E"));
        v.push_back(9);
        }
    sort(v.begin(),v.end());
    cout << "Case #"<<n<<": ";
    for (int i=0;i<v.size();i++){
        cout << v[i];
        }
    cout << endl;
    }

return 0;
}
