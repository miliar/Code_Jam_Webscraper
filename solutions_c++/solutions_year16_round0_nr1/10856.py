#include <iostream>
using namespace std;

int main() {
    long t,n,i,j,tc=0,d,num,flag,number,ht[10]={0};
    cin>>t;
    while(tc++<t)
    {
        cin>>n;
        flag=0;
        i=1;
        for(j=0;j<10;j++)
            ht[j]=0;
        while(true)
        {
            num=i*n;
            number=num;
            if(i*n==(i+1)*n&&i*n==(i+2)*n)  break;
            while(num!=0)
            {
                d=num%10;
                num=num/10;
                ht[d]=1;
            }
            for(j=0;j<10;j++)
                if(ht[j]==0)
                    break;
            if(j==10) 
            {
                flag=1;
                break;
            }
            
            ++i;
        }
        if(flag==1) cout<<"Case #"<<tc<<": "<<number<<endl;
        else        cout<<"Case #"<<tc<<": "<<"INSOMNIA"<<endl;
        
    }
	return 0;
}
