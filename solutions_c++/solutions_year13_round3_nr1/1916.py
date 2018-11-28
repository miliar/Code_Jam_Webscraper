#include <iostream>
#include <vector>
#include <cmath>
#include <string>
using namespace std;
int main() {
    int t;
    cin>>t;
    for(int i=1; i<=t; ++i) {
        int n;
        string lol;
        vector<int> loput;
        cin>>lol;
        cin>>n;

        vector<int> alut;
        for(int j=0; j<lol.size();++j) {
            for(int k=0; k<n; ++k) {

                if(j+k>=lol.size()||lol[j+k]=='a'||lol[j+k]=='e'||lol[j+k]=='i'||lol[j+k]=='o'||lol[j+k]=='u') {
                    goto ohi3;
                }

            }
            alut.push_back(j);
ohi3:;
        }
         
        int tulos=0;
        int edellinen=0;
        for(int j=0; j<alut.size(); ++j) {
        //    cout<<alut[j]<<' ';
         //   cout<<alut[j]-edellinen+1<<' '<<lol.size()-(alut[j]+n-1)<<'\n';
            tulos+=(alut[j]-edellinen+1)*(lol.size()-(alut[j]+n-1));

            edellinen=alut[j]+1;

        }

        cout<<"Case #"<<i<<": "<<tulos<<'\n';

ohi:;
    }
}
