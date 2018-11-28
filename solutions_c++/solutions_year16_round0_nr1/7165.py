#include <iostream>
using namespace std;

int main() {
	long long int t,n,i,test[10],temp,r,mul,num;
    bool test1=true;
	cin>>t;
	for(i=0;i<t;i++)
	{
		cin>>n;
        test[0]=0;
        test[1]=0;
        test[2]=0;
        test[3]=0;
        test[4]=0;
        test[5]=0;
        test[6]=0;
        test[7]=0;
        test[8]=0;
        test[9]=0;
		mul=2;
		num=n;
		if(n==0)
		cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
        else
		{
		while(test1)
		{
			temp=num;
		    while(temp)
		    {
			r=temp%10;
			test[r]=1;
			temp=temp/10;
		    }
		    if(test[0]==1)
		    if(test[1]==1)
		    if(test[2]==1)
		    if(test[3]==1)
		    if(test[4]==1)
		    if(test[5]==1)
		    if(test[6]==1)
		    if(test[7]==1)
		    if(test[8]==1)
		    if(test[9]==1)
		    {
		    	cout<<"Case #"<<i+1<<" "<<num<<endl;
		        goto xy;
		    }


		    	num=n*mul;
		    	mul++;

		}

		}
		xy:  ;
	}

	return 0;
}
