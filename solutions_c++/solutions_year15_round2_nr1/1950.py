#include<bits/stdc++.h>
#define N 1100000
using namespace std;
int arr[N];
/*int rec(int x){
	if(x<=19) return x;
	if(arr[x]) return arr[x];
	if(v[x]) return N;
	else{
		v[x]=1;
		int cur=x;
		int rev=0, f1=0, f2=0;
		while(x){
			int temp=x%10;
			rev*=10;
			rev+=temp;
			x/=10;
			f1++;
		}
		x=cur;
		int xx=rev;
		while(xx){
			f2++;
			xx/=10;
		}
		int v1=rec(x-1);
		int v2=N;
		if(f1==f2) v2=rec(rev);
		arr[x]=min(v1,v2);
		arr[x]++;
		v[x]=0;
		return arr[x];
	}
}*/
int main(){
	int t;
	cin>>t;
    for(int i=0; i<=1000000; i++){
        arr[i]=999999;
        if(i<=20) arr[i]=i;
        int f1=0,f2=0;
        int val=i;
        int rev=0;
        while(val){
            f1++;
            rev=rev*10 + val%10;
            val/=10;
        }
        
        int kk=rev;
        while(kk){
            kk/=10, f2++;
        }
        if(rev<i && rev>0 && f1==f2){
            arr[i]=arr[rev];
        }
        arr[i]=min(arr[i],arr[i-1]);
        arr[i]++;
    }
    int num=0;
	while(t--){
		num++;
		int n;
		cin>>n;
		//arr[n]=rec(n);
		cout<<"Case #"<<num<<": "<<arr[n]<<endl;
	}
}
