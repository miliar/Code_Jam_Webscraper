#include <iostream>
#include <map>
#include <vector>
#include <string>

using namespace std;

map<int, vector<char> > m;

void secureAdd(int k, char v){
    if (k<=0){
       return;
       }
    if ( m.find(k) == m.end() ){
        m[k] = vector<char>();
        }
    (m[k]).push_back(v);
    }

int main(){
int T,p,k;
map<int, vector<char> >::reverse_iterator it;
cin >> T;
for (int n=1;n<=T;n++){
    cin >> p;
    for (char c='A';p>0;c++,p--){
          cin >> k;
          secureAdd(k,c);
          }

    cout << "Case #" << n << ": ";

    while (m.size()>0){

          it=m.rbegin();
          if ( (it->second).size() % 2 == 1  ){

             if ( (it->first) > 1 ){
                cout << (it->second)[0] << (it->second)[0] << " ";
                secureAdd(it->first-2,(it->second)[0]);
                }
                else{
                    cout << (it->second)[0] << " ";
                    secureAdd(it->first-1,(it->second)[0]);
                    }
             (it->second).erase( (it->second).begin() );

             }
             else{
                 for (int i=0;i<2;i++){
                    cout << (it->second)[0];
                    secureAdd(it->first-1,(it->second)[0]);
                    (it->second).erase( (it->second).begin() );
                    }
                 cout << " ";
                 }
          if ((it->second).size() == 0){
             m.erase(it->first);
             }

          }
    cout << endl;
    }

return 0;
}
