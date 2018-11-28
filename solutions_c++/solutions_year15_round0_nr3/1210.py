#include <iostream>
#include <cstdio>
#include <queue>
using namespace std;

int elejchar[300000];
int eleje[300000];
int vegechar[300000];
int vegee[300000];


int chh(int a, int b) {
    if (a==4 && b==1) return 1;
    if (a==4 && b==2) return 2;
    if (a==4 && b==3) return 3;

    if (a==1 && b==4) return 1;
    if (a==2 && b==4) return 2;
    if (a==3 && b==4) return 3;

    if (a==1 && b==1) return 4;
    if (a==1 && b==2) return 3;
    if (a==1 && b==3) return 2;


    if (a==2 && b==1) return 3;
    if (a==2 && b==2) return 4;
    if (a==2 && b==3) return 1;

    if (a==3 && b==1) return 2;
    if (a==3 && b==2) return 1;
    if (a==3 && b==3) return 4;

}

int eee(int a, int b) {




    if (a==4 && b==1) return 1;
    if (a==4 && b==2) return 1;
    if (a==4 && b==3) return 1;

    if (a==1 && b==4) return 1;
    if (a==2 && b==4) return 1;
    if (a==3 && b==4) return 1;

    if (a==1 && b==1) return -1;
    if (a==1 && b==2) return 1;
    if (a==1 && b==3) return -1;


    if (a==2 && b==1) return -1;
    if (a==2 && b==2) return -1;
    if (a==2 && b==3) return 1;

    if (a==3 && b==1) return 1;
    if (a==3 && b==2) return -1;
    if (a==3 && b==3) return -1;
}

int valt(char c) {
    if (c=='i') return 1;
    if (c=='j') return 2;
    if (c=='k') return 3;
}

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int tt;
    cin >> tt;
    for (int ttt=1;ttt<=tt;ttt++) {
        int l;
        long long x;
        cin >>l>>x;
        string aaa;
        cin >> aaa;

        string s=aaa;

        long long y=x/4;
        y-=3;
        if (y>0) x-=4*y;


        for (int i=1;i<x;i++) {
            s+=aaa;
        }

        int n=s.size();


        elejchar[0]=valt(s[0]);
        eleje[0]=1;

        vegechar[n-1]=valt(s[n-1]);
        vegee[n-1]=1;

        for (int i=1;i<n;i++) {
            elejchar[i]=chh(elejchar[i-1],valt(s[i]));
            eleje[i]=eee(elejchar[i-1],valt(s[i]))*eleje[i-1];
        }

        for (int i=n-2;i>=0;i--) {
            vegechar[i]=chh(valt(s[i]),vegechar[i+1]);
            vegee[i]=eee(valt(s[i]),vegechar[i+1])*vegee[i+1];
        }
        bool lehet=false;

        if (elejchar[n-1]==4 && eleje[n-1]==-1) {
            int min1=200000;
            int min2=0;
            for (int i=0;i<n-1;i++) {
                if (elejchar[i]==1 && eleje[i]==1) min1=min(min1, i);
            }
            for (int i=n-1;i>=0;i--) {
                if (vegechar[i]==3 && vegee[i]==1) min2=max(min2, i);
            }
            if (min1<min2) lehet=true;
        }

        cout << "Case #" << ttt<< ": ";
        if (lehet) {
            cout << "YES"<<endl;
        }
        else {
            cout << "NO"<<endl;
        }
    }
    return 0;
}
