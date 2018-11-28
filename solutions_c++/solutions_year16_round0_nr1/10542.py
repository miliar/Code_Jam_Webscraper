#include<iostream>
#include<stdio.h>
#include<set>
using namespace std;
int main(){
    int T,i,temp;
    long long int N,num,val;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w+",stdout);
    cin>>T;
    for(int j=1;j<=T;j++){
        set<int>s;
        cin>>N;
        i=1;
        if(N==0){
            cout<<"Case #"<<j<<": INSOMNIA"<<endl;
        }
        else{
	       while(s.size()!=10){
		      val=i*N;
		      i++;
		      num=val;
		      while(num){
		          temp=num%10;
		          num/=10;
		          s.insert(temp);
		          if(s.size()==10)
			         break;
		      }
	       }
          cout<<"Case #"<<j<<": "<<val<<endl;
        }
    }
    return 0;
}
