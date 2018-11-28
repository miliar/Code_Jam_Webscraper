#include<iostream>
#include<cmath>
#include<string>
#include<stdio.h>
using namespace std;
struct num{
	int a[111],len;
}A,B,a,b,ans[43001];
void mult(num a){
	int i,j;
	b.len=a.len*2-1;
	for(i=1;i<=b.len+1;i++) b.a[i]=0;
	for(i=1;i<=a.len;i++){
		for(j=1;j<=a.len;j++){
			b.a[i+j-1]+=a.a[i]*a.a[j];
		}
	}
	for(i=1;i<=b.len;i++){
		b.a[i+1]+=(b.a[i])/10;
		b.a[i]%=10;
	}
	if(b.a[b.len+1]) b.len++;
}
void out(num a){
	int i;
	for(i=a.len;i>=1;i--) printf("%d",a.a[i]);
	printf("\n");
}
int pan1(num a){
	int i;
	for(i=1;i<=a.len/2;i++) if(a.a[i]!=a.a[a.len-i+1]) return(0);
	return(1);
}
int pan2(num a){
	int i,t=0;
	for(i=1;i<=a.len;i++){
		t=t+a.a[i]*a.a[a.len-i+1];
	}
	if(t>9) return(0);
	return(1);
}
int pan(num a){
	mult(a);
	//out(a);
	//out(b);
	//cout<<" "<<b.len<<" "<<pan1(b)<<endl;
	if(pan1(b)) return(1);
	return(0);
}
int comp(num a,num b){
	if(a.len>b.len) return(1);
	if(a.len<b.len) return(-1);
	int i;
	for(i=a.len;i>=1;i--){
		if(a.a[i]>b.a[i]) return(1);
		if(a.a[i]<b.a[i]) return(-1);
	}
	return(0);
}
int s;
void create(int x,int n,int sum){
	if(x>(n+1)/2){
		a.len=n;
		if(pan(a)){
			s++;
			mult(a);
			ans[s]=b;
			//out(a);
		}
		return;
	}
	int i,t;
	for(i=0;i<=2;i++){
		if(x==1&&i==0) continue;
		if(n%2&&x==(n+1)/2) t=i*i;
		else t=2*i*i;
		if(sum-t<0) break;
		a.a[x]=a.a[n-x+1]=i;
		create(x+1,n,sum-t);
	}
}
void init(){
	int i,j;
	create(1,1,9);
	s++;
	ans[s].len=1;ans[s].a[1]=9;
	for(i=2;i<=50;i++){
		create(1,i,9);
	}
	//cout<<s;
}
int find(num a){
	int l,r,mid,t;
	l=0;r=s;
	while(l<r){
		mid=(l+r+1)/2;
		t=comp(ans[mid],a);
		if(t==0) return(mid);
		if(t>0) r=mid-1;
		else l=mid;
	}
	return(l);
}
void Minus(num &a){
	int i;
	a.a[1]--;
	for(i=1;i<=a.len;i++){
		if(a.a[i]<0){
			a.a[i]+=10;
			a.a[i+1]--;
		}
	}
	if(a.a[a.len]==0) a.len--;
}
void work(){
	char s[120];
	int i;
	cin>>s;
	A.len=B.len=0;
	for(i=strlen(s)-1;i>=0;i--){
		A.a[++A.len]=s[i]-'0';
	}
	cin>>s;
	for(i=strlen(s)-1;i>=0;i--){
		B.a[++B.len]=s[i]-'0';
	}
	Minus(A);
	cout<<find(B)-find(A)<<endl;
}
int main(){
    //freopen("C-large-2.in","r",stdin);
    //freopen("c.out","w",stdout);
    int T,i;
    cin>>T;
    init();
    for(i=1;i<=T;i++){
		printf("Case #%d: ",i);
		work();
	}
}
