#include <iostream>
using namespace std;

int main()
{
    int n;
    cin>>n;
    for(int i = 1; i <= n; i++)
    {
        int k;
        cin>>k;
        if(k==0){
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
            continue;
        }
        bool arr[10];
        for(int j = 0; j < 10; j++){
            arr[j] = false;
        }
        int m = 1,num,temp;
        bool flag = true;
        while(flag){
            temp=num = k*m++;
            while(num!=0){
                int d = num%10;
                arr[d] = true;
                num/=10;
            }
            flag = false;
            for(int j = 0; j < 10; j++){
				if(!arr[j])
					flag = true;
            }
        }
        cout<<"Case #"<<i<<": "<<temp<<endl;
    }
    return 0;
}
