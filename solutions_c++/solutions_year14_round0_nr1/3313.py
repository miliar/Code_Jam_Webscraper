#include <iostream>
#include <fstream>
#include <cstdio>
using namespace std;

int main()
{
    ifstream in;
    ofstream out;
    in.open("A-small-attempt1.in");
    out.open("A-small-attempt.out");
    int n;
    in>>n;
    int card[4][4];
    int t1[4],t2[4];
    for (int cur=1;cur<=n;cur++){
        int r1;
        in>>r1;
        for (int i=0;i<4;i++)
            for (int j=0;j<4;j++){
                in>>card[i][j];
                if(i==r1-1) t1[j]=card[i][j];
            }
        int r2;
        in>>r2;
        for (int i=0;i<4;i++)
            for (int j=0;j<4;j++){
                in>>card[i][j];
                if(i==r2-1) t2[j]=card[i][j];
            }
        int cnt=0;
        int temp;
        for (int i=0;i<4;i++)
            for (int j=0;j<4;j++){
                if (t1[i]==t2[j]) {cnt++; temp=t1[i];}
        }
        if (cnt==0) out<<"Case #"<<cur<<": Volunteer cheated!";
        if (cnt>=2) out<<"Case #"<<cur<<": Bad magician!";
        if (cnt==1) out<<"Case #"<<cur<<": "<<temp;
        if (cur<n) out<<"\n";
    }
    return 0;
}
