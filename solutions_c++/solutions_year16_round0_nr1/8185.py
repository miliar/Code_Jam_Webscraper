#include <bits/stdc++.h>

using namespace std;

int main(){
    int t, a, b, x, temp=0;

    ofstream myfile;
    myfile.open("test.txt");

    cin >> t;
    while(t--){
        cin >> a;
        set<int> s;
        int i=1;
        while(s.size()!=10){
            if(a==0){
                cout << "Case #" << temp++ << ": INSOMNIA" << endl;
                myfile << "Case #" << temp << ": INSOMNIA" << endl;
                break;
            }
            b=a*i;
            x=b;
            i++;
            while(b!=0){
                s.insert(b%10);
                b=b/10;
            }
            if(s.size()==10){
                cout << "Case #" << temp++ << ": " << x << endl;
                myfile << "Case #" << temp << ": " << x << endl;
                break;
            }
        }
    }

    return 0;
}
