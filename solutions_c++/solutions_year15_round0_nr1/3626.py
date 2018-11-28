#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("A-large.in","r",stdin);
	freopen("data.out","w",stdout);
	int cases,maxs;
	string digits;
	cin>>cases;
	for(int k=1; k<=cases; k++) {
        int flag=0;
        unsigned long long int ans = 0;
        unsigned long long int stands = 0;
        cin>>maxs;
        cin>>digits;
        for(int i=0; i<digits.length(); i++) {
            if(i == 0) {
            stands = stands + (int)digits[i] - 48;
            }
            else {
                if(stands < i) {
                    ans++;
                    flag = 1;
                }
                if(flag==1)
                    stands = stands + (int)digits[i] - 48 + 1;
                else
                    stands = stands + (int)digits[i] - 48;
            }
            flag=0;
            //cout<<"stands "<<stands<<endl;
            //cout<<"ans "<<ans<<endl;
        }
        cout<<"Case #"<<k<<": "<<ans<<endl;
	}
	return 0;
}

