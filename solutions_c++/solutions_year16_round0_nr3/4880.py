#include <iostream>
#include <string>
#include <cstdio>
#include <math.h>
using namespace std;

int j = 50;

void print_binary(long long int n)
{
        long long int bit = 1<<14 - 1 , flag;
        long long int y[9]={0},x,f,num,div=0,div1,divisor[9]={0};
        f=14;
        while ( bit ) {
        	x = n & bit ? 1 : 0;
        	for(int i=0;i<9;i++)
            	y[i] = y[i] + x * pow(i+2,f);
        	f--;
        	bit >>= 1;
        }
        flag=1;
        for(int i=0;i<9;i++){
        	div=0;
            y[i] =  y[i]+pow(i+2,15)+1;
            num = y[i];
            if(num%2==0)
            	div=2;
            else if(num%3==0)
            	div=3;
            else{
            div1=5;
            while(div1*div1 <= num){
                if((num%div1)==0){
                	div = div1;
                    break;
				}
                if(num%(div1+2) == 0){
                	div=div1+2;
                	break;
				}
                    div1=div1+6;
                }
        	}
        	divisor[i] = div;
            if(div==0){
                flag=0;
                break;
            }
        }
        if(flag){
            cout<<y[8];
            for(int i=0;i<9;i++)
                cout<<" "<<divisor[i];
            cout<<endl;
            j--;
        }
        
}

int main(){
    long long int i=0,p,q,r; 
    freopen("C-small-attempt2.in","r",stdin);	
    freopen("output.txt","w",stdout);
    cin>>p>>q>>r;
    long long int n = 1<<14;
    cout<<"Case #"<<p<<":"<<endl;
    while(i<n && j){
        print_binary(i);
        i++;
    }
    return 0;
}