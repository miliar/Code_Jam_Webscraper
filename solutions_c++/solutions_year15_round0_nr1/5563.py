#include <iostream>
#include <algorithm>
#include <limits>
#include <queue>
#include <vector>
#include <cmath>
#include <sstream>
#include <fstream>
using namespace std;

int main(){
	int T;
	int Tn;
	cin>>T;
	Tn = T;
	freopen("output.txt","w",stdout);
	while(T--){
		int S;cin>>S;
		string sh;
		int ar[S+1];
		
		cin>>sh;
		for(int i=0;i<S;i++)
		{
			ar[i]=sh[i]-'0';
			//cout<<ar[i]<<endl;
		}
		int num = 0;
		int buffer = 0 + ar[0];
		for(int i=1;i<=S;i++)
		{
			if(buffer>=i)
			{
				buffer = buffer + ar[i];
			}	
			else
			{
				num = num + (i-buffer);
				buffer = buffer + ar[i] + (i-buffer);
			}
		}
		cout<<"Case #"<<(Tn-T)<<": "<<num<<endl;
	}
}
