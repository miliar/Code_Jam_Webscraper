#include <iostream>
using namespace std;

int main() {
    int T, smax, sum, inc;
    string str;
    cin>>T;
    int i=0;
    while(T-->0)
    {
    
        sum=0;
        inc=0;
        cin>>smax>>str;
        for(int k=0; k<=smax; k++)
        {
            if(str[k]-48!=0 && sum<k)
            {
                inc=inc+k-sum;
                sum=sum+inc;
            }
            sum=sum+(str[k]-48);
      }
        cout<<"Case #"<<i+1<<":"<<" "<<inc<<endl;
        i++;
    }
	return 0;
}
