#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
using namespace std;
int main(){
    int tc;
    cin>>tc;
    char arr[2][10]={"RICHARD","GABRIEL"};
    for(int t=1;t<=tc;++t){
        printf("Case #%d: ",t);
        int x,r,c;
        cin>>x>>r>>c;
        if(x>(max(r,c))||min(r,c)<x-1){
            printf("%s\n",arr[0]);
        }
        else if(x==1){
            printf("%s\n",arr[1]);
        }
        else if(x==2){
            printf("%s\n",arr[!((r*c)&1)]);
        }
        else if(x==3){
            if(((r*c)%3)==0){
                printf("%s\n",arr[1]);
            }
            else{
                printf("%s\n",arr[0]);
            }
        }
        else if(x==4){
            if(((r*c)%4)==0){
                printf("%s\n",arr[1]);
            }
            else{
                printf("%s\n",arr[0]);
            }
        }
        else if(x==5){
            
        }
        else if(x==6){
            
        }
        else{
            printf("%s\n",arr[0]);
        }
    }   
}
