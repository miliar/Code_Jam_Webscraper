#include<bits/stdc++.h>
using namespace std;





int main(){

int t,x,r,c;

cin>>t;
int k=1;
while(t--){
           cin>>x>>r>>c;

           if(x==1)

             {cout<<"Case #"<<k<<": "<<"GABRIEL"<<endl;
              k++;continue;
             }

           if(x==2)
           {

             if((r==1 && c==1) || (r==1 && c==3) || (r==3 && c==1) || (r==3 && c==3))
            {cout<<"Case #"<<k<<": "<<"RICHARD"<<endl;
              k++;continue;
             }
             else{cout<<"Case #"<<k<<": "<<"GABRIEL"<<endl;
              k++;continue;
             }


            }
            if(x==3)
            {
            if((r==1 || c==1) || (c==2 && r==2))
            {cout<<"Case #"<<k<<": "<<"RICHARD"<<endl;
              k++;continue;
             }
            else
            {cout<<"Case #"<<k<<": "<<"GABRIEL"<<endl;
              k++;continue;
             }

            }

            if(x==4)
            {
            if((r==3 && c==4)|| (r==4 && c==3) || (r==4 && c==4))
            {cout<<"Case #"<<k<<": "<<"GABRIEL"<<endl;
              k++;continue;
             }
            else
             {cout<<"Case #"<<k<<": "<<"RICHARD"<<endl;
              k++;continue;
             }
             }






            }

}

