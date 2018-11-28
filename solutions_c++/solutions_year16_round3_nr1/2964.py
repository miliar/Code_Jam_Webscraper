#include<iostream>
#include<string>
#include<sstream>
#include<cstring>
#include<math.h>
#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<vector>
#include<algorithm>
using namespace std;
#define sd(a) scanf("%d",&a)
#define sl(a) scanf("%ld",&a)
#define sll(a) scanf("%lld",&a)
#define sc(a) printf("%c",&a)
#define pd(a) printf("%d ",a)
#define pl(a) printf("%ld ",a)
#define pll(a) printf("%lld ",a)
#define pc(a) printf("%c",a)
#define pf(a) printf("%s",a);
#define f(i,n) for(i=0;i<n;i++)
#define flu(i,l,u) for(i=l;i<u;i++)
#define max(a,b) a>b?a:b
struct ele{
	int d;
	char c;

};

void max_heapify(ele *a, int i, int n)
{
    int j;
	ele temp;
    temp = a[i];
    j = 2 * i;
    while (j <= n)
    {
        if (j < n && a[j+1].d > a[j].d)
            j = j + 1;
        if (temp.d > a[j].d)
            break;
        else if (temp.d <= a[j].d)
        {
            a[j / 2] = a[j];
            j = 2 * j;
        }
    }
    a[j/2] = temp;
    return;
}
void build_maxheap(ele *a,int n)
{
    int i;
    for(i = n/2; i >= 1; i--)
    {
        max_heapify(a,i,n);
    }
}
int main(){
	int t,n;
	ele x1,x2,x3;
	ele a[27];
	cin>>t;
	for(int i=1;i<=t;i++){
		cin>>n;
		cout<<"Case #"<<i<<": ";
		for(int j=1;j<=n;j++){
			cin>>a[j].d;
			a[j].c = ' ';
			a[j].c = (char) 64+j;
		}
		build_maxheap(a,n);
		
		while(a[1].d>0){	
			if(a[1].d>a[2].d&&a[1].d>a[3].d){
				a[1].d--;
				cout<<a[1].c<<" ";
				build_maxheap(a,n);
			}else if(a[1].d==a[2].d&&a[1].d>a[3].d){
				a[1].d--;
				a[2].d--;
				cout<<a[1].c<<a[2].c<<" ";
				build_maxheap(a,n);
			}else if(a[1].d>a[2].d&&a[1].d==a[3].d){
				a[1].d--;
				a[3].d--;
				cout<<a[1].c<<a[3].c<<" ";
				build_maxheap(a,n);
			}else if(a[1].d==a[2].d&&a[1].d==a[3].d){
				a[1].d--;
				cout<<a[1].c<<" ";
				build_maxheap(a,n);
			}
		}
		cout<<"\n";
	}
	return 0;
}
