#include<bits/stdc++.h>
using namespace std;
#define ull unsigned long long int
int main()
{
	int t,maxs;
	string dig;
	cin>>t;
	for(int t1=1; t1<=t; t1++) {
        int flag=0;
        ull ans = 0;
        ull std = 0;
        cin>>maxs;
        cin>>dig;
        for(int i=0; dig[i]!='\0'; i++)
        {
            flag=0;
            if(i == 0)
            std = std + dig[i] - 48;
            else
            {
                if(std < i)
                {
                    ans++;
                    flag = 1;
                }
                std += dig[i] - 48;
                if(flag==1)
                     std++;
            }
        }
        cout<<"Case #"<<t1<<": "<<ans<<endl;
	}
	return 0;
}

