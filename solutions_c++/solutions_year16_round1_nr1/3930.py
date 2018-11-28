#include<iostream>
using namespace std;

int main(){

	freopen("A-large.in","r",stdin);
    freopen("output.txt","w",stdout);

	int test,t=0,beg,end,pos,len;
	string str,str2;
	char start;
	cin>>test;
	while(t<test){
		cin>>str;
		str2=str;
		len=str.length();
		int val[len] = {0};
		beg=0, end=0;
		start=str[0];
		for(int i=1;i<len;i++){
			if(str[i]>=start){
				beg--;
				val[i] = beg;
				start = str[i];
			}
			else{
				end++;
				val[i] = end;
			}
		}
		for(int i=0;i<len;i++){
			pos = val[i]-beg;
			str2[pos] = str[i];
		}
			cout<<"Case #"<<t+1<<": "<<str2<<endl;
		t++;
	}

return 0;
}
