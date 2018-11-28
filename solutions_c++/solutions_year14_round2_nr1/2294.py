#include "iostream"
#include "bitset"
#include "cstdio"
#include "cstring"
#include "string"
#include "vector"
#include "cmath"
#include "algorithm"
using namespace std;

#define FOR(count) for(int i=0;i<(count);i++)
#define FORi(i,count) for(int i=0;i<(count);i++)
#define FOR2(from,to) for(int i=(from);i<=(to);i++)
#define FOR2i(i,from,to) for(int i=(from);i<=(to);i++)
#define long long ll

#define MAX 105

void compress(char* s,char* d){
	int ind1=0,t=0;
	int ind2=0, tm=0;
	//cout<<s<<"\t";
	while(s[ind1]!='\0'){
		t=ind1;
		//cout<<s[t];
		while(s[t]==s[ind1]){
			ind1++;
		}
		d[ind2++]=s[t];
		//ind1;
	}
	//cout<<"\t"<<d<<endl;
}

int Max(int a,int b){
	return (a>b?a:b);
}

int main(){
	#ifdef codejam
		freopen("out.txt","w",stdout);
	#endif

	int T,n=1;
	cin>>T;


	int res=0,pos=0,loc=0;

	char** str;
	char *s,stmp[MAX+2];


	FORi(t,T){
		cin>>n;

		res=-1;
		str= new char*[n];
		FOR(n){
			str[i]= new char[MAX];
			cin>>str[i];
			//compress(stmp,str[i]);
			//res=Max(res,strlen(stmp)- strlen(str[i]));
			//if(i!=0) pos=strcmp(str[i],str[i-1])==0?1:0;
		}
		//pos=1;
		//cout<<res<<endl;
		
		int x=0,y=0;
		res=0; pos=1;
		char ch;

		while(str[0][x]!='\0' && str[1][y]!='\0'){
			ch=str[0][x];
			if(str[0][x]==str[1][y]){
				//cout<<"Found eq at : "<<x<<"\t"<<y<<endl;
				while(str[0][x]==ch && ch==str[1][y]){
					x++;y++;
				}
				while(str[0][x]==ch){x++;res++;}
				while(str[1][y]==ch){y++;res++;}
			}
			else{
				//cout<<x<<" "<<y<<"\tnot pos\n";
				pos=0;
				break;	
			}
		}
		if(str[0][x]!='\0' || str[1][y]!='\0') pos=0;

		delete[] str;
		if(pos)
			printf("Case #%d: %d\n",t+1,res);
		else
			printf("Case #%d: Fegla Won\n",t+1);
	}

	return 0;
}