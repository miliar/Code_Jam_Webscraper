#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

void flip(string &s, int n){
    n++;
    reverse(s.begin(), s.begin()+n);
    for(int i=0; i<n; i++){
        if(s[i] == '+')
            s[i] = '-';
        else
            s[i] = '+';
    }
}


int main()
{
    int t;
    vector<string> a;
    string s;
    cin>>t;

    for(int i=0; i<t; i++){
        cin >> s;
        a.push_back(s);
    }


    for(int i=0; i<t; i++){

        int c=0;
        while(1){
            int x = a[i].length()-1;
            while(a[i][x] == '+') x--;

            if(x < 0)
                break;

            int y = 0;
            while(a[i][y] == '+'){
                a[i][y++] = '-';
            }
            if(y!=0)
                c++;

            flip(a[i], x);
            c++;
        }
        cout<<"Case #"<<i+1<<": "<<c<<endl;
    }
    return 0;
}
