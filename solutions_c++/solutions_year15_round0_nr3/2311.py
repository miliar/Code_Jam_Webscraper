#include<bits/stdc++.h>
using namespace std;
long long sign=1;
long long s[5][5],arr[5][5],in[4],sn[4];
long long fn(long long y,char c){
	long long x;
	if(c=='i')
		x=2;
	else if(c=='j')
		x=3;
	else if(c=='k')
		x=4;
	else 
		x=1;
		
	sign=sign*s[y][x];
	return arr[y][x];
}
char fc(long long x){
	if(x==1)
		return '1';
	else if(x==2)
		return 'i';
	else if(x==3)
		return 'j';
	else 
		return 'k';	
}
int main(){
	long long t,a,b,c,l,x,ans,flag,flag2;
	string str;
	for(long long i=1;i<=4;i++)
		arr[1][i]=i;
	for(long long i=1;i<=4;i++){
		for(long long j=1;j<=4;j++){
			s[i][j]=1;
		}
	}
	arr[2][1]=2;
	arr[2][2]=1;
	arr[2][3]=4;
	arr[2][4]=3;
	arr[3][1]=3;
	arr[3][2]=4;
	arr[3][3]=1;
	arr[3][4]=2;
	arr[4][1]=4;
	arr[4][2]=3;
	arr[4][3]=2;
	arr[4][4]=1;
	s[2][2]=-1;
	s[2][4]=-1;
	s[3][2]=-1;
	s[3][3]=-1;
	s[4][3]=-1;
	s[4][4]=-1;
	ifstream input;
 	ofstream output;
 	input.open("codejamc.txt");
 	output.open("answer.txt");
	input>>t;
	//output<<t<<endl;
	long long no=t,z;
	while(t--){
		
		input>>l>>x;
		input>>str;
		
		ans=0;
		flag=0;
		flag2=0;
		sign=1;
		in[1]=1;
		for(long long i=0;i<l;i++)
			in[1]=fn(in[1],str[i]);
		sn[1]=sign;
		char ch=fc(in[1]);
		//output<<ch<<endl;
		sign=1;
		in[2]=fn(in[1],ch);
		sn[2]=sn[1]*sn[1]*sign;
		sign=1;
		in[3]=fn(in[2],ch);
		sn[3]=sn[2]*sn[1]*sign;
		in[0]=1;
		sn[0]=1;
		//for(int i=0;i<4;i++){
			//output<<in[i]<<" "<<sn[i]<<endl;
		//}
		sign=1;	
		a=1;
		b=1;
		c=1;
		
		for(long long i=0;i<min((l*5),x*l);i++){
			a=fn(a,str[i%l]);
			//output<<a<<" "<<sign<<"A "<<endl;
			
			if(sign==1&&a==2){
				flag=1;
				for(long long j=i+1;j<min(l*x,(i+1+6*l));j++){
					b=fn(b,str[j%l]);
				//	output<<b<<" "<<sign<<"B "<<endl;
					if(b==3&&sign==1){
						
						
						for(long long k=j+1;;k++){
							
							c=fn(c,str[k%l]);
								z=(k+1)/l;
							if((k+1)%l==0){
								//output<<z<<" "<<endl;
								z=x-z;
								z=z%4;
								//output<<c<<" "<<z<<" "<<in[z]<<" "<<sn[z]<<" "<<sign<<endl;
								if( ( fn(c,fc(in[z]))==4)&&(sign*sn[z]==1) ){
									ans=1;
								}
								
								break;
							}
							
							//output<<c<<" "<<sign<<"C "<<endl;
						}
						break;
						
					}
					
					
				}
				
				
					break;	
					
			}
			
		}
		if(ans==0){
			output<<"Case #"<<no-t<<": "<<"NO\n";
		}
		else{
			output<<"Case #"<<no-t<<": "<<"YES\n";
		}
	}
	return 0;
}
