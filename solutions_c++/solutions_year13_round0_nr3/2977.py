#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
using namespace std;
bool palindrome(int valu)
{
	vector<int> dig;
	while(valu)
	{
	    dig.push_back(valu%10);
	    valu/=10;
	}

	int len=(int)dig.size();
	for(int i=0;i<len;i++)
        if(dig[i]!=dig[len-1-i])
            return false;
	return true;
}
bool judge(int valu)
{
	int squ=(int)sqrt(valu*1.0);
	if(squ*squ!=valu) return false;

	bool flag1=palindrome(squ);
	bool flag2=palindrome(valu);
	if(flag1&&flag2) return true;
	return false;

}
int main()
{
	freopen("C-small-attempt2.in","r",stdin);
	freopen("out.txt","w",stdout);
	int t,t_cnt=0;
	scanf("%d",&t);
	while(t--)
	{
		int A,B,cnt=0;
		scanf("%d%d",&A,&B);
		for(int i=A;i<=B;i++) if(judge(i))
		{
			 cnt++; 
		}
		printf("Case #%d: %d\n",++t_cnt,cnt);
	}
	return 0;
}

