#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
{
    //freopen("input_file.txt","r",stdin);
    //freopen("output_file.txt","w",stdout);
    int T;
    cin >> T;
    for(int j=1;j<=T;j++) {
        int n;
        cin >> n;
        int i=1,flag=1,a,ans,get[10]={0},count=0;
    if(n>0) {
        while(flag==1) {
            a=n*i;
            ans=a;
            while(a>0) {
                int b=a%10;
                    if(b==0 && get[0]==0){
                            count++;
                            get[0]=1;
                    }
                    else if(b==1 && get[1]==0) {
                        count++;
                        get[1]=1;
                    }
                    else if(b==2 && get[2]==0) {
                        count++;
                        get[2]=1;
                    }
                    else if(b==3 && get[3]==0) {
                        count++;
                        get[3]=1;
                    }
                    else if(b==4 && get[4]==0) {
                        count++;
                        get[4]=1;
                    }
                    else if(b==5 && get[5]==0) {
                        count++;
                        get[5]=1;
                    }
                    else if(b==6 && get[6]==0) {
                        count++;
                        get[6]=1;
                    }
                    else if(b==7 && get[7]==0) {
                        count++;
                        get[7]=1;
                    }
                    else if(b==8 && get[8]==0) {
                        count++;
                        get[8]=1;
                    }
                    else if(b==9 && get[9]==0) {
                        count++;
                        get[9]=1;
                    }
                a=a/10;
            }
            if(count==10) {
                cout <<"Case #"<<j<<":"<<" "<<ans<<endl;
                flag=0;
            }
             else if(j>500) {
                cout <<"Case #"<<j<<":"<<" "<<"INSOMNIA"<<endl;
                flag=0;
             }
            i++;
        }
    }
       else {
            cout <<"Case #"<<j<<":"<<" "<<"INSOMNIA"<<endl;
            flag=0;
        }

    }
}
