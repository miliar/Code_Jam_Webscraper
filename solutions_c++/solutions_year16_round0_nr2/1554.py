#include <bits/stdc++.h>
using namespace std;

int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");
#define cin in
#define cout out
    int nbCas;
    cin>>nbCas;

    for(int c=1;c<=nbCas;c++) {

        cout<<"Case #"<<c<<": ";

        string s;
        cin>>s;
        int steps = 0;
        while(s.find('-') != string::npos) {
            while(s.size() > 0 && s[s.size()-1]=='+') s = s.substr(0,s.size()-1);
            int bla = s.find_last_of(s[0]);
            reverse(s.begin(),s.begin()+bla+1);
            for(int c2=0;c2<=bla;c2++) {
                if(s[c2] == '-') s[c2]='+';
                else s[c2]='-';
            }
            steps++;
        }
        cout<<steps<<endl;

    }
}
