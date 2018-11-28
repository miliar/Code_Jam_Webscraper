#include <iostream>
#include <string>

using namespace std;

string res(string o){
    string c="";
    for (int i=0;i<o.size();i++){
         if (c.size()==0 || c[0]>o[i]){
            c+=o[i];
            }
            else{
                c=o[i]+c;
                }
        }
    return c;
    }

int main(){
int n;
string o;
cin >> n;
for (int i=1;i<=n;i++){
    cin >> o;
    cout << "Case #"<<i <<": " << res(o) << endl;
    }
return 0;
}
