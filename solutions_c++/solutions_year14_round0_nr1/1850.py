#include <iostream>
#include <map>
#include <stdio.h>
using namespace std;

#define NUM 4

int data1[NUM][NUM];
int data2[NUM][NUM];

int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int t,tt=1;
    cin>>t;
    int ans1,ans2;
    int i,j;
    while ( tt <= t ){
        map<int,int> maptest;
        map<int,int>::iterator it;
        int counts = 0;
        int chosen = 0;
        cin >> ans1;
        ans1--;
        for ( i = 0 ; i < NUM ; i++ ){
            for ( j = 0 ; j < NUM ; j++ ){
                cin >> data1[i][j];
            }
        }
        for( j = 0 ; j < NUM ; j++ )
            maptest.insert( pair<int,int> (data1[ans1][j],data1[ans1][j]));

        cin >> ans2;
        ans2--;
        for ( i = 0 ; i < NUM ; i++ ){
            for ( j = 0 ; j < NUM ; j++ ){
                cin >> data2[i][j];
            }
        }
        for( j = 0 ; j < NUM ; j++ ){
            it = maptest.find(data2[ans2][j]);
            if ( it != maptest.end() ){
                chosen = data2[ans2][j];
                counts++;
            }
        }

        if ( counts == 1 )
            cout << "Case #" << tt << ": " << chosen << endl;
        else if (counts > 1 )
            cout << "Case #" << tt << ": Bad magician!" << endl;
        else
            cout << "Case #" << tt << ": Volunteer cheated!" << endl;
        tt++;
    }
return 0;
}
