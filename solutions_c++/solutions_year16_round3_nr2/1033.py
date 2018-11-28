#include<bits/stdc++.h>
using namespace std;
int main()
{
ifstream in;
ofstream out;
in.open("B-large.in");
out.open("output.out");

int T;
in>>T;
for(int t=1;t<=T;t++)
{
    long long b,m;
		in>>b>>m;
		long long mx;
		int j=0;
		int ans[b+1][b+1];
		memset(ans,0,sizeof(int)*(b+1)*(b+1));
		for (int  i = b-1;  i>0;  i--) {
				mx=pow(2,j++);
		}
		if(m>mx)
		{
				out<<"Case #"<<t<<": "<<"IMPOSSIBLE"<<endl;
		}
		else
		{
				long long temp =m;
				int k=0;
				while(temp>0)
				{
						if((temp&1)==1)
						{
								int index=b-k-1;
								if(index!=1)
								ans[1][index]=1;

								for (int  i = index;  i <b;  i++) {
											for (int  j = i+1;  j <=b;  j++) {
												ans[i][j]=1;
											}
								}
						}
						temp=temp>>1;
						k++;
				}
				out<<"Case #"<<t<<": "<<"POSSIBLE"<<endl;
				for (int  i = 1;  i <=b;  i++) {
							for (int  j = 1;  j <=b;  j++) {
								out<<ans[i][j];
							}
							out<<endl;
				}
		}

}

return 0;
}

