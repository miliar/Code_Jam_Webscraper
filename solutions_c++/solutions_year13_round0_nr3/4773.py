#include<cstdio>
#include<iostream>
#include<cstring>
#include<cmath>
#include<vector>
#include<algorithm>
using namespace std;
#define ull unsigned long long int
vector<int>q;


int oneDigit(int num)
{
     return (num >= 0 && num < 10);
}


bool isPalUtil(int num, int* dupNum)
{
	if (oneDigit(num))
        return (num==(*dupNum)%10);

  	if(!isPalUtil(num/10,dupNum))
        return false;
 	*dupNum/=10;
 	return (num%10==(*dupNum)%10);
}


int isPal(int num)
{
    if (num < 0)
       num = -num;
	int *dupNum = new int(num);
 	return isPalUtil(num, dupNum);
}



int main()
{
	int t;
	int a,b,r=1,i,count=0,low;

	freopen("C-small-attempt0.in","r",stdin);
	freopen("out3.txt","w",stdout);

	for(i=1;i*i<=1000;i++)
	{
		if(isPal(i) && isPal(i*i))
		{
            q.push_back(i*i);
		}
	}

	cin>>t;
	while(t--)
	{
		cin>>a>>b;

		int s=q.size();

		i=0;
        while(q[i]<a)
        i++;
        count=0;
        for(;i<s;i++)
        {
            if(q[i]>b)
            break;
            else count++;
        }

		printf("Case #%d: %d\n",r++,count);

	}
	return 0;
}
