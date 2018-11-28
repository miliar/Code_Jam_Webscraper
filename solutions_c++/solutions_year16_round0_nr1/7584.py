#include <bits/stdc++.h>
using namespace std;
int main(){
freopen("D:\\A-large.in","r",stdin);
freopen("D:\\outputFileName.txt","w",stdout);
	int t;
	cin>>t;
	for(int i=1;i<=t;i++){
        int pot[10];
        memset(pot,0,sizeof(pot));
        unsigned long long int x;
        cin>>x;
        if(x==0){
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
            continue;
        }
        unsigned long long int y=x;
        int fau=1;
        for(int j=1;j<=10000;j++){
            y=x*j;
            ostringstream convert;

            convert << y;
        string g= convert.str();
            for(int h=0;h<g.size();h++){
                char m=g.at(h);
                int u=m-'0';
                pot[u]=1;

            }
            fau=1;
            for(int b=0;b<10;b++){
                if(pot[b]==0){
                    fau=0;
                    break;
                }
            }
            if(fau==1)
                break;

        }
        if(fau==0)cout<<"Case #"<<i<<": INSOMNIA"<<endl;
        else if(fau==1)
        cout<<"Case #"<<i<<": "<<y<<endl;
	}
}
