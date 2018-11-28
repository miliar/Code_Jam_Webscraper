#include <iostream>
#include <bitset>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <sstream>
#include <fstream>
#include <cmath>

using namespace std;

typedef vector<int> vi;
typedef vector<vector<int> > vii;
int main()
{
    int T;


    cin>>T;
    // I want to play with set_intersection

    for(int step=1; step<=T; step++){


        vector<vector<int> > table1(4, vector<int>(4,0)), table2(4, vector<int>(4,0));
        int ans1, ans2;
        cin>>  ans1;
        for(int i=0; i<4;  i++){
            for(int j=0; j<4; j++){
                cin >> table1[i][j];
            }
        }

        cin>>ans2;

        for(int i=0; i<4;  i++){
            for(int j=0; j<4; j++){
                cin >> table2[i][j];
            }
        }

        vector<int> v(4,0);
        vector<int>::iterator it;

        sort(table1.at(ans1-1).begin(), table1.at(ans1-1).end());
        sort(table2.at(ans2-1).begin(), table2.at(ans2-1).end());
        it = set_intersection(table1.at(ans1-1).begin(), table1.at(ans1-1).end(),table2.at(ans2-1).begin(), table2.at(ans2-1).end(), v.begin());

        int num = it-v.begin();
        cout<<"Case #"<<step<<": ";

        if(num > 1){
            cout<<"Bad magician!"<<endl;
        } else if(num <= 0){
            cout<<"Volunteer cheated!"<<endl;
        } else{
            cout<<v[0]<<endl;
        }




    }
    return 0;
}

