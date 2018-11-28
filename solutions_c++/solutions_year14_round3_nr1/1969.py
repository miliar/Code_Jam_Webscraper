#pragma warning(disable:4996)
#include<stdio.h>
#include<string.h>
#include<iostream>
using namespace std;
int getCommonMutiple(int a, int b){
    int r = a%b;
    if(r != 0){
        a = b;
        b = r;
        getCommonMutiple(a ,b);
    }
    return b;
}


int main()
{
	int TC, T, P,Q,i,j;
    char c;
    int num=0;
    int factor = 0;
    bool doable = false;
	cin>>TC;
	for (T = 1; T <= TC; T++){
		cout<<"Case #"<<T<<":";
		cin>>P>>c>>Q;
        num =0;
		factor = getCommonMutiple(Q,P);
        doable = true;
        
        Q = Q/factor;
        P = P/factor;
        i = Q;
        while (i!=1) {
            if(i%2!=0){
                doable = false;
                break;
            }
            else{
                i = i>>1;
            }
        }
        if(!doable)
            cout<<"impossible"<<endl;
        else{
            j = Q/P;
            while (j>1) {
                num++;
                j = j>>1;
            }
            cout<<num<<endl;
        }
	}
}