#include <stdexcept>
#include <cassert>
#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <iterator>
#include <vector>
#include <stack>
#include <list>
#include <map>
#include <queue>
#include <cmath>
#include <climits>
#include <ctime>
#include <cstring>
#include <string>
#include <cstdlib>
#include <cstdio>
#include <utility>
#include <set>
using namespace std;


string add(string s1, string s2){
    int sz1 = s1.size();
    int sz2 = s2.size();
    int i = sz1-1;
    int j = sz2-1;
    int t = 0, carry = 0;
    int a, b;
    string ret = "";
    while(1){
        if(i<0&&j<0)
            break;
        a = 0;
        if(i>=0)
            a = s1[i--]-'0';
        b = 0;
        if(j>=0)
            b = s2[j--]-'0';
        t = a + b + carry;
        carry = t/10;
        t = t%10;
        ret.insert(0,1,t+'0');
    }
    if(carry > 0)
        ret.insert(0,1,carry+'0');
    return ret;
}

string multiply(string str, char ch){
    string s = "";
    int t = 0, carry = 0, a = 0, b = (ch-'0');
    for(int i = str.size()-1; i >= 0; i--){
        a = str[i]-'0';
        t = a * b + carry;
        carry = t/10;
        t = t%10;
        s.insert(0,1,t+'0');
    }
    if(carry > 0)
        s.insert(0,1,carry+'0');
    return s;
}

string multiply(string a, string b){
        string t = "";
        for(int j = b.size()-1; j >= 0 ; j--){
            string tmp = multiply(a,b[j]);
            int i = b.size()-1-j;
            while(i>0){
                tmp = tmp + "0";
                i--;
            }

            t = add(t,tmp);
        }
        return t; 
}

bool check(string s){
    int i = 0;
    int j = s.size()-1;
    while(i<j){
        if(s[i++] != s[j--])
            return false;
    }
    return true;
}
bool cmp_less(string a, string b){
    if(a.size() < b.size())
        return true;
    if(a.size() > b.size())
        return false;
    for(int i = 0; i < a.size(); i++){
        if(a[i] < b[i])
            return true;
        else if(a[i] > b[i])
            return false;
    }
    return false;
}

void check_all(string beg, int k){
    string end = "1";
    string i = beg;
    while(k>=0){
        end = multiply(end,"10");
        k--;
    }
    while(cmp_less(i,end)){
        if(check(i)){
            string s = multiply(i,i);    
            if(check(s)){
                cout << s << endl;
            }
        }
        i = add(i,"1");
    }
}

int cmp_str(string a, string b){
    if(a.size() < b.size())
        return -1;
    if(a.size() > b.size())
        return 1;
    for(int i = 0; i < a.size(); i++){
        if(a[i] < b[i])
            return -1;
        else if(a[i] > b[i])
            return 1;
    }
    return 0;
}

int search_upper(vector<string>& A, string key){
    int i = 0;
    int j = (int)A.size()-1;
    int m;
    while(i <= j){
        m = (i+j)/2;
        if(cmp_str(A[m],key) == 0){
            return m;
        }else if(cmp_str(A[m],key) < 0){
            i = m+1;
        }else{
            j = m-1;
        }
    }
    return i;
}

int search_lower(vector<string>& A, string key){
    int i = 0;
    int j = (int)A.size()-1;
    int m;
    while(i <= j){
        m = (i+j)/2;
        if(cmp_str(A[m],key) == 0){
            return m;
        }else if(cmp_str(A[m],key) < 0){
            i = m+1;
        }else{
            j = m-1;
        }
    }
    return j;
}

vector<string> load_data(){
    ifstream fin("./data5.log");
    if(!fin.good()){
        cout << "Error, cannot open file" << endl;
        vector<string>B;
        return B;
    }
    vector<string> A;
    string line;
    while(getline(fin,line)){
        A.push_back(line);
    }
    fin.close();
    return A;
}

void parse_line(string s, string& a, string& b){
    int i = 0;
    for(i = 0; i < s.size(); i++){
        if(s[i] == ' ')
            break;
    }
    a = s.substr(0,i);
    for(i = s.size()-1; i >=0; i--)
        if(s[i] == ' ')
            break;
    i++;
    b = s.substr(i);
}

void solve(){
    vector<string> A = load_data();

    ifstream fin("./in.txt");
    if(!fin.good()){
        cout << "Error, cannot open file" << endl;
        return;
    }
    
    ofstream fout("./out.txt");
    if(!fout.good()){
        cout << "Error, cannot open file" << endl;
        return;
    }
    
    int nTest;
    string a, b;
    fin>>nTest;
    string line;
    getline(fin,line);

    for(int i = 0; i < nTest; i++){
        getline(fin,line);        
        parse_line(line,a,b);
        int lower = search_upper(A,a);
        int upper = search_lower(A,b);
        fout << "Case #" << (i+1) << ": " << upper-lower+1 << endl;    
    }
    fin.close();
    fout.close();
}

int main(){
    //test();
    //check_all(beg,k);
    solve();
    return 0;
}
