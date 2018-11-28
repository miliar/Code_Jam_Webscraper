#include<iostream>
#include<iomanip>
#include<vector>
#include<string>
#include<algorithm>
#include<list>
#include<map>

using namespace std;

int main()
{	
	int t;
	cin>>t;
	for(int k=1; k<=t; k++){
        long long r,t;
        cin>>r>>t;
		long long sum=0;
        long long fir = 2*r+1;
        long long sec = 2*(r+2)+1;
        long long d = sec-fir;
        long long count =1;
        while(sum<=t)
        {
			sum =count*(2*fir+(count-1)*d)/2;
            if(sum>t)
				count--;
            else
				count++;
        }
		
		cout<<"Case #"<<k<<": "<<count<<endl;
	}
	return 0;
}