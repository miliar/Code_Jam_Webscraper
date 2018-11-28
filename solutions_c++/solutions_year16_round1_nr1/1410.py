#include<iostream>
#include<string>
#include<algorithm>
using namespace std;
string arr[1005];
int main(){
    int t1;
    cin >> t1;
    int ind=1;
    while(t1--){
        string s;
        cin >> s;
        arr[1]=s[0];
        for(int i=1;i<s.size();++i){
            string f=arr[i];
            string g=f;
            g=s[i]+arr[i];
            f=arr[i]+s[i];
            arr[i+1]=max(f,g);
        }
        cout << "Case #" << ind++ << ": " << arr[(int)s.size()] << endl;
    }
    return 0;
}
