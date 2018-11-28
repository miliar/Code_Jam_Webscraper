#include<iostream>
#include<algorithm>
using namespace std;

int main(){

int T, N;
double Naomee[1100], Kent[1100];

//freopen("G:\\ACM\\CodeJam2014\\D-large.in","r",stdin);
//freopen("G:\\ACM\\CodeJam2014\\war_out.txt","w",stdout);

cin>>T;

for(int t=1; t<=T; t++){
    cin>>N;

    for(int i=0; i<N; i++) cin>>Naomee[i];
    for(int i=0; i<N; i++) cin>>Kent[i];

    sort(Naomee, Naomee+N);
    sort(Kent, Kent+N);

    int tot_war = N;
    int tot_dec = 0;
    double Naomee_val;
    int ind=0;

    for(int i=0; i<N; i++){
        Naomee_val = Naomee[i];
        for(int j=ind;j<N;j++)
        {
            if(Kent[j]>Naomee_val){
                ind=j+1;
                tot_war--;
                break;
            }
        }
    }
    double Kent_val;
    for(int i=N-1; i>=0; i--){
        Kent_val = Kent[i];
        for(int j=0;j<N;j++){
            if(Naomee[j]>Kent_val){
               tot_dec++;
               Naomee[j]=-1;
               break;
            }
        }
    }

cout<<"Case #"<<t<<": "<<tot_dec<<" "<<tot_war<<endl;;

}

return 0;
}
