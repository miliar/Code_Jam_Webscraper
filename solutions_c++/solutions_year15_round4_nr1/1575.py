#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cmath>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <vector>

using namespace std;

#define openfile {freopen("input.txt","r",stdin); freopen("output.txt","w",stdout);}
#define debug 01

int r, c, t, res, rr[110], cc[110], sumr[110][110], sumc[110][110];
char a[110][110];

void solve() {
    memset(rr, 0, sizeof rr);
    memset(cc, 0, sizeof cc);
    cin>>r>>c;
    for (int i=0; i<r; i++) {
        for (int j=0; j<c; j++) {
            cin>>a[i][j];
        }
    }
    res=0;
    for (int i=0; i<r; i++) {
        for (int j=0; j<c; j++) {
            if (a[i][j]!='.') {
                rr[i]++;
                cc[j]++;
                if (i>0)
                    sumr[i][j]=sumr[i-1][j]+1;
                else sumr[i][j]=1;
                if (j>0)
                    sumc[i][j]=sumc[i][j-1]+1;
                else sumc[i][j]=1;
            }
            if (i>0)
                sumr[i][j]=sumr[i-1][j];
            else sumr[i][j]=0;
            if (j>0)
                sumc[i][j]=sumc[i][j-1];
            else sumc[i][j]=0;
        }
    }
    for (int i=0; i<r; i++) {
        for (int j=0; j<c; j++) {
            if (a[i][j]!='.' && rr[i]==1 && cc[j]==1) {
                res=-1;
                return;
            }
        }
    }
    for (int i=0; i<r; i++) {
        if (rr[i]>1) {
            for (int j=0; j<c; j++) {
                if (a[i][j]!='.') {
                    if (a[i][j]=='<') {
                        res++;
                        a[i][j]='>';
                    }
                    break;
                }
            }
            for (int j=c-1; j>=0; j--) {
                if (a[i][j]!='.') {
                    if (a[i][j]=='>') {
                        res++;
                        a[i][j]='<';
                    }
                    break;
                }
            }
        }
    }
    for (int j=0; j<c; j++) {
        if (cc[j]>1) {
            for (int i=0; i<r; i++) {
                if (a[i][j]!='.') {
                    if (a[i][j]=='^') {
                        res++;
                        a[i][j]='v';
                    }
                    break;
                }
            }
            for (int i=r-1; i>=0; i--) {
                if (a[i][j]!='.') {
                    if (a[i][j]=='v') {
                        res++;
                        a[i][j]='^';
                    }
                    break;
                }
            }
        }
    }
    for (int i=0; i<r; i++) {
        for (int j=0; j<c; j++) {
            if (rr[i]==1 && a[i][j]!='.') {
                if (sumc[i][j]==1) {
                    if (a[i][j]!='v') {
                        res++;
                        a[i][j]='v';
                    }
                }
                else if (sumc[i][j]==cc[j]) {
                    if (a[i][j]!='^') {
                        res++;
                        a[i][j]='^';
                    }
                }
                else {
                    if (a[i][j]!='^' && a[i][j]!='v') {
                        res++;
                        a[i][j]='^';
                    }
                }
            }
            if (cc[j]==1 && a[i][j]!='.') {
                if (sumr[i][j]==1) {
                    if (a[i][j]!='>') {
                        res++;
                        a[i][j]='>';
                    }
                }
                else if (sumr[i][j]==rr[i]) {
                    if (a[i][j]!='<') {
                        res++;
                        a[i][j]='<';
                    }
                }
                else {
                    if (a[i][j]!='>' && a[i][j]!='<') {
                        res++;
                        a[i][j]='<';
                    }
                }
            }
        }
    }
}

int main()
{
    if (debug) openfile;
    cin>>t;
    for (int i=0; i<t; i++) {
        solve();
        if (res==-1) {
            printf("Case #%d: IMPOSSIBLE\n", i+1);
        }
        else printf("Case #%d: %d\n", i+1, res);
    }
    return 0;
}
