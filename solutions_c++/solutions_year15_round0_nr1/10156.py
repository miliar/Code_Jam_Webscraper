#include <iostream>
using namespace std;

int main() {
    int t, smax, sum, count;
    string a;
    cin>>t;
    for(int i=0; i<t; i++)
    {
        sum=0;
        count=0;
        cin>>smax;
        cin>>a;
        /*for(int j=0; j<=smax; j++)
        {
            cin>>a[i];
        }*/
        for(int j=0; j<=smax; j++)
        {
            if(a[j]-48!=0 && sum<j)
            {
                count=count+j-sum;
                sum=sum+count;
            }
            sum=sum+(a[j]-48);
            //cout<<sum<<endl;
        }
        cout<<"Case #"<<i+1<<":"<<" "<<count<<endl;
    }
	// your code goes here
	return 0;
}
