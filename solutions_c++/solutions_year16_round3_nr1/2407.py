#include<bits/stdc++.h>
using namespace std;
int main()
{
    //freopen("A-large.in","rt",stdin);
    //freopen("output.cpp","wt",stdout);
    int t;
    cin>>t;
    for(int tc=1;tc<=t;tc++){
        int n;
        cin>>n;
        int party[n];
        int total=0;
        for(int i=0;i<n;i++){
            cin>>party[i];
            total+=party[i];
        };
        cout<<"Case #"<<tc<<": ";
        int cnt=0;
        while(1){

            if(total==0){
                break;
            }
            //int greatest=-1e8,secondGreatest=-1e8;
            int greatestIndex=-1,secondGreatestIndex=-1;
            for(int i=0;i<n;i++){
                if(party[i]){
                    if(greatestIndex==-1){
                        greatestIndex=i;
                        continue;
                    }
                    if(party[i]>party[greatestIndex]){
                        greatestIndex=i;
                    }
                }
            }
            for(int i=0;i<n;i++){
                if(party[i]){
                    if(secondGreatestIndex==-1){
                        if(greatestIndex!=i){
                            secondGreatestIndex=i;
                        }
                        continue;
                    }
                    if(party[i]>party[secondGreatestIndex]){
                        if(greatestIndex!=i){
                            secondGreatestIndex=i;
                        }
                    }
                }
            }
            if(greatestIndex==-1){
                break;
            }
            if(total==3){
                cout<<char('A'+greatestIndex)<<" ";
                total--;
                party[greatestIndex]--;
                continue;
            }
            /*
            if(secondGreatestIndex==-1){
                cout<<char('A'+greatestIndex)<<" ";
                total--;
            }
            */
            if(party[greatestIndex]==party[secondGreatestIndex]){
                cout<<(char)(greatestIndex+'A')<<(char)(secondGreatestIndex+'A')<<" ";
                party[greatestIndex]--;party[secondGreatestIndex]--;
                total-=2;
            }
            else{
                cout<<(char)(greatestIndex+'A')<<(char)(greatestIndex+'A')<<" ";
                party[greatestIndex]-=2;
                total-=2;
            }
        }
        cout<<endl;
    }
    return 0;
}
