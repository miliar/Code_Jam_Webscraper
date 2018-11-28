#include <iostream>
#include<string>
#include<vector>

using namespace std;
 
int main() {
       freopen("input.txt","r",stdin);
        freopen("output.txt","w",stdout);

		int casesNum,count=0;
		cin>>casesNum;
		while(casesNum!=0)
		{
			int friendsNumber=0,standing=0,Smax;
			string audience;
		
			cin>>Smax>>audience;
			count++;
			for(int x=0;x<audience.size();x++)
			{

				int num = audience[x] - '0';
				if(standing>=x)
					standing+=(num);	
				else
				{
					friendsNumber+=(x-standing);
					standing+=(num+(x-standing));	
				}
			}
		
			cout<<"Case #"<<count<<": "<<friendsNumber<<endl;
			casesNum--;
		}

		return 0;
}