#include<iostream>
#include<vector>
using namespace std;
int main(){
    int t,m,j,i,pp,ll;
    cin>>t;
    for(ll=1;ll<=t;ll++){
        int n1,n2;
        vector<int> kk(17,-1),kk2(17,-1);
        cin>>n1;
        n1--;
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                cin>>pp;
                if(i==n1)
                    kk[pp]=1;
            }
        }
        cin>>n2;
        n2--;
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                cin>>pp;
                if(i==n2)
                    kk2[pp]=0;
            }
        }
        int c=0;
        for(i=1;i<17;i++){
            if(kk[i]==1 && kk2[i]==0){
                c++;
                m=i;
            }
        }
        if(c==1)
            cout<<"Case #"<<ll<<": "<<m<<endl;
        else if(c>1)
            cout<<"Case #"<<ll<<": "<<"Bad magician!"<<endl;
        else if(c==0)
            cout<<"Case #"<<ll<<": "<<"Volunteer cheated!"<<endl;
    }
    return 0;
}
