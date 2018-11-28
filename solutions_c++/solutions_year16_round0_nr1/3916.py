#include<iostream>
#include<fstream>
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


int main() {
    sheep();
}