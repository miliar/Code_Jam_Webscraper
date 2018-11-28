#include <bits/stdc++.h>
#define ok cout << "ok"
#define open freopen("A-small-attempt1.in","r",stdin)
#define close freopen("output.txt","w",stdout)
using namespace std;

int main(){
    open;
    close;
    int n;
    cin >> n;
    for(int i=1;i<=n;i++)
    {
        int first;
        cin >> first;
        int firstArray[5][5];
        for(int j=1;j<=4;j++)
        {
            for(int k=1;k<=4;k++)
            {
                cin >> firstArray[j][k];
            }
        }
        int second;
        cin >> second;
        int secondArray[5][5];
        for(int j=1;j<=4;j++)
        {
            for(int k=1;k<=4;k++)
            {
                cin >> secondArray[j][k];
            }
        }

        bool f = false;
        vector <int> v;
        for(int j=1;j<=4;j++)
        {
            for(int k=1;k<=4;k++)
            {
                if(firstArray[first][j] == secondArray[second][k]){
                    v.push_back(firstArray[first][j]);
                }
            }
        }
        cout << "Case #" << i << ": ";
        if(v.size()==1){
            cout << v[0];
        }else if(v.size()>1){
            cout << "Bad magician!";
        }else if(v.size()==0){
            cout << "Volunteer cheated!";
        }
        cout << endl;
    }
    return 0;
}
