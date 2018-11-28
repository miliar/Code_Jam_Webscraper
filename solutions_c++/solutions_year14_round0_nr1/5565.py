#include<cstdio>
#include<cstdlib>
#include<algorithm>
#include<iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    int blah=1;
    while(n--){
        int cards[4][4];
        int i=0,j=0;
        int row;
        cin>>row;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>cards[i][j];
            }
        }
        int row1;
        int cards2[4][4];
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++){
                cin>>cards2[i][j];
            }
        }
        int flag=0;
        int chu[4];
        int k=0;
        for(i=0;i<4;i++){
            for(j=0;j<4;j++)
            {
                if(cards[row-1][i]==cards2[row1-1][j])
                {
                    flag++;
                    chu[k++]=cards[row-1][i];
                }
            }
        }
        if(flag==0)
        {
            cout<<"Case #"<<blah<<": Volunteer cheated!"<<endl;
        }
        if(flag==1)
        {cout<<"Case #"<<blah<<": "<<chu[0]<<endl;
        }
        if(flag>1){
            cout<<"Case #"<<blah<<": Bad magician!"<<endl;
        }
    }
    return 0;
}





