#include <iostream>
#include <set>
#include <algorithm>
using namespace std;

int main()
{
    int n,i=0;
    cin>>n;
    while (i<n){
        int ans1,ans2;
        int row[4];
        set<int> rows1[4],cols1[4],rows2[4],cols2[4];
        cin>>ans1;
        ans1--;
        for (int j=0;j<4;j++) {
            cin>>row[0]>>row[1]>>row[2]>>row[3];
            rows1[j].insert(row[0]);
            rows1[j].insert(row[1]);
            rows1[j].insert(row[2]);
            rows1[j].insert(row[3]);

            cols1[0].insert(row[0]);
            cols1[1].insert(row[1]);
            cols1[2].insert(row[2]);
            cols1[3].insert(row[3]);

        }
        cin>>ans2;
        ans2--;
        for (int j=0;j<4;j++) {
            cin>>row[0]>>row[1]>>row[2]>>row[3];
            rows2[j].insert(row[0]);
            rows2[j].insert(row[1]);
            rows2[j].insert(row[2]);
            rows2[j].insert(row[3]);

            cols2[0].insert(row[0]);
            cols2[1].insert(row[1]);
            cols2[2].insert(row[2]);
            cols2[3].insert(row[3]);

        }
        bool foundcol=false;
        //for ( set<int>::iterator it=rows1[ans1].begin(); it!=rows1[ans1].end(); it++){
        //    cout<<"d"<<*it<<endl;
       // }
        for (int x=0;x<4;x++){
            if (rows1[ans1] == cols2[x]) {
                foundcol=true;
                break;
            }
        }
        set<int> intersect;

            set_intersection(rows1[ans1].begin(),rows1[ans1].end(),rows2[ans2].begin(),rows2[ans2].end(),
                              std::inserter(intersect,intersect.begin()));

        if (intersect.size() == 0) {
            //cheatah
            cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;
        } else if (intersect.size() > 1) {
            //bad magician
            cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
        } else {

            cout<<"Case #"<<i+1<<": "<<*(intersect.begin())<<endl;

        }
        i++;
    }
    return 0;
}

