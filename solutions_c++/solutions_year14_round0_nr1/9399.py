#include <iostream>

using namespace std;

int main()
{
    int T,n,temp;
    int a,b;
    int tempa[5],tempb[5];
    int t1[5][5],t2[5][5];
    cin>>n;
    for(int i=1;i<=n;i++){
        cin>>a;
        for(int j=1;j<=4;j++){
            for(int k=1;k<=4;k++){
                    if(j==a){
                        cin>>tempa[k];
                    }else{
                        cin>>temp;
                    }
            }
        }
        cin>>b;
        for(int j=1;j<=4;j++){
            for(int k=1;k<=4;k++){
                    if(j==b){
                        cin>>tempb[k];
                    }else{
                        cin>>temp;
                    }
            }
        }
        int count=0,ans;
        if(tempa[1]==tempb[1]||tempa[1]==tempb[2]||tempa[1]==tempb[3]||tempa[1]==tempb[4]){
            count++;
            ans=tempa[1];
        }
        if(tempa[2]==tempb[1]||tempa[2]==tempb[2]||tempa[2]==tempb[3]||tempa[2]==tempb[4]){
            count++;
            ans=tempa[2];
        }
        if(tempa[3]==tempb[1]||tempa[3]==tempb[2]||tempa[3]==tempb[3]||tempa[3]==tempb[4]){
            count++;
            ans=tempa[3];
        }
        if(tempa[4]==tempb[1]||tempa[4]==tempb[2]||tempa[4]==tempb[3]||tempa[4]==tempb[4]){
            count++;
            ans=tempa[4];
        }
        if(count==1)
            cout<<"case #"<<i<<": "<<ans<<endl;
        else if(count>1)
            cout<<"case #"<<i<<": Bad magician!"<<endl;
        else
            cout<<"case #"<<i<<": Volunteer cheated!"<<endl;
    }
    return 0;
}
