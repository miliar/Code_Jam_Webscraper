#include <iostream>

using namespace std;

int main()
{
    //freopen("aaa.in","r",stdin);
   // freopen("out.txt","w",stdout);
    int ans1,ans2,ar[6][6],t,seq1[6],seq2[6],i,j,ans,cas=0;
    cin>>t;
    while(t--){
        cin>>ans1;
        for(i=1;i<=4;i++){
            for(j=1;j<=4;j++){
                cin>>ar[i][j];
                if(i==ans1)
                seq1[j]=ar[i][j];
            }
        }
        cin>>ans2;
        for(i=1;i<=4;i++){
            for(j=1;j<=4;j++){
                cin>>ar[i][j];
                if(i==ans2)
                seq2[j]=ar[i][j];
            }
        }
        ans=0;
        for(i=1;i<=4;i++){
            for(j=1;j<=4;j++){
                if(seq1[i]==seq2[j]&&!ans)
                ans=seq1[i];
                else if(seq1[i]==seq2[j]&&ans){
                ans=-1;
                break;
                }
            }
            if(ans==-1)
            break;
        }
        if(ans>0)
        cout<<"Case #"<<++cas<<": "<<ans<<endl;
        else if(ans==-1)
        cout<<"Case #"<<++cas<<": Bad magician!"<<endl;
        else if(ans==0)
        cout<<"Case #"<<++cas<<": Volunteer cheated!"<<endl;
    }


    return 0;
}
