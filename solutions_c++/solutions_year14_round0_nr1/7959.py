#include <cstdio>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <cassert>
#include <sstream>
#include <bitset>
#include <numeric>
#include <climits>
#include <string>
#include <cctype>
#include <ctime>
#include <iomanip>
#include <cmath>
#include <vector>
#include <queue>
#include <list>
#include <map>
#include <set>
#define maxl 1000000000
using namespace std;
#ifndef __WATASHI__
struct $ {
  $(const char* input, const char* output) {
    freopen(input, "r", stdin);
    freopen(output, "w", stdout);
  }
} $("A-small-attempt4.in" ,"A-small-attempt4.out");
#endif

void solve(){
	
	int i,j,now,x;
	int ans1,ans2,tru_num,bad_magic,cheat_v,n_find;
int card1[16],card2[16],find[4];
	n_find=0;
	tru_num=0;
bad_magic=0;
cheat_v=1;
		//scanf("%lf %lf %lf",&C,&F,&X);
	cin>>ans1;
	for(i=0;i<16;i++)
		cin>>card1[i];
	cin>>ans2;
	for(i=0;i<16;i++)
		cin>>card2[i];
		for(j=0;j<4;j++)
	{
		for(i=0;i<4;i++)
		{
			if(card1[(ans1-1)*4+j]==card2[(ans2-1)*4+i])
			{
				cheat_v=0;
				//cout<<card1[(ans1-1)*4+j]<<"=="<<card2[(ans2-1)*4+i]<<endl;
				tru_num=card1[(ans1-1)*4+j];
				n_find++;
				//cout<<n_find;
			}
			else
			{
				//cout<<card1[(ans1-1)*4+j]<<"!="<<card2[(ans2-1)*4+i]<<endl;
			}
		}
	}
	/*for(j=1;j<=4;j++)
	{
		
		if(cheat_v==0)
		for(i=0;i<16;i++)
		{
			if(card2[(ans2-1)*4+j-1]==card1[i])
			{
				if((j-2<0)||(j-3>=0&&find[j-2]!=i/4+1&&find[j-3]!=i/4+1)||(j==2&&find[j-2]!=i/4+1))
				{
					find[j-1]=i/4+1;
					if(find[j-1]==ans1)
					{
						tru_num=card1[i];
						cout<<card1[i]<<" in line"<<find[j-1]<<endl;
						n_find++;
					}
					
				}
				/else if((j-3>=0&&(find[j-2]==i/4+1||find[j-3]==i/4+1))||(j==2&&find[j-2]==i/4+1))
				{	cout<<card2[i]<<" in line"<<i/4+1<<endl;
                   bad_magic=1;
				}
		/

			}
		}
	}*/
//	if((find[0]+find[1]+find[2]+find[3])!=10)
//		bad_magic=1;
	if(n_find>1) bad_magic=1;
	if(cheat_v==1)
		cout<<"Volunteer cheated!";
	else if(bad_magic==1)
		cout<<"Bad magician!";
	else
		cout<<tru_num;
	cout<<endl;
}

int main(){
	ios::sync_with_stdio(false);
	int t,i;
	cin>>t;
	for(int i=1;i<=t;++i){
		cout<<"Case #"<<i<<": ";
		solve();
	}
	return 0;
}