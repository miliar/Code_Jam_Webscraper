#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <math.h>
#include <set>
#include <sstream>


#define forf(a,b) for(a=0;a<b;a++)
#define forb(a,b) for(a=b;a>0;a--)
#define count(a) for (int zzz=0;zzz<a;zzz++)
#define PI 3.14159265358979
#define MILLION 1000000
#define BILLION 1000000000
using namespace std;

int main()
{
    freopen("A-small-attempt2.in","r",stdin);
    freopen("swag.txt","w",stdout);
    int T, ans1, ans2;
    //cout<<"hi"<<endl;
    cin>>T;
    for (int i=0;i<T;i++){
        int board[4][4]={};
        int board2[4][4]={};
        cin>>ans1;
        ans1--;
        for (int j=0;j<4;j++){
            for (int k=0;k<4;k++){
                cin>>board[j][k];
            }
        }
        cin>>ans2;
        ans2--;
        for (int j=0;j<4;j++){
            for (int k=0;k<4;k++){
                cin>>board2[j][k];
            }
        }
        int flag=0;
        int answer=0;
        for (int j=0;j<4;j++){
            for (int k=0;k<4;k++){
                if (board[ans1][j]==board2[ans2][k]){
                    answer=board[ans1][j];
                    flag+=1;
                }
            }
        }
        if (flag==0){
            cout<<"Case #"<<i+1<<": Volunteer cheated!"<<endl;

        }
        else if (flag==1){
            cout<<"Case #"<<i+1<<": "<<answer<<endl;
        }
        else{
            cout<<"Case #"<<i+1<<": Bad magician!"<<endl;
        }


    }
    return 0;
}
