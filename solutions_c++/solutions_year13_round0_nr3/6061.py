#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
using namespace std;

int t,a,b;

int res[1010];

void update(int idx,int val)
{   while(idx<=1000)
    {   res[idx]+=val;
        idx+=(idx & -idx);
    }
}       

int read(int idx){
	int sum = 0;
	while (idx > 0){
		sum += res[idx];
		idx -= (idx & -idx);
	}
	return sum;
}
          
            
void pre_compute()
{   update(1,1);  
    update(4,1);
    update(9,1);
    update(121,1);
    update(484,1);    
    
}       

int main()
{   scanf("%d",&t);
    int m=1;
    memset(res,0,sizeof(res));
    
    pre_compute();
    while(t--)
    {   scanf("%d",&a);
        scanf("%d",&b);
        int p=read(b)-read(a-1);
       printf("Case #%d: %d\n",m++,p);
       }    
   //system("pause");
}          

      
