#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

int main()
{
    ifstream cin("input.txt");
    ofstream cout("output.txt");
    int t;
    int c=0;
    cin>>t;
    while(t--){
            c++;
    int grid[4][4];
    int row1[4];
    int row2[4];
    int choice;
    cin>>choice;
    choice--;
    for(int i=0;i<4;i++){
    for(int j=0;j<4;j++){
        cin>>grid[i][j];
    }
    }
    for(int i=0;i<4;i++){
        row1[i]=grid[choice][i];
    }
    cin>>choice;
    choice--;
    for(int i=0;i<4;i++){
    for(int j=0;j<4;j++){
        cin>>grid[i][j];
    }
    }
    for(int i=0;i<4;i++){
        row2[i]=grid[choice][i];
    }
    set<int> same;
    for(int i=0;i<4;i++){
        for(int j=0;j<4;j++){
            if(row1[i]==row2[j])
                same.insert(row1[i]);
        }
    }
    cout<<"Case #"<<c<<": ";
    if(same.size()==1)
        cout<<*same.begin()<<endl;
    else if(same.size()==0)
        cout<<"Volunteer cheated!"<<endl;
    else
        cout<<"Bad magician!"<<endl;
    }
}
