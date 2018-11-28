#include<vector>
#include<iostream>
using namespace std;

int main(){
    int t;
    cin>>t;
    for(int test = 1; test <= t; test++){
        int row1;
        int row2;
        int arr[4][4];
        int arr2[4][4];
        cin>>row1;
        for(int i=0;i < 4;i++){
            for(int j=0; j < 4; j++){
                cin>>arr[i][j];
            }
        }
        vector<int> rowlist;
        vector<int> rowlist2;
        for(int i=0; i < 4; i++)
            rowlist.push_back(arr[row1 - 1][i]);
        cin>>row2;
        for(int i=0;i < 4;i++){
            for(int j=0; j < 4; j++){
                cin>>arr2[i][j];
            }
        }
        for(int i=0; i < 4; i++)
            rowlist2.push_back(arr2[row2 - 1][i]);

        vector<int> mergelist;
        for(int i=0; i < 4; i++){
            for(int j=0; j < 4; j++){
                if(rowlist[i] == rowlist2[j])
                    mergelist.push_back(rowlist[i]);
            }
        }
        if(mergelist.size()==0)
            cout<<"Case #"<<test<<": Volunteer cheated!"<<endl;
        else if(mergelist.size() > 1)
            cout<<"Case #"<<test<<": Bad Magician!"<<endl;
        else
            cout<<"Case #"<<test<<": "<<mergelist[0]<<endl;

    }
}
