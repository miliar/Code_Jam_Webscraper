#include<iostream>
#include<cmath>
#include<string>
#include<fstream>
#include<sstream>
using namespace std;

string toString(int a);
bool isPalindrome(string s);
int main() {
    ifstream in("C-small-attempt0.in",ios_base::in);
    ofstream out("out.txt",ios_base::out);
    if(in.fail() || out.fail()){
        cout << "Error" <<endl; return 0;
    }
    int cases,a,b,count;
    string temp;
    in >> cases;

    for(int k=1; k<=cases; k++) {
        count = 0;
        in >>a; in >> b;
        for(int i=a; i<=b; i++){
            temp = toString(i);
            if(isPalindrome(temp)){
                int root = sqrt(i);
                if(root*root == i){
                    if(isPalindrome(toString(root))){
                        count++;
                    }
                }
            }
        }
        out << "Case #"<<k << ": " << count<<endl;
    }
    in.close();
    out.close();
    return 0;
}

string toString(int a){
    stringstream ss;
    ss << a;
    string s;
    ss >> s;
    return s;
}

bool isPalindrome(string s){
    int l = s.length();
    int n = l/2;
    for(int i=0; i<n; i++){
        if(s.at(i)!=s.at(l-i-1))
            return false;
    }
    return true;
}
