#include<iostream>
#include<vector>
#include<iomanip>
#include<string>

using namespace std;

int main(){

    int T, N, pos[1000], ppos[1000], NDCount, NOCount, flag, max;
    double Naomi[1000], Ken[1000], temp;

    cin>>T;

    for(int run=0; run<T; run++){

        cin>>N;
        for(int j=0; j<N; j++){
            cin>>Naomi[j];
        }
        for(int j=0; j<N; j++){
            cin>>Ken[j];
            pos[j]=1;
            ppos[j]=1;
        }
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                if(Naomi[i]<Naomi[j]){
                    temp=Naomi[i];
                    Naomi[i]=Naomi[j];
                    Naomi[j]=temp;
                }
                if(Ken[i]<Ken[j]){
                    temp=Ken[i];
                    Ken[i]=Ken[j];
                    Ken[j]=temp;
                }
            }
        }
        NDCount=0;
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                if(Naomi[i]>Ken[j]&&ppos[j]==1){
                    ppos[j]=0;
                    NDCount++;
                    break;
                }
            }
        }
        NOCount=0;
        for(int i=0; i<N; i++){
            flag=0;
            for(int j=0; j<N; j++){
                if(Ken[j]>Naomi[i]&&pos[j]==1){
                    flag=1;
                    pos[j]=0;
                    break;
                }
            }
            if(flag==0){
                NOCount++;
            }
        }
        cout<<"Case #"<<run+1<<": "<<NDCount<<" "<<NOCount<<endl;

    }

    return 0;
}
