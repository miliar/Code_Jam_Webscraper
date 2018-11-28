#include <bits/stdc++.h>
using namespace std;

class quat {
public:
    int sign;
    char val;
    quat(): sign(1), val('1') { }
    quat(int a, char b): sign(a), val(b) { }
};

quat mult(quat a, quat b) {
    quat ret;
    if (a.val=='1') {
        ret.sign=a.sign*b.sign;
        ret.val=b.val;
    }
    else if (a.val=='i') {
        ret.sign=a.sign*b.sign;
        if (b.val=='1') {
            ret.val='i';
        }
        else if (b.val=='i') {
            ret.sign*=-1;
            ret.val='1';
        }
        else if (b.val=='j') {
            ret.val='k';
        }
        else {
            ret.sign*=-1;
            ret.val='j';
        }
    }
    else if (a.val=='j') {
        ret.sign=a.sign*b.sign;
        if (b.val=='1') {
            ret.val='j';
        }
        else if (b.val=='i') {
            ret.val='k';
            ret.sign*=-1;
        }
        else if (b.val=='j') {
            ret.sign*=-1;
            ret.val='1';
        }
        else {
            ret.val='i';
        }
    }
    else {
        ret.sign=a.sign*b.sign;
        if (b.val=='1') {
            ret.val='k';
        }
        else if (b.val=='i') {
            ret.val='j';
        }
        else if (b.val=='j') {
            ret.sign*=-1;
            ret.val='i';
        }
        else {
            ret.val='1';
            ret.sign*=-1;
        }
    }
    return ret;
}

int main(void) {
    if (fopen("c-small.in","r")) {
        freopen("c-small.in","r",stdin);
        freopen("c-small.out","w",stdout);
    }
    int t;
    cin >> t;
    for (int ii=1; ii<=t; ii++) {
        string ex, s="";
        int x, l;
        cin >> l >> x;
        cin >> ex;
        for (int i=0; i<x; i++) s+=ex;
        quat ret;
        int good=-1;
        for (int i=0; i<s.length(); i++) {
            ret=mult(ret,quat(1,s[i]));
            if (good==-1 && ret.val=='i' && ret.sign==1) {
                good=i;
            }
        }
        if (ret.sign!=-1 || ret.val!='1' || good==-1) {
            cout << "Case #" << ii << ": NO\n";
            continue;
        }
        ret=quat();
        bool found=false;
        for (int i=s.length()-1; i>=good+2 && !found; i--) {
            ret=mult(quat(1,s[i]),ret);
            if (ret.sign==1 && ret.val=='k') {
                cout << "Case #" << ii << ": YES\n";
                found=true;
            }
        }
        if (!found) cout << "Case #" << ii << ": NO\n";
    }
}
