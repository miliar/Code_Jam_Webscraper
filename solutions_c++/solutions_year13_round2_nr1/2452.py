#include<iostream>

using namespace std;

void bubleSort(int *a,int s){
	int i,j,tmp;
	for(i=0;i<s;i++){
		for(j=i+1;j<s;j++){
			if(a[j]<a[i]){
				tmp = a[j];
				a[j] = a[i];
				a[i] = tmp;
			}
		}
	}
}

int ceil(int x,int y){
	int k=0;
	while(y>=x){
		x += x-1;
		k++;
	}
	return k;
}
int ceil2(int x,int y){
	while(y>=x){
		x += x-1;
	}
	return x;
}

int minMove(int as,int *list,int s){
	int i,cnt=0,t1=0,t2=0;
	if(as == 1)
		return s;	
	for(i=0;i<s;i++){
		if(as>list[i]){
			as += list[i];
		}
		else if(ceil(as,list[i]) < s-i){
			cnt+=ceil(as,list[i]);
			as = ceil2(as,list[i])+list[i];
		}
		else{
			cnt+=s-i;
			break;
		}
	}
	
	return cnt;
}


int main(){
	int *ms,j,t,i,as,n;
	cin>>t;
	for(i=0;i<t;i++){
		cin>>as>>n;
		ms = new int[n];
		for(j=0;j<n;j++){
			cin>>ms[j];
		}
		bubleSort(ms,n);
		cout<<"Case #"<<i+1<<": "<<minMove(as,ms,n)<<endl;

		delete ms;
	}

	return 0;
}
