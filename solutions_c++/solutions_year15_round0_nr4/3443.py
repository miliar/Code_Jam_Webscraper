#include <cstdio>
#include <iostream>
int main(){
    int t ,x,r,c,p=1 ;
    cin>>t;
    while(t--){
    cin>>x>>r>>c;
    if(x==1){
        cout<<"Case #"<<p<<": Gabriel"<<endl; 
    }
    else if(x==2){
        if(r%2==0||c%2==0)
            cout<<"Case #"<<p<<": Gabriel"<<endl;
        else
            cout<<"Case #"<<p<<": Richard"<<endl;
    }
    else if (x==3){
        if(r>=2&&c>=2&&(r*c)%3==0)
				cout<<"Case #"<<p<<": Gabriel"<<endl;
            else
				cout<<"Case #"<<p<<": Richard"<<endl;
    }
    else if(x==4)
        if(r>=3&&c>=3&&(r*c)%4==0)
			cout<<"Case #"<<p<<": Gabriel"<<endl;
        else
			cout<<"Case #"<<p<<": Richard"<<endl;
    else if(x==5)
        if(r*c>=20&&(r*c)%5==0)
			cout<<"Case #"<<p<<": Gabriel"<<endl;
        else
			cout<<"Case #"<<p<<": Richard"<<endl;
    else if(x==6)
        if((r*c)>=30&&(r*c)%6==0)
			cout<<"Case #"<<p<<": Gabriel"<<endl;
        else
			cout<<"Case #"<<p<<": Richard"<<endl;
    else
    {
     cout<<"Case #"<<p<<": Richard"<<endl;
 
    }
    p++;
 
    }
    return 0;
}
