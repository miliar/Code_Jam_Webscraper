/*AUTHOR:PUNIT PATEL*/
#include<bits/stdc++.h>
using namespace std;
int reverse(int startindex,int endindex,char string[]){
	char temp1,temp2;
//	int count = 0
	if(endindex==-1)
		return 0;
	for(int i=startindex;i<=endindex;i++){
		temp1=string[i];
		temp2=string[endindex];
		if(temp1=='+')
			string[endindex]='-';
		else
			string[endindex]='+';
		if(temp2=='+')
			string[i]='-';
		else
			string[i]='+';
		endindex-=1;
	}
	return 1;
}
int main(){
	//freopen("C:\\Users\\P\\Downloads\\B-large.in","r+",stdin);
	//freopen("C:\\Users\\P\\Desktop\\punit\\output_large.txt","w",stdout);
	int test_case,tm=1,i,j,k,count;
	char str[101];
	cin>>test_case;
	while(tm<=test_case){
		count=0;
		cin>>str;
		//cout<<endl<<str;
		while(1){
			for(k=0;k<strlen(str);k++)
				if(str[k]=='-')
					break;
			//cout<<"k="<<k<<endl;
			if(k==strlen(str))
				break;
			for(i=strlen(str)-1;i>=0;i--)
				if(str[i]=='-')
					break;
			//cout<<"i="<<i<<endl;
			for(j=0;j<strlen(str);j++)
				if(str[j]=='-')
					break;
		//	cout<<"j="<<j<<endl;
			count+=reverse(0,j-1,str);
			//if(i!=0 && j!= strlen(str))
			count+=reverse(0,i,str);
		//	break;
		}
		cout<<"Case #"<<tm<<": "<<count<<endl;
		tm++;
	}
	return 0;
}
