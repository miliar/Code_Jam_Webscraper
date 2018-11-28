#include<bits/stdc++.h>

#define MAX 100

using namespace std;

int main(){
    int T;
    long long int N;
    long long int x;
    bool flag=true;
    long long int num;
    int digit;
    bool bits[10];
    int c; 
    
    cin>>T;

    for(int i=1;  i<=T;  i++){

//        bits =0;
        for(int j=0;j<10;j++){
            bits[j]=false;
        }

        flag=false;

        cin>>N;
        
        //Cuerpo del programa
        if(N == 0)
            flag=true;
        else{
            for(int j=1; j<= MAX ; j++ ) {
                num=N*j;        
                x=num;
                while( num >= 1 ){
                    digit = num % 10;
                    num/=10;
                    bits[digit]=true;
                }
                /*
                if(bits == 15 ){
                    flag=false;
                    break;
                }*/
                c=0;
                for(int k=0; k<10; k++){
                    if(bits[k] == true){
                        c++;
                    }
                }

                if(c==10){
                    flag=false;
                    break;
                }

//                cout<<"j = "<< j <<endl;
            }
        
        }
            
        
        if(flag)//flag==true INSOMNIA
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
        else
            cout<<"Case #"<<i<<": "<<x<<endl;
    
    
    }

return 0;
}
