#include<iostream>
#include<fstream>
#include<string>
using namespace std;


int count_d(long long num, bool* v, int left) {
    int left_count = left;
    long long tmp = num;
    while (tmp > 0) {
        if (!v[tmp%10]) {
            left_count --;
            v[tmp%10] = true;
        }
        tmp = tmp / 10;
    }
    return left_count;
}

void sheep() {
    freopen("A-large.in.txt", "r", stdin);
    //ifstream ifs("input.in", ifstream::in);
    ofstream ofs("output.out", ofstream::out);
    int N;
    cin>>N;
    int a = -1;
    int ct = 0;
    bool *v = new bool[10];
    while (N>0) {
        N--;
        cin>>a;
        ct++;
        if (a==0) {
            ofs<<"Case #"<<ct<<": INSOMNIA\n";
        } else {
        for (int i = 0; i<10; i++) v[i] = false;
        long long c = 0;
        int left = 10;
        while (left > 0) {
            c = c + a;
            left = count_d(c, v, left);
        }
        ofs<<"Case #"<<ct<<": "<<c<<'\n';
        }
    }
    
}

void flip() {
    freopen("B-large.in.txt","r", stdin);
    freopen("B-large.out", "w", stdout);
    
    int T;
    cin>>T;
    int ct = 0;
    while (T>0) {
        T--;
        string s;
        cin>>s;
        int n = s.length();
        bool v[200];
        for (int i =0; i<n; i++) v[i] = s[i] == '+';
        int k = n-1;
        int j = 0;
        int count = 0;
        while (true) {
            while (v[k] && k >=0) k--;
            if (k<0) break;
            j = 0;
            while (!v[j] && j<=k) j++;
            if (j>k) {
                count ++;
                break;
            }
            if (j>0) {
                for (int i = 0; i<k/2+1; i++) {
                    bool tmp = v[i];
                    v[i] = v[k-i];
                    v[k-i] = tmp;
                    v[i] = !v[i];
                    if (i!=k-i) {v[k-i] = !v[k-i];}
                }
                count++;
            } else {
                while (v[j] && j<n) j++;
                for (int i =0; i<j; i++) v[i] = !v[i];
                count++;
            }
            j = 0;
        }
        ct++;
        cout<<"Case #"<<ct<<": "<<count<<'\n';
    }
    
}


int main() {
    flip();
}