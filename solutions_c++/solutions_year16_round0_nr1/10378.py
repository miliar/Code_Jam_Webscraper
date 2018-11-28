#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
//freopen("A-small-attempt0.in","r",stdin);
//freopen("sheep.out","w",stdout);


int main() {
    long long int N,T;
    long long int casen=0;
    cin>>T;
    while(T--)
    {   casen++;
        cin>>N;
        if(N==0)
        {
        cout<<"Case #"<<casen<<":"<<" "<<"INSOMNIA"<<endl;
        continue;
        }
        else{
        long long int table[10]={0,0,0,0,0,0,0,0,0,0};
        long long int temp=N,i=1,flag=1,temp1,temp2;
        while(flag)
        {
            temp1=i*N;
            temp2=temp1;
            i++;
            while(temp1)
            {
                table[(temp1%10)]++;
                temp1/=10;
            }
            for(int i=0;i<10;i++)
            {
                if(table[i]==0)
                break;
                else if(i==9) flag=0;
            }
            
        }
        if(flag==0)
                cout<<"Case #"<<casen<<":"<<" "<<temp2<<endl;

            
    }     }
	return 0;
}


