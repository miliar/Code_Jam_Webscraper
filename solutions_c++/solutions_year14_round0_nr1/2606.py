using namespace std;
#include<iostream>
int main(){
    int T,row[2],trick[4][4],trick2[4][4],ans;

    cin>>T;
    for(int i=0;i<T;i++){
            int flag = 0;
            cin>>row[0];
            row[0]=row[0]-1;
            for(int r=0;r<4;r++){
                for(int c=0;c<4;c++){
                    cin>>trick[r][c];
                }
            }

            cin>>row[1];
            row[1]=row[1]-1;
            for(int r=0;r<4;r++){
                for(int c=0;c<4;c++){
                    cin>>trick2[r][c];
                }
            }

            for(int r=0;r<4;r++){
                for(int c=0;c<4;c++){
                   if(trick[row[0]][r]==trick2[row[1]][c]){
                        ans=trick[row[0]][r];
                        flag++;
                   }
                }
            }
            if(flag==1){
                cout<<"Case "<<"#"<<i+1<<": "<<ans<<endl;
            }
            else if(flag>1){
                cout<<"Case "<<"#"<<i+1<<": Bad magician!"<<endl;
            }
            else{
                cout<<"Case "<<"#"<<i+1<<": Volunteer cheated!"<<endl;
            }

    }
    return 0;
}
