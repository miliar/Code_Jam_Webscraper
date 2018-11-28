#include<iostream>
#include<string>
#include<stdio.h>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
    int t;
    cin>>t;
    string str;
    int ro;

    for (int i = 0; i<t; i++){
        int ans1,ans2, temp, j, k;
        int row1[4], row2[4];
        cin>>ans1;
        for(j = 0; j < ans1-1; j++)
            for(k = 0; k < 4; k++) cin>>temp;

        for(j = 0;j<4;j++)  cin>>row1[j];

        for(int j = ans1; j < 4; j++)
            for(k = 0; k < 4; k++) cin>>temp;

        cin>>ans2;

        for(j = 0; j < ans2-1; j++)
            for(k = 0; k < 4; k++) cin>>temp;

        for(j = 0;j<4;j++)  cin>>row2[j];

        for(j = ans2; j < 4; j++)
            for(int k = 0; k < 4; k++) cin>>temp;

        int found = 0, card = 0;
        for(j = 0; j<4; j++) {
            for(k = 0; k<4; k++){
                if(row1[j] == row2[k])  { found++;
                  card = row1[j];
                }
            }
        }
        cout<<"Case #"<<i+1<<": ";
        if(found == 0)  cout<<"Volunteer cheated!"<<endl;
        else if(found == 1)  cout<<card<<endl;
        else if(found >= 2)  cout<<"Bad magician!"<<endl;
    }
    getchar();
    return 0;
}
