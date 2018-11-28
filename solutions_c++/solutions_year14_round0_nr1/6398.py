 #include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
using namespace std;

int main()
{
    ifstream file("A-small-attempt0.in");
    ofstream o("A-small-attempt0.out");
    if (!file.is_open())
        cout<<"error";
    long long n;
    string t;
    getline(file,t);
    n = atoi( t.c_str() );

    //long long num,v1[800],v2[800];

    for(int i=0; i<n; i++) {
        int row1, arr1[4][4],row2,arr2[4][4];
        file>>row1;
        for(int j=0; j<4;j++)
            for(int k=0;k<4;k++)
                file>>arr1[j][k];
        file>>row2;
        for(int j=0; j<4;j++)
            for(int k=0;k<4;k++)
                file>>arr2[j][k];

        row1--;
        row2--;

        // analyze
        o<<"Case #"<<i+1<<": ";
        bool found = false;
        bool bad = false;
        int what = 0;
        for(int j=0; j<4 && !bad;j++) {
            for(int k=0;k<4;k++) {
                if(arr1[row1][j] == arr2[row2][k]) {
                    if(found == true) {
                        //cout<<"case"<<i+1<<"found == true"<<endl;
                        bad = true;
                        break;
                        }
                        //cout<<"case "<<i+1<<" set found = true "<<arr1[row1][j]<<" "<<arr2[row2][k]<<endl;
                    found = true;
                    what = arr1[row1][j];
                    }
                }
            }

        if(!bad && found)
            o<<what<<endl;
        else if(!bad && !found)
            o<<"Volunteer cheated!"<<endl;
        else
            o<<"Bad magician!"<<endl;
        }
    return 0;
}