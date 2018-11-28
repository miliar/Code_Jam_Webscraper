#include <iostream>
#include <cstdio>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int main(void){

    ifstream fin("Clarge.in");
    ofstream fout("Clarge.out");
    int n;
    fin>>n;

    for(int t = 1; t <= n; t++){
        double girl[1001];
        double boy[1001];
        vector <double> tempg;
        vector <double> tempb;
        int x;
        fin>>x;
        for ( int i = 0; i < x; i++ )
            fin>>girl[i];
        for ( int i = 0; i < x; i++ )
            fin>>boy[i];
        for ( int i = 0; i < x; i++ ){
            tempg.push_back(girl[i]);
            tempb.push_back(boy[i]);
        }
        sort(tempg.rbegin(),tempg.rend());
        sort(tempb.rbegin(),tempb.rend());

        int scoregirl = 0;
        int scoreboy = 0;
        //fout<<"girl "<<tempg[0]<<" boy "<<tempb[0]<<endl;
        for ( int i =0; i < x; i++ ){
            double elem = tempg[i];
            int sizeb = tempb.size();
            if( elem > tempb[0]){
                ++scoregirl;
                tempb.erase(tempb.begin() + tempb.size() -1);
                continue;
            }
            bool flag = true;
            ++scoreboy;
            for ( int j = 1; j < sizeb; j++ ){
                if ( tempb[j] < elem){
                    tempb.erase(tempb.begin() + j - 1);
                    flag = false;
                    break;
                }
            }
            if ( flag ){
                tempb.erase(tempb.begin() + tempb.size() -1);
            }
        }
        //fout<<"girl "<<scoregirl<<" boy "<<scoreboy<<endl;

        //Now the part where deception war is there
        vector <double> temp2g;
        vector <double> temp2b;
        for ( int i = 0; i < x; i++ ){
            temp2g.push_back(girl[i]);
            temp2b.push_back(boy[i]);
        }
        sort(temp2g.begin(),temp2g.end());
        sort(temp2b.begin(),temp2b.end());

        int dscoregirl = 0;
        int dscoreboy = 0;

        for ( int k = 0; k < x; ++k ){
            if ( temp2g[k] < temp2b[0] ){
                ++dscoreboy;
                temp2b.erase(temp2b.begin() + temp2b.size() - 1);
            }
            else {
                ++dscoregirl;
                temp2b.erase(temp2b.begin());
            }
        }

        //******second part ends here

        //fout<<endl<<"dgirl "<<dscoregirl<<" dboy "<<dscoreboy<<endl;
        fout<<"Case #"<<t<<": "<<dscoregirl<<" "<<scoregirl<<"\n";
    }
    return 0;
}

