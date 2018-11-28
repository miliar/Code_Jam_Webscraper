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
        map<char,int> m;
        string res="";
        for(int c=0;c<s.size();c++) m[s[c]]++;

        string tmp = "ZERO";
        while(m['Z'] > 0) {
            m['Z']--;
            m['E']--;
            m['R']--;
            m['O']--;
            res = res + '0';
        }
        tmp = "EIGHT";

        while(m['G'] > 0) {
            for(int c=0;c<tmp.size();c++) m[tmp[c]]--;
            res = res + '8';
        }

        tmp = "SIX";

        while(m['X'] > 0) {
            for(int c=0;c<tmp.size();c++) m[tmp[c]]--;
            res = res + '6';
        }

        tmp = "THREE";

        while(m['H'] > 0) {
            for(int c=0;c<tmp.size();c++) m[tmp[c]]--;
            res = res + '3';
        }

        tmp = "TWO";

        while(m['W'] > 0) {
            for(int c=0;c<tmp.size();c++) m[tmp[c]]--;
            res = res + '2';
        }

        tmp = "FOUR";

        while(m['U'] > 0) {
            for(int c=0;c<tmp.size();c++) m[tmp[c]]--;
            res = res + '4';
        }

        tmp = "FIVE";

        while(m['F'] > 0) {
            for(int c=0;c<tmp.size();c++) m[tmp[c]]--;
            res = res + '5';
        }

        tmp = "SEVEN";

        while(m['S'] > 0) {
            for(int c=0;c<tmp.size();c++) m[tmp[c]]--;
            res = res + '7';
        }

        tmp = "NINE";

        while(m['I'] > 0) {
            for(int c=0;c<tmp.size();c++) m[tmp[c]]--;
            res = res + '9';
        }
        tmp = "ONE";

        while(m['O'] > 0) {
            for(int c=0;c<tmp.size();c++) m[tmp[c]]--;
            res = res + '1';
        }
        sort(res.begin(),res.end());
        cout<<res<<endl;
    }



}
