#include<iostream>
#include<map>
#include<fstream>
#include<iomanip>
#include<stdio.h>
#include<vector>
#include<algorithm>
#include<stdlib.h>
#include<string.h>

using namespace std;
string s;

char multiple(char x, char y){
    if (x=='1') return y;
    if (y=='1') return x;
    if (x=='i') {
        switch (y){
        case 'i': return '0';
        case 'j': return 'k';
        case 'k': return 'y';
        case 'x': return '1';
        case 'y': return 'z';
        case 'z': return 'j';
        case '0': return 'x';
        }
    }
    if (x=='x') {
            switch (y) {
                case 'i': return '1';
                case 'j': return 'z';
                case 'k': return 'j';
                case 'x': return '0';
                case 'y': return 'k';
                case 'z': return 'y';
                case '0': return 'i';
            }

    }
    if (x=='j') {
            switch (y) {
                case 'i': return 'z';
                case 'j': return '0';
                case 'k': return 'i';
                case 'x': return 'k';
                case 'y': return '1';
                case 'z': return 'x';
                case '0': return 'y';
            }

    }
    if (x=='y') {
        switch (y) {
            case 'i': return 'k';
            case 'j': return 'l';
            case 'k': return 'x';
            case 'x': return 'z';
            case 'y': return '0';
            case 'z': return 'i';
            case '0': return 'j';
        }
    }
    if (x=='k') {
        switch (y) {
            case 'i': return 'j';
            case 'j': return 'x';
            case 'k': return '0';
            case 'x': return 'y';
            case 'y': return 'i';
            case 'z': return '1';
            case '0': return 'z';
        }
    }
    if (x=='z') {
            switch (y){
            case 'i': return 'y';
            case 'j': return 'i';
            case 'k': return '1';
            case 'x': return 'j';
            case 'y': return 'x';
            case 'z': return '0';
            case '0': return 'k';
            }
    }
    if (x=='0') {
            switch (y) {
                case 'i': return 'x';
                case 'j': return 'y';
                case 'k': return 'z';
                case 'x': return 'i';
                case 'y': return 'j';
                case 'z': return 'k';
                case '0': return '1';
            }
    }

}

int main() {

    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    cin>>t;
    for (int cas=1;cas<=t;cas++) {
        int n,m;
        cin>>n>>m;
        cin>>s;
        string temp=s;
        for (int i=1;i<m;i++) s=s+temp;
        char multi1='1';
        bool i1=false;int pi;
        char multi2='1';
        bool k1=false;int pk;
        char total='1';
        for (int i=0;i<s.size();i++) {
            total=multiple(total, s[i]);
        }
        for (int i=0;i<s.size();i++) {
            multi1=multiple(multi1,s[i]);
            if (multi1=='i') {
                pi=i;
                i1=true;
                break;
            }
        }
        for (int i=s.size()-1;i>=0;i--){
            multi2=multiple(s[i],multi2);
            if (multi2=='k'){
                pk=i;
                k1=true;
                break;
            }
        }
        bool answer=false;
        if (total=='0' && k1 && i1 && (pk-pi>1)) answer=true;
        if (answer) cout<<"Case #"<<cas<<": YES"<<endl;
        else cout<<"Case #"<<cas<<": NO"<<endl;
    }
    return 0;
}
