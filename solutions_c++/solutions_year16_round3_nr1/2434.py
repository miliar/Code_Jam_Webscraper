#include <unistd.h>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
#include <sstream>
using namespace std;

#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)
typedef long long ll;

int sum(int v[],int ct)
{
	int i,res=0;
	F0(i,ct) res+=v[i];
	return res;
}
int check_maj(int v[], int ct)
{
	int i,sm=sum(v,ct);
	float sm2=sm/2;
	F0(i,ct)
	{
		if(v[i]>sm2)
			return 0;
	}
	return 1;
}
int main(int argc, char const *argv[])
{
	freopen("A.in", "r", stdin);
	// freopen("A.out", "w", stdout);

	int tt, i,j, tn; cin >> tn;

	F1(tt,tn) {
		int ct;
		string ans="";
		cin>>ct;
		int v[ct];
		char c[ct];
		F0(i,ct)  cin>>v[i];
		while(sum(v,ct)!=0)
		{
			F0(i,ct)
			{if(sum(v,ct)==0)
				break;
			F0(j,ct)
			{

				if(v[i]!=0)
				{
					v[i]-=1;
					int maj=check_maj(v,ct);
					if(maj)
						{char cc=65+i; ans+=" "; ans.push_back(cc); }
					else
					{
						v[i]++;
						if(i!=ct-1)
						{
							if(v[j]!=0)
							{
								v[i]--;
								v[j]--;
								if(check_maj(v,ct))
								{
									char c1=65+i, c2=65+j; ans+=" ";
									ans.push_back(c1);
									ans.push_back(c2);
								}
								else
								{
									v[i]++;
									v[j]++;
								}
							}
						}
					}
				}
			}
			}
			// cout<<sum(v,ct)<<"\t"<<ans<<endl;
			// usleep(600000);
		}
		printf("Case #%d:", tt);
		// ans.
		cout << ans << endl;
	}

	return 0;
}