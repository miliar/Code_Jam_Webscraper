#include <iostream>
using namespace std;
int T,i1;
int main(){
	freopen("1in.txt","r",stdin);
	freopen("1out.txt","w",stdout);
    cin>>T;
    for(i1=0;i1<T;i1++){
        int g,i,j,an1,an2,k[17][2];
        cin>>an1;
        for(i=1;i<=4;i++)
            for(j=0;j<4;j++){
                cin>>g;
                k[g][0]=i;
            }
        cin>>an2;
        for(i=1;i<=4;i++)
            for(j=0;j<4;j++){
                cin>>g;
                k[g][1]=i;
            }
        bool flag=false,flag1=false;
        int ans;
        for(i=1;i<17;i++){
            if(k[i][0]==an1&&k[i][1]==an2){
                if(flag==true){
                    cout<<"Case #"<<i1+1<<": "<<"Bad magician!"<<endl;
					flag1=true;
					break;
				}
                else{
                    ans=i;
                    flag=true;
                }
            }
        }
		if(!flag1){
			if(flag==false)
				cout<<"Case #"<<i1+1<<": "<<"Volunteer cheated!"<<endl;
			else 
				cout<<"Case #"<<i1+1<<": "<<ans<<endl;
		}
    }
}