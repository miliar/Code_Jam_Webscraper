#include<iostream>

using namespace std;

int main(){

int T;

int arr1[10][10], arr2[10][10];
//freopen("G:\\ACM\\CodeJam2014\\A-small-attempt0.in","r",stdin);
//freopen("G:\\ACM\\CodeJam2014\\magic_out.txt","w",stdout);

cin>>T;

for(int t=1; t<=T; t++){

    int row1, row2;

    cin>>row1;

    for(int i=1;i<=4;i++)
            for(int j=1;j<=4; j++)
                cin>>arr1[i][j];

    cin>>row2;

        for(int i=1;i<=4;i++)
            for(int j=1;j<=4; j++)
                cin>>arr2[i][j];

    int found=0, val, ans=-1;
    for(int j=1; j<=4; j++){
        val = arr1[row1][j];
        for(int jj=1;jj<=4;jj++){
            if(val==arr2[row2][jj]) {found++; ans=val;}
        }
    }

    cout<<"Case #"<<t<<": ";
    if(found==1) cout<<ans;
    else if(found==0) cout<<"Volunteer cheated!";
    else cout<<"Bad magician!";

    cout<<endl;
}
return 0;
}
