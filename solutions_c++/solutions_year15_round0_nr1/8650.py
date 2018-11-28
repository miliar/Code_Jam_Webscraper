#include<bits/stdc++.h>
#define f_in(st) freopen(st,"r",stdin);
#define f_out(st) freopen(st,"w",stdout);
using namespace std ;
int main(){
    f_out("A-large-out.txt");
    f_in("A-large.in");
    int test ;
    cin>>test;
    for(int xt = 1 ; xt <= test ; xt ++){
        int maxShy ;
        cin>>maxShy ;
        char audience[maxShy+1];
        for(int i = 0 ; i <= maxShy; i++)
            cin>>audience[i];
        int currentStanding = 0 ;
        int inviteNum = 0 ;
        for(int i = 0 ; i <= maxShy; i++){
           int currentLevel = i ;
            if (currentLevel <= currentStanding ){

                int temp = (int)audience[i]-'0';
                currentStanding += temp;
            }
            else{
                inviteNum += (currentLevel - currentStanding);
                currentStanding+=(currentLevel - currentStanding);
                int temp = (int)audience[i]-'0';
                currentStanding += temp;

            }
        }
        cout<<"Case #"<<xt<<": "<<inviteNum<<endl;


    }
return 0;}
