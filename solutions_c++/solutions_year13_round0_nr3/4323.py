#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <iostream>
using namespace std;
bool huiwen(long long c)
{
	char chArr[200];
	sprintf(chArr,"%lld",c);
	int len = strlen(chArr);
	for(int i = 0;i< len /2;i++)
		if(chArr[i] != chArr[len-(i+1)])
			return false;
	return true;
}
long long a[100000];
int table()
{
	int k =0;
	for(long long i = 1; i <= 10000000;i++)
		{
			if(huiwen(i) && huiwen(i * i))
			{
				//printf("%lld\n",i * i);
				a[k ++] = i*i;
			}
		}
	return k;
}
struct FLAG  
{  
    int right;  
    bool if_have;  
};  
struct FLAG erfen3(int left,int right,long long x)      //如果找到了x就返回相应的位置，且FLAG.if_have 是true，如果没有找到，就返回刚好比x的那个数的位置，且FLAG.if_have=false  
{  
    struct FLAG flag;  
    flag.if_have=false;  
    while(left<=right)  
    {  
        int mid=(left+right)/2;  
        if(a[mid]==x)  
        {  
            flag.if_have=true;  
            flag.right=mid;  
            return flag;  
        } 
        if(a[mid]>x&& a[mid-1]<x)  
        {  
            flag.if_have=false;  
            flag.right=mid;  
            return flag;  
        }  
        else if(a[mid]<x)  
            left=mid+1;  
        else  
            right=mid-1;  
    }  
    flag.if_have=false;     //x比最大的数都大，做标记  
    flag.right=-1;  
    return flag;  
}  
int main()
{
	//freopen("in.in","r",stdin);
	//freopen("lyo2.txt","w",stdout);
	long long ncase,start,end,tmpNcase = 0;
	cin>>ncase;
	int len = table() - 1;
	while(ncase --)
	{
		tmpNcase ++;
		int cnt = 0;
		cin>>start>>end;
		int qian = 0  ,hou=0;
		if(start > 4004009004004)
		{
			printf("Case #%lld: %d\n",tmpNcase,0);
			continue;
		}
		else if(start == 4004009004004)
		{
			printf("Case #%lld: %d\n",tmpNcase,1);
			continue;
		}

		qian = erfen3(0,len,start).right;
		if(end >= 4004009004004)
		{
			hou  = 38;
			printf("Case #%lld: %d\n",tmpNcase,hou - qian + 1);
		}
		else
		{
			hou  = erfen3(0,len,end).right;	
			bool flagHou = true;
			if(erfen3(0,len,end).if_have == false)
				flagHou  = false;
			if(flagHou == true)
				printf("Case #%lld: %d\n",tmpNcase,hou - qian + 1);
			else
				printf("Case #%lld: %d\n",tmpNcase,hou - qian);
		}

	}
	return 0;
}