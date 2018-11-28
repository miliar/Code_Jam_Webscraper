#include <iostream>
using namespace std;

int main() {
    int arr[10]={0};
    int t;
    long int n;
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        int flg;
        cin>>n;
        flg=0;
        arr[0]=arr[1]=arr[2]=arr[3]=arr[4]=arr[5]=arr[6]=arr[7]=arr[8]=arr[9]=0;
        if(n==0)
            cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
        else
        {
        int tmp=n;
        int mul=n;
        int sum=0;
        while(flg==0)
        {
            while(tmp!=0)
            {
                arr[tmp%10]=1;
                tmp=tmp/10;
            }
            sum=arr[0]+arr[1]+arr[2]+arr[3]+arr[4]+arr[5]+arr[6]+arr[7]+arr[8]+arr[9];
            if(sum == 10)
            {
                cout<<"Case #"<<i<<": "<<mul<<endl;
                flg=1;
            }
            tmp=mul+n;
            mul=tmp;
        }
        }
    }
	return 0;
}
