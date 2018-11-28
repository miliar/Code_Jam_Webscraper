#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    ifstream ss;
    ofstream sss;
    ss.open("a.txt");
    sss.open("a.out");
    int nbCases;
    ss >> nbCases;
    for(int c=0 ; c<nbCases ; c++) {
        int id;
        vector<int> cards0(4), cards1(4);
        ss >> id;
        for(int i=0 ; i<id-1 ; i++) {
            int a;
            ss >> a >> a >> a >> a;
        }
        ss >> cards0[0] >> cards0[1] >> cards0[2] >> cards0[3];
        for(int i=id ; i<4 ; i++) {
            int a;
            ss >> a >> a >> a >> a;
        }
        ss >> id;
        for(int i=0 ; i<id-1 ; i++) {
            int a;
            ss >> a >> a >> a >> a;
        }
        ss >> cards1[0] >> cards1[1] >> cards1[2] >> cards1[3];
        for(int i=id ; i<4 ; i++) {
            int a;
            ss >> a >> a >> a >> a;
        }
        sort(cards0.begin(), cards0.end());
        sort(cards1.begin(), cards1.end());
        int i0=0, i1=0;
        int nbFound = 0;
        int lastNb=-1;
        while(i0<4&&i1<4) {
            if(cards0[i0]<cards1[i1]) {
                i0++;
            } else if(cards0[i0]>cards1[i1]) {
                i1++;
            } else {
                nbFound++;
                lastNb = cards0[i0];
                i0++;
            }
        }
        sss << "Case #" << c+1 << ": ";
        if(nbFound==0) {
            sss << "Volunteer cheated!";
        } else if(nbFound==1) {
            sss << lastNb;
        } else {
            sss << "Bad magician!";
        }
        sss << endl;
    }
    ss.close();
    return 0;
}
