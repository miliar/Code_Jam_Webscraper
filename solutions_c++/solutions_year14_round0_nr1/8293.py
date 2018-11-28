#include<stdlib.h>
#include<string.h>
#include<vector>
#include<algorithm>
#include<fstream>
#include<iostream>
using namespace std;

int a[4][4],b[17],sol,counter;

int main(){
    int i,j;
    int t,t1;
    ifstream cin("1.in");
    ofstream cout("1.out");
    cin >> t;
    int x,y;
    for(t1=1;t1<=t;t1++){
        for(i=1;i<17;++i)b[i]=0;
        sol = 0;
        counter = 0;
        cin >> x;
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                cin >> y;
                if(i==x-1)b[y]++;
            }
        }
        cin >> x;
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                cin >> y;
                if(i==x-1)b[y]++;
            }
        }
        for(i=1;i<17;++i){
            if(b[i]==2){
                sol = i;
                counter++;
            }
        }
        cout << "Case #" << t1 << ": ";
        if(counter == 1)cout << sol << endl;
        else if(counter > 1)cout << "Bad magician!" << endl;
        else cout << "Volunteer cheated!" << endl;
    }
    
    scanf(" ");

}
