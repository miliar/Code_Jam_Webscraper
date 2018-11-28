#include<bits/stdc++.h>
using namespace std;
 
#define rep(i,n) for(i=0;i<n;i++)
#define ll long long
#define elif else if
#define ff first
#define ss second
#define pii pair<ll int,ll int>
#define mp make_pair
#define pb push_back
#define CLEAR(array, value) memset(ptr, value, sizeof(array));
#define si(a)     scanf("%d", &a)
#define sl(a)     scanf("%lld", &a)
#define pi(a)     printf("%d", a)
#define pl(a)     printf("%lld", a)
#define pn        printf("\n")

char a[3000];

int main()
{
	freopen("A-large.in","r",stdin);
	freopen("outputLarge.txt","w",stdout);
	int f,r,t,i,j,l,k,x;
	char ch;
	char tab2[1024];
    string str;
    si(t);
    for(i=1;i<=t;i++){
	cin>>str;
	ch=0;
	l=str.length();
    strncpy(tab2, str.c_str(), sizeof(tab2));
    ch=tab2[0];
    f=r=1500;
    a[1500]=ch;
    for(j=1;j<l;j++){
    	if(tab2[j]<ch){
    		r++;
    		a[r]=tab2[j];
		}
		if(tab2[j]==ch){
			f--;
			a[f]=tab2[j];
		}
		if(tab2[j]>ch){
			f--;
			a[f]=tab2[j];
			ch=tab2[j];
		}
	}
	for(k=0;k<3000;k++)
	if(a[k]!=0)
	break;
	cout<<"Case #"<<i<<": ";
	for(x=k;x<k+l;x++){
	cout<<a[x];
	a[x]=0;
}
	cout<<endl;
	
    
}
return 0;	
} 
