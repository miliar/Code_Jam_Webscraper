#include <iostream>
using namespace std;

int main(){
        int t;
            int first[4][4], second[4][4];
                int r1,r2;
                    cin>>t;
                        int sol;//0=Volunteer cheated;-1->Bad Magician else answer
                            for(int n=1;n<=t;n++){
                                        sol=0;
                                                cin>>r1;
                                                        for(int i=0;i<4;i++){
                                                                        for(int j=0;j<4;j++){
                                                                                            cin>>first[i][j];
                                                                                                        }
                                                                                }
                                                                cin>>r2;
                                                                        for(int i=0;i<4;i++){
                                                                                        for(int j=0;j<4;j++){
                                                                                                            cin>>second[i][j];
                                                                                                                        }
                                                                                                }
                                                                                for(int i=0;i<4;i++){
                                                                                                for(int j=0;j<4;j++){
                                                                                                                    if(first[r1-1][i]==second[r2-1][j]){
                                                                                                                                            if(sol==0){
                                                                                                                                                                        sol = first[r1-1][i];
                                                                                                                                                                                            } else if (sol==-1){
                                                                                                                                                                                                                        sol = -1;
                                                                                                                                                                                                                                            } else {
                                                                                                                                                                                                                                                                        sol=-1;
                                                                                                                                                                                                                                                                                            }
                                                                                                                                                            }
                                                                                                                                }
                                                                                                        }
                                                                                        cout<<"Case #"<<n<<": ";
                                                                                                switch (sol) {
                                                                                                                case -1 : cout<<"Bad magician!"<<endl;
                                                                                                                                            break;
                                                                                                                                    case 0 : cout<<"Volunteer cheated!"<<endl;
                                                                                                                                                                break;
                                                                                                                                                        default : cout<<sol<<endl;
                                                                                                                                                                        }
                                                                                                    }
                                return 0;
}

