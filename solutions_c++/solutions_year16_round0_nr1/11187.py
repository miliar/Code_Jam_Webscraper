#include<bits/stdc++.h>
using namespace std;
int array [10];
void build(){
	for(int i=0;i<10;i++)
	  array[i]=0;
}

bool check(){
	bool flag = true;;
	for(int i=0;i<10;i++){
		if(array[i]==0)
		{
			flag = false;
			break;
		}
	}
	return (!flag)? false:true;
}

bool parse_and_update(long long int x){
	bool flag = false;
	while(x>0){
	  long long int a = x%10;
          x = x/10;
     if (array[a]==0)
     	array[a]=1;
     	
      if(check())
      {
      	flag = true;
      	break;
      }
	}
     return flag;
}

long long int Csheep(long long int n){
	long long int b = n;
	bool flag = false;
	for(int i=1;i<1000000;i++){
		b =i*n;
		if(parse_and_update(b))
		 {
		 	flag = true;
		 	break;
		 }
	}
	if(flag)
		return b;
		else
	      return 0;
}

int main(){
	freopen("A-large.in","r",stdin);
	freopen("large.out","w",stdout);
	int t;
	cin>>t;
	for(int i=0;i<t;i++)
	{
		build();
	long long int x;
	cin>>x;
	long long int q = Csheep(x);
	if(q==0)
	 cout<<"Case "<<"#"<<i+1<<": "<<"INSOMNIA"<<endl;
	 else
	  cout<<"Case "<<"#"<<i+1<<": "<<q<<endl;
   }
}
