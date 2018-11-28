#include <iostream>

using namespace std;

int main(){
    int i;
    cin>>i;
    int cong=1;
    while(i--){

        int e2,j1,x;
        cin>>j1;
        int c1[4][4];
        for(int col=0;col<4;col++){
            for(int fi=0;fi<4;fi++){
                cin>>x;
                c1[col][fi]=x;
            }
        }

        int c2[4][4];
        cin>>e2;
        for(int col=0;col<4;col++){
            for(int fi=0;fi<4;fi++){
                cin>>x;
                c2[col][fi]=x;
            }
        }

        int res,res2,cont=0,outP;
        for(int col=0;col<4;col++){
                res=c1[j1-1][col];
                //cout<<res;
                for(int de=0;de<4;de++){
                    //cout<<c2[e2-1][de];
                   if(res==c2[e2-1][de]){
                        outP=c2[e2-1][de];
                        cont++;
                   }
            }
            //cout<<endl;
        }

        if(cont==1){
            cout<<"Case #"<<cong<<": "<<outP<<endl;
            cong++;
        }else{
                if(cont>1){
                    cout<<"Case #"<<cong<<": "<<"Bad magician!"<<endl;
                    cong++;
                }
                else{
                    if(cont==0){
                        cout<<"Case #"<<cong<<": "<<"Volunteer cheated!"<<endl;
                        cong++;
                    }
                }
            }


    }

}
