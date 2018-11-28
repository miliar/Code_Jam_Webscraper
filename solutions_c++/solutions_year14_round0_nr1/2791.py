#include<iostream>
#include<cstring>
#include<cstdio>
#include<fstream>
using namespace std;
int main()
{
    int t,l=1;
    ifstream cin("A-large.in");
	ofstream cout("a.txt");
    cin>>t;
    while(t--){
        int ans1,ans2,mat1[4][4],mat2[4][4],f=0,ans;
        cin>>ans1;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                cin>>mat1[i][j];
            }
        }
        cin>>ans2;
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                cin>>mat2[i][j];
            }
        }
        for(int i=0;i<4;i++){
            for(int j=0;j<4;j++){
                if(mat1[ans1-1][i]==mat2[ans2-1][j]){
                    f++;
                    ans=mat1[ans1-1][i];
                }
            }
        }
        cout<<"Case #"<<l<<": ";
        if(f==1)
            cout<<ans<<endl;
        else if(f>1)
                cout<<"Bad magician!"<<endl;
           else
                cout<<"Volunteer cheated!"<<endl;
            l++;


    }

}
