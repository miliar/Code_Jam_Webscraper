#include<iostream>
#include<conio.h>
#include<string.h>
#include<algorithm>
using namespace std;

int main() {
    int t,o=1;
    cin>>t;
    string a="GABRIEL";
    string b="RICHARD";
    while(t--)
    {
        int x,r,c,flag=0,p;
        cin>>x>>r>>c;
        p=r*c;
        if(x==1)
            flag=1;
        else if((x==2)&&(p%2==0))
            flag =1;
        else if((x==3)&&(p%3==0)&&(p>3))
            flag=1;
        else if((x==4)&&((p==12)||(p==16)))
                flag=1;

if(flag==1)
            cout<<"Case #"<<o<<": "<<a<<endl;
        else 
            cout<<"Case #"<<o<<": "<<b<<endl;
o++;
    }
        

        

    
    getch();
return 0;         
}
