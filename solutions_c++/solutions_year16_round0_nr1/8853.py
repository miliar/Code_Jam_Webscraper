#include <iostream>
#include<set>
using namespace std;

int main() {
	int T, i,j=1;
	unsigned int N, temp;
	std::set<int> X;
	cin>>T;
	if(T>100)
	return 0;
	while(j<=T)
	{
	    cin>>N;
	    X.clear();
	    i=1;
	   while(1)
	    {
	        if(N==0)
	        {
	            cout<<"Case #"<<j<<": "<<"INSOMNIA"<<'\n';
	            break;
	        }
	        temp=i*N;
	        while(temp)
	        {
	            //cout<<temp%10;
	            X.insert(temp%10);
	            temp=temp/10;
	        }
	        if(X.size()==10)
	        {cout<<"Case #"<<j<<": "<<i*N<<'\n';
	        break;
	        }
	        i++;
	    }
	    
	    j++;
	}
	return 0;
}