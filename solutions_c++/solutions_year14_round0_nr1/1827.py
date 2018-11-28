#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    freopen("in.txt","r+",stdin);
    freopen("out.txt","w+",stdout);
    int t;
    cin >> t;
    for (int c(0);c<t;c++){
        int before;
        cin >> before;
        int beforearr[4][4],afterarr[4][4];
        for (int c1(0);c1<4;c1++){int a1,b1,d1,e1;cin >> a1>>b1>>d1>>e1;beforearr[c1][0]=a1;beforearr[c1][1]=b1;beforearr[c1][2]=d1;beforearr[c1][3]=e1;}
    int after;cin >> after;
        for (int c1(0);c1<4;c1++){int a1,b1,d1,e1;cin >> a1>>b1>>d1>>e1;afterarr[c1][0]=a1;afterarr[c1][1]=b1;afterarr[c1][2]=d1;afterarr[c1][3]=e1;}

    cout << "Case #"<< c+1<<": " ;
    int result(-1);int flag(0);
    for (int c1(0);c1<4;c1++){
        for (int c22(0);c22<4;c22++)if(beforearr[before-1][c1]==afterarr[after-1][c22]&&result==-1){result=beforearr[before-1][c1];} else if (result!=-1&&beforearr[before-1][c1]==afterarr[after-1][c22]){cout << "Bad magician!" << endl;goto l;}
    }

        if (result==-1)cout << "Volunteer cheated!" << endl;
            else cout << result << endl;
        l:;
    }
    return 0;
}
