#include<iostream>
#include<cstdlib>

using namespace std;
int main () {
    long long int t,j=1,x,r,c;
    int type;
    cin>>t;
    while(t){
        t-=1;
        cin>>x>>r>>c;
        if((x>=7)||((r*c)%x!=0))
            type=1;
        else if(x==1||x==2)
            type=0;
        else{
            if(x==3){
                if((r%3==0&&c>=2)||(c%3==0&&r>=2))
                    type=0;
                else
                    type=1;
            }
            else if(x==4){
                if((r%4==0&&c>=3)||(c%4==0&&r>=3))
                    type=0;
                else
                    type=1;
            }
            else if(x==5){
                if((r%5==0&&c>=4)||(c%5==0&&r>=4))
                    type=0;
                else
                    type=1;
            }
           else if(x==6){
                if((r%6==0&&c>=5)||(c%6==0&&r>=5))
                    type=0;
                else
                    type=1;
            }

        }
        if(type==1)
            cout<<"Case #"<<j<<": RICHARD"<<endl;
        else
            cout<<"Case #"<<j<<": GABRIEL"<<endl;
        j++;
    }
    return 0;
}

