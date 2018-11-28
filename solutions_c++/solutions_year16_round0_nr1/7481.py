#include <iostream>
using namespace std;
int main() {
    int n,a,i,j,temp;
    bool check[10];
    cin>>n;
    for(i=0 ; i<n ; i++){
        for(j=0 ; j<10 ; j++) check[j]=false;
        cin >> a;
        if(a==0) cout << "Case #" << i+1 << ": " << "INSOMNIA"<< endl;
        else{
                for(j=1 ; j<1000 ; j++){
                    temp=j*a*10;
                    while(temp>=10){
                    temp/=10;
                    if(temp%10==1) check[1]=true;
                    else if(temp%10==2) check[2]=true;
                    else if(temp%10==3) check[3]=true;
                    else if(temp%10==4) check[4]=true;
                    else if(temp%10==5) check[5]=true;
                    else if(temp%10==6) check[6]=true;
                    else if(temp%10==7) check[7]=true;
                    else if(temp%10==8) check[8]=true;
                    else if(temp%10==9) check[9]=true;
                    else if(temp%10==0) check[0]=true;
                    }
                    if(check[0]&&check[1]&&check[2]&&check[3]&&check[4]&&check[5]&&check[6]&&check[7]&&check[8]&&check[9]) {
                        cout << "Case #" << i+1 << ": " << a*j << endl;
                        break;
                    }
                }
        }
    }
    return 0;
}
